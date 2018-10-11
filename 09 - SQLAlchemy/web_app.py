from datetime import datetime, timedelta
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_, or_
from sqlalchemy.pool import StaticPool

connection_string = 'sqlite:///hawaii.sqlite'
engine = create_engine(connection_string, connect_args={'check_same_thread':False}, poolclass=StaticPool)
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)    

def get_year_range():
    max_date_s = session.query(func.max(Measurement.date)).one()[0]
    max_date = datetime.strptime(max_date_s, '%Y-%m-%d')
    year_ago_from_max_date = max_date - timedelta(365)
    year_ago_from_max_date_s = datetime.strftime(year_ago_from_max_date, '%Y-%m-%d')
    return year_ago_from_max_date_s, max_date_s

def get_measurements(date_range=None):
    if not date_range:
        date_range = get_year_range()
    query = session.query(Measurement).filter(Measurement.date >= date_range[0])
    if len(date_range) > 1 and date_range:
        query = query.filter(Measurement.date <= date_range[1])
    return query.all()

def get_temperature_aggregates(date_range=None):
    if not date_range:
        date_range = get_year_range()
    query = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= date_range[0])
    if len(date_range) > 1 and date_range[1]:
        query = query.filter(Measurement.date <= date_range[1])
    data = query.first()
    return {
        'tmin': data[0],
        'tavg': data[1],
        'tmax': data[2]
    }


@app.route('/')
def home():
    return '''
    <h1>Available endpoints:</h1>
    <ul>
        <li><a href="http://localhost:5000/api/v1.0/precipitation">Precipitation data for the last year</a></li>
    </ul>
    <ul>
        <li><a href="http://localhost:5000/api/v1.0/stations">List of all stations</a></li>
    </ul>
    <ul>
        <li><a href="http://localhost:5000/api/v1.0/tobs">Temperature data for the last year</a></li>
    </ul>
    <ul>
        <li><a href="http://localhost:5000/api/v1.0/tobs/2017-01-01/2017-01-01">Temperature range for specific period</a></li>
    </ul>
    '''

@app.route('/api/v1.0/precipitation')
def precipitation():
    measurements = get_measurements()
    result = {}
    for measurement in measurements:
        precipitation = result.setdefault(measurement.date, [])
        precipitation.append({
            'station': measurement.station,
            'precipitation': measurement.prcp
        })
    return jsonify(result)

@app.route('/api/v1.0/stations')
def stations():
    stations = session.query(Station).all()
    result = [
        {
            'id': station.id,
            'station': station.station,
            'name': station.name,
            'latitude': station.latitude,
            'longitude': station.longitude,
            'elevation': station.elevation
        }
        for station in stations
    ]
    return jsonify(result)

@app.route('/api/v1.0/tobs')
def temperature():
    measurements = get_measurements()
    result = {}
    for measurement in measurements:
        precipitation = result.setdefault(measurement.date, [])
        precipitation.append({
            'station': measurement.station,
            'tobs': measurement.tobs
        })
    return jsonify(result)

@app.route('/api/v1.0', defaults={ 'start': None, 'end': None })
@app.route('/api/v1.0/<start>', defaults={  'end': None })
@app.route('/api/v1.0/<start>/<end>')
def temperature_aggregated(start, end):
    app.logger.info(f'Start date - {start}, end date - {end}')
    if not(start) and not(end):
        return jsonify(get_temperature_aggregates())
    if end:
        try:
            datetime.strptime(end, '%Y-%m-%d')
        except ValueError:
            return jsonify({ 'error': 'End date must be in format \'YYYY-MM-DD\''}), 400
    if start:
        try:
            datetime.strptime(start, '%Y-%m-%d')
        except ValueError:
            return jsonify({ 'error': 'Start date must be in format \'YYYY-MM-DD\''}), 400
    if start and end and start > end:
        return jsonify({ 'error': 'Start date must be less than or equal than end date'}), 400
    return jsonify(get_temperature_aggregates((start, end)))

if __name__ == '__main__':
    app.run()