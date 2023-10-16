import argparse
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

    try:
        exclude_patterns: list[str] = load_exclude_patterns(
            args.exclude, str(Path(folder_path).joinpath(".scanignore").resolve()))
        scanned_files = scan_files(folder_path, exclude_patterns)
        write_to_file(scanned_files, output_file)
        print(
            'Scan complete. Results saved to {}'.format(output_file))
    except Exception as e:
        print('Error: {}'.format(str(e)))


if __name__ == "__main__":
    main()
