from collections import namedtuple
from functools import reduce
import csv
import os
import shared
import sys

_input_file_name = 'election_data.csv'
_output_file_name = 'election_data_summary.txt'

CandidateStats = namedtuple('CandidateStats', 'name vote_count vote_percentage')
ElectionSummary = namedtuple('ElectionSummary', 'total_vote_count candidates winner_name')

def report_no_input_file():    
    '''Print the information on data file that was not found and on all locations it has been looked for at.'''
    file_locations = shared.get_input_file_locations(_input_file_name)
    shared.print_separator()
    print('The input file was not found. Please place it at one of the following locations:')
    for location in file_locations:
        print(location)
    shared.print_separator()

def get_data(path: str) -> dict:
    '''
    Open the CSV file at the specified path and convert its content into a dictionary of candidate-vote count.

    :param str path: A path to the data file
    :return: A dictionary of candidate names and their vote count
    :rtype: [dict]
    '''
    with open(path, 'r', encoding='UTF-8',newline='') as input_file:
        csv_reader = csv.reader(input_file)
        # Skipping headers line: Voter ID,County,Candidate
        next(csv_reader)
        result = {}
        for line in csv_reader:
            vote_count = result.setdefault(line[2], 0)
            result[line[2]] = vote_count + 1
        return result

def report_no_data():
    '''Print the information on being unable to calculate the election summary due to the lack of the data points.'''
    shared.print_separator()
    print('There is not enough data to calculate the election summary')
    shared.print_separator()

def generate_summary(data: dict) -> ElectionSummary:
    '''
    Generates the election summary given the total vote count for each candidate

    :param dict data: Dictionary for candidate-vote count
    :return: Election summary that contains total vote count, winner name and statistics for each candidate
    :rtype: ElectionSummary
    '''
    # Here we just use one-liner to calculate the sum of all values of dictionary (total vote count)
    total_vote_count = reduce((lambda x, y: x + y), data.values())
    # Here we sort candidates by the their vote count descending (winner is on top)
    sorted_candidates = [k for k in sorted(data, key=data.get, reverse=True)]
    candidate_stats = []
    for candidate in sorted_candidates:
        vote_count = data[candidate]
        candidate_stats.append(CandidateStats(candidate, vote_count, vote_count / total_vote_count))

    return ElectionSummary(total_vote_count, candidate_stats, candidate_stats[0].name)

def output_summary(election_summary: ElectionSummary, file=sys.stdout):
    '''
    Print the contents of the election summary to the specific file.

    :param ElectionSummary election_summary: Election summary
    :param file file: File to output analysis to. Defaults to sys.stdout 
    '''
    shared.print_separator(file)
    print('Election Results Analysis', file=file)
    shared.print_separator(file)
    print(f'Total Votes: {election_summary.total_vote_count}', file=file)
    shared.print_separator(file)
    for candidate in election_summary.candidates:
        print(f'{candidate.name}: {candidate.vote_percentage:.2%} ({candidate.vote_count})',file=file)
    shared.print_separator(file)
    print(f'Winner: {election_summary.winner_name}', file=file)
    shared.print_separator(file)

def main():
    input_file_path = shared.get_input_file_path(_input_file_name)
    if input_file_path == '':
        report_no_input_file()
        exit(1)
    data = get_data(input_file_path)
    # If we don't have any votes at all we won't be able to generate the summary
    if len(data) == 0:
        report_no_data()
        exit(2)   
    election_summary = generate_summary(data)
    # Output summary to the console
    output_summary(election_summary)
    # Output analysis to the file
    output_file_path = os.path.join('..', 'Output')
    if not os.path.exists(output_file_path):
        os.mkdir(output_file_path)
    output_file_path = os.path.join(output_file_path, _output_file_name)
    with open(output_file_path, 'w+', encoding='UTF-8', newline='') as output_file:
        output_summary(election_summary, output_file)
    print('Saved election summary to ' + output_file_path)
    shared.print_separator()

if __name__ == '__main__':
    main()