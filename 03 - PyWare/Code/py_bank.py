import os
import csv
import sys
# First of all lets make our script to look for the required file in several places (just in case and for potential simplicity of use)
_file_name = 'budget_data.csv'
_file_locations = [ 
    _file_name,
    os.path.join('..', _file_name),
    os.path.join('Input', _file_name),
    os.path.join('..', 'Input', _file_name)
    ]


def print_separator():
    '''Print a horizontal line having a standard console window width (80 symbols).'''
    print(''.rjust(80, '-'))

def get_data_path() -> str:
    '''
    Look for the data file in all predefined locations.
    
    :return: the relative path to the data file
    :rtype: str
    '''
    for location in _file_locations:
        if os.path.exists(location):
            return location
    return ''

def report_no_data_file():    
    '''Print the information on data file that was not found and on all locations it has been looked for.'''
    print_separator()
    print('The input file was not found. Please place it at one of the following locations:')
    for location in _file_locations:
        print(location)
    print_separator()

def get_data(path: str):
    '''
    Open the CSV file at the specified path and convert its content into analyzable format.

    :param str path: A path to the data file
    :return: Data point collection
    :rtype: [(str, int)]
    '''
    with open(path, 'r', encoding='UTF-8',newline='') as input_file:
        csv_reader = csv.reader(input_file)
        # Skipping headers line
        next(csv_reader)
        return [(line[0], int(line[1])) for line in csv_reader]

def report_no_data():
    '''Print the information on being unable to perform the analysis due to the lack of the data points.'''
    print_separator()
    print('There is not enough data to perform financial analysis')
    print_separator()    

def analyze(data):
    '''
    Perform the analysis of the incoming month-pnl pairs and aggregates some statistics.

    :param [(str, int)] data: Data point collection
    :return: Statistics on months count, total PnL, average PnL change, greatest PnL increase (or None) and greatest PnL decrease (or None)
    :rtype: (int, int, float, (str, int), (str, int))
    '''
    months_count = len(data)
    total_pnl = data[0][1]
    pnl_change_list = []
    # Though we could start calculations from 0 index, the below approach saves us extra check for the index on every iteration 
    # (we can't calculate the change for the very first data point)
    for i in range(1, months_count):
        total_pnl += data[i][1]
        pnl_change_list.append((data[i][0], data[i][1] - data[i - 1][1]))
    # Simply walk through all data points to find max/min
    max_pnl_increase = pnl_change_list[0]
    min_pnl_decrease = pnl_change_list[0]
    for pnl_change in pnl_change_list:
        if pnl_change[1] > max_pnl_increase[1]:
            max_pnl_increase = pnl_change
        if pnl_change[1] < min_pnl_decrease[1]:
            min_pnl_decrease = pnl_change
    # The straightforward way of calculating the average change would be to sum all average changes and divide it by the number of these changes
    # But a little trick will allow us to reduce it to just one division:
    # The sum of changes would look like this: Diff(1,0) + Diff(2,1) + ... + Diff(n - 1, n - 2) where n - number of data points (DP).
    # And it expands into (DP1 - DP0) + (DP2 - DP1) + ... + (DPn-2 - DPn-3) + (DPn-1 - DPn-2) = DPn-1 - DP0
    # The number of changes equals to the number of data points minus one
    average_pnl_change = (data[-1][1] - data[0][1]) / (months_count - 1)
    # Also it may happen that all changes are non-negative (non-positive).
    # In these cases we won't be able to make a conclusion on greatest decrease (greatest increase respectively) 
    return (
        months_count,
        total_pnl,
        average_pnl_change,
        None if max_pnl_increase[1] <= 0 else max_pnl_increase,
        None if min_pnl_decrease[1] >= 0 else min_pnl_decrease
    )

def output_analysis(analysis):
    '''
    Print the contents of financial analysis.

    :param (int, int, float, (str, int), (str, int)) analysis: financial analysis
    '''
    print_separator()
    print('Financial Analysis')
    print_separator()
    print(f'Total Months: {analysis[0]}')
    print(f'Total PnL: ${analysis[1]}')
    print(f'Average Change: ${analysis[2]:.2f}')
    print(f'Greatest Increase in Profits: {"N/A" if analysis[3] is None else f"{analysis[3][0]} (${analysis[3][1]})"}')
    print(f'Greatest Decrease in Profits: {"N/A" if analysis[4] is None else f"{analysis[4][0]} (${analysis[4][1]})"}')

def main():
    data_path = get_data_path()
    if data_path == '':
        report_no_data_file()
        exit(1)
    data = get_data(data_path)
    # If we have less than two data points we won't be able to calculate the PnL changes between months
    if len(data) < 2:
        report_no_data()
        exit(2)   
    analysis = analyze(data)
    # Output analysis to console
    output_analysis(analysis)
    # Output analysis to file
    output_file_path = os.path.join('..', 'Output')
    if not os.path.exists(output_file_path):
        os.mkdir(output_file_path)
    output_file_path = os.path.join(output_file_path, 'budget_data_financial_analysis.txt')
    with open(output_file_path, 'w+', encoding='UTF-8', newline='') as output_file:
        prev_stdout = sys.stdout
        sys.stdout = output_file
        output_analysis(analysis)
        sys.stdout = prev_stdout
    print_separator()
    print('Saved financial analysis to ' + output_file_path)
    print_separator()

if __name__ == '__main__':
    main()