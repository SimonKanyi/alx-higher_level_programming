#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Print the computed metrics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing status code counts.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))

def parse_line(line, status_codes):
    """
    Parse a line of input and update metrics.

    Args:
        line (str): Line of input in the specified format.
        status_codes (dict): Dictionary containing status code counts.

    Returns:
        int: File size of the current line.
    """
    parts = line.strip().split(" ")
    status_code = parts[-2]
    file_size = int(parts[-1])
    status_codes[status_code] = status_codes.get(status_code, 0) + 1
    return file_size

def main():
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                file_size = parse_line(line, status_codes)
                total_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print_metrics(total_size, status_codes)
            except Exception as e:
                continue
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
