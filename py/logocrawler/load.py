import csv
import sys

def write_results(results):
    """
    Loads the results in CSV format for the end user

    Args:
        results (list): The list of results
    """
    stdout = csv.writer(sys.stdout, dialect='excel')
    for result in results:
        stdout.writerow(result)