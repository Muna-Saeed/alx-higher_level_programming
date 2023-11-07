#!/usr/bin/python3
import sys
"""Reads from standard input and computes metrics."""


def print_stats(total_size, status_counts):
    """
    Prints the statistics.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print("{}: {}".format(status_code, count))

def parse_log_line(line):
    """
    Parses a log line and extracts the file size and status code.
    """
    parts = line.split()
    file_size = int(parts[-1])
    status_code = parts[-2]
    return file_size, status_code

total_size = 0
status_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        file_size, status_code = parse_log_line(line)
        total_size += file_size

        if status_code not in status_counts:
            status_counts[status_code] = 0
        status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
