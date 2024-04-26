#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Print the computed metrics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parse a line and extract file size and status code.
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        status = int(parts[-2])
        return size, status
    except (ValueError, IndexError):
        return None, None

def compute_metrics():
    """
    Compute metrics from stdin.
    """
    line_count = 0
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            line_count += 1
            size, status = parse_line(line.strip())
            if size is not None and status is not None:
                total_size += size
                if status in status_codes:
                    status_codes[status] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    compute_metrics()
