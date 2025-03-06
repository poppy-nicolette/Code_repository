
"""
For help run this in terminal: python script.py --help

Usage: combine_csv.py input_path output_file [--encoding=<utf-8>] [--delimiter=<,>]

Arguments:
  input_path  Path to the directory containing CSV files
  output_file Name of the output file

Options:
  --encoding=<utf-8>  File encoding [default: utf-8]
  --delimiter=<,>     CSV delimiter [default: ,]
"""

import csv
import glob
import os
import argparse


def combine_csv_files(input_path, output_file, encoding='utf-8', delimiter=','):
    try:
        # Get all CSV files in the directory
        csv_files = glob.glob(os.path.join(input_path, "*.csv"))

        if not csv_files:
            raise ValueError("No CSV files found in the specified directory")

        # Write to the output file
        with open(output_file, 'w', newline='', encoding=encoding) as outfile:
            writer = csv.writer(outfile, delimiter=delimiter)

            # Process first file
            print(f"Processing {csv_files[0]}")
            with open(csv_files[0], 'r', encoding=encoding) as firstfile:
                reader = csv.reader(firstfile, delimiter=delimiter)
                headers = next(reader)
                writer.writerow(headers)
                for row in reader:
                    writer.writerow(row)

            # Process remaining files
            for file in csv_files[1:]:
                print(f"Processing {file}")
                with open(file, 'r', encoding=encoding) as infile:
                    reader = csv.reader(infile, delimiter=delimiter)
                    next(reader)  # Skip header
                    for row in reader:
                        writer.writerow(row)

        print(f"Successfully combined {len(csv_files)} files into {output_file}")

    except Exception as e:
        print(f"Oops, an error occurred: {str(e)}")
        raise




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine multiple CSV files into a single file")
    parser.add_argument("input_path", help="Path to the directory containing CSV files")
    parser.add_argument("output_file", help="Name of the output file")
    parser.add_argument("--encoding", help="File encoding (default: utf-8)", default='utf-8')
    parser.add_argument("--delimiter", help="CSV delimiter (default: ,)", default=',')
    args = parser.parse_args()

    combine_csv_files(
        args.input_path,
        args.output_file,
        encoding=args.encoding,
        delimiter=args.delimiter
    )
