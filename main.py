import argparse
import logging
from pathlib import Path
from code_scanner import load_exclude_patterns, scan_files, write_to_file


def main():
    parser = argparse.ArgumentParser(description="Code Scanner CLI")
    parser.add_argument("folder_path", help="Path to the folder to scan.")
    parser.add_argument("-o", "--output", default="output.txt",
                        help="Output text file name. (default: output.txt)")
    parser.add_argument("-e", "--exclude", nargs="*",
                        default=[], help="Patterns to exclude files.")
    args = parser.parse_args()

    folder_path: str = args.folder_path
    output_file: str = args.output

    logging.basicConfig(filename="scan.log", level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        exclude_patterns: list[str] = load_exclude_patterns(
            args.exclude, str(Path(folder_path).joinpath(".scanignore").resolve()))
        scanned_files = scan_files(folder_path, exclude_patterns)
        write_to_file(scanned_files, output_file)
        logging.info(
            'Scan complete. Results saved to {}'.format(output_file))
    except Exception as e:
        logging.error('Error: {}'.format(str(e)))


if __name__ == "__main__":
    main()
