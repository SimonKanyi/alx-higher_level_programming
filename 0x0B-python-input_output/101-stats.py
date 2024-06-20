#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Print the computed metrics.
<<<<<<< HEAD

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
=======
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
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
