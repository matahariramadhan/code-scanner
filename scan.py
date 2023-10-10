import os
import argparse

def get_scanignore_patterns():
    scanignore_patterns = []
    if os.path.exists(".scanignore"):
        with open(".scanignore", "r") as scanignore_file:
            scanignore_patterns = scanignore_file.read().splitlines()
    return scanignore_patterns

def scan_folder(path, exclude_patterns=None):
    text_data = ""

    try:
        for root, dirs, files in os.walk(path):
            for filename in files:
                file_path = os.path.join(root, filename)

                # Check if the file matches any exclusion patterns
                if exclude_patterns and any(pattern in file_path for pattern in exclude_patterns):
                    continue

                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    file_content = file.read()
                    text_data += f"{file_path}:\n{file_content}\n\n"

    except Exception as e:
        print(f"Error: {e}")
        text_data = None

    return text_data

def main():
    parser = argparse.ArgumentParser(description="Recursively scan files in a folder and create a text file.")
    parser.add_argument("folder_path", help="Path to the folder to scan")
    parser.add_argument("-o", "--output", default="output.txt", help="Output text file name")
    parser.add_argument("-e", "--exclude", nargs='*', help="Patterns to exclude files")

    args = parser.parse_args()

    folder_path = args.folder_path

    # Validate folder path
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        return

    # Get exclusion patterns from .scanignore or command line arguments
    exclude_patterns = get_scanignore_patterns() if not args.exclude else args.exclude

    text_data = scan_folder(folder_path, exclude_patterns)

    if text_data is not None:
        with open(args.output, 'w', encoding='utf-8') as output:
            output.write(text_data)

        print(f"Scanning complete. Results saved to {args.output}")
    else:
        print("Scanning failed.")

if __name__ == "__main__":
    main()
