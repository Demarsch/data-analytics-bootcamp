from collections import namedtuple
import csv
import os
import shared
import sys

DataPoint = namedtuple('DataPoint', 'month pnl')

FinancialAnalysis = namedtuple('FinancialAnalysis', 'month_count total_pnl average_pnl_change max_increase min_decrease')

_input_file_name = 'budget_data.csv'
_output_file_name = 'budget_data_financial_analysis.txt'

def report_no_input_file():    
    '''Print the information on data file that was not found and on all locations it has been looked for at.'''
    file_locations = shared.get_input_file_locations(_input_file_name)
    shared.print_separator()
    print('The input file was not found. Please place it at one of the following locations:')
    for location in file_locations:
        print(location)
    shared.print_separator()

def get_data(path: str) -> list:
    '''
    Open the CSV file at the specified path and convert its content into analyzable format.

    :param str path: A path to the data file
    :return: Data point collection
    :rtype: [DataPoint]
    '''
    with open(path, 'r', encoding='UTF-8',newline='') as input_file:
        csv_reader = csv.reader(input_file)
        # Skipping headers line
        next(csv_reader)
        return [DataPoint(line[0], int(line[1])) for line in csv_reader]

def report_no_data():
    '''Print the information on being unable to perform the analysis due to the lack of the data points.'''
    shared.print_separator()
    print('There is not enough data to perform financial analysis')
    shared.print_separator()

def analyze(data) -> FinancialAnalysis:
    '''
    Perform the analysis of the incoming month-pnl pairs and aggregates some statistics.

    :param [DataPoint] data: Data point collection
    :return: Statistics on months count, total PnL, average PnL change, greatest PnL increase (or None) and greatest PnL decrease (or None)
    :rtype: FinancialAnalysis
    '''
    month_count = len(data)
    total_pnl = data[0].pnl
    pnl_change_list = []
    # Though we could start calculations from 0 index, the below approach saves us extra check for the index on every iteration 
    # (we can't calculate the change for the very first data point)
    for i in range(1, month_count):
        total_pnl += data[i].pnl
        pnl_change_list.append(DataPoint(data[i].month, data[i].pnl - data[i - 1].pnl))
    # Simply walk through all data points to find max/min
    max_pnl_increase = pnl_change_list[0]
    min_pnl_decrease = pnl_change_list[0]
    for pnl_change in pnl_change_list:
        if pnl_change.pnl > max_pnl_increase.pnl:
            max_pnl_increase = pnl_change
        if pnl_change.pnl < min_pnl_decrease.pnl:
            min_pnl_decrease = pnl_change
    # The straightforward way of calculating the average change would be to sum all average changes and divide it by the number of these changes
    # But a little trick will allow us to reduce it to just one division:
    # The sum of changes would look like this: Diff(1,0) + Diff(2,1) + ... + Diff(n - 1, n - 2) where n - number of data points (DP).
    # And it expands into (DP1 - DP0) + (DP2 - DP1) + ... + (DPn-2 - DPn-3) + (DPn-1 - DPn-2) = DPn-1 - DP0
    # The number of changes equals to the number of data points minus one
    average_pnl_change = (data[-1].pnl - data[0].pnl) / (month_count - 1)
    # Also it may happen that all changes are non-negative (non-positive).
    # In these cases we won't be able to make a conclusion on greatest decrease (greatest increase respectively) 
    return FinancialAnalysis(
        month_count,
        total_pnl,
        average_pnl_change,
        None if max_pnl_increase.pnl <= 0 else max_pnl_increase,
        None if min_pnl_decrease.pnl >= 0 else min_pnl_decrease
    )

def output_analysis(analysis: FinancialAnalysis, file=sys.stdout):
    '''
    Print the contents of financial analysis.

    :param FinancialAnalysis analysis: financial analysis
    :param file file: file to output analysis to. Defaults to sys.stdout 
    '''
    shared.print_separator(file)
    print('Financial Analysis', file=file)
    shared.print_separator(file)
    print(f'Total Months: {analysis.month_count}', file=file)
    print(f'Total PnL: ${analysis.total_pnl}', file=file)
    print(f'Average Change: ${analysis.average_pnl_change:.2f}', file=file)
    print(f'Greatest Increase in Profits: {"N/A" if analysis.max_increase is None else f"{analysis.max_increase.month} (${analysis.max_increase.pnl})"}', file=file)
    print(f'Greatest Decrease in Profits: {"N/A" if analysis.min_decrease is None else f"{analysis.min_decrease.month} (${analysis.min_decrease.pnl})"}', file=file)

def main():
    input_file_path = shared.get_input_file_path(_input_file_name)
    if input_file_path == '':
        report_no_input_file()
        exit(1)
    data = get_data(input_file_path)
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
    output_file_path = os.path.join(output_file_path, _output_file_name)
    with open(output_file_path, 'w+', encoding='UTF-8', newline='') as output_file:
        output_analysis(analysis, output_file)
    shared.print_separator()
    print('Saved financial analysis to ' + output_file_path)
    shared.print_separator()

if __name__ == '__main__':
    main()