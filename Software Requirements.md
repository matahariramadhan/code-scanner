# Code Scannern Software Requirements

## Overview

The Code Scanner is a software that can **scan** a folder and its subfolders for files and create a text file containing their content in the path specified by user. The user can specify patterns to **exclude** some files from being scanned and copied. The user can also put all the excluded patterns in a `.scanignore` file in the root folder of the scan. The software can **handle errors** gracefully and **log** them to a file. The software is written in **Python** programming language.

## Features

- **Scan and copy**: The software can scan a folder and its subfolders for files and create a text file containing their content in the path specified by user. The text file will have the name of the source file, followed by a colon, followed by a newline, followed by its content, followed by two newlines, for each file scanned. The text file will be saved in the same folder as the software or as specified by the user.
- **Exclude pattern**: The user can specify patterns to exclude some files from being scanned and copied. The patterns can be glob patterns. For example, the user can exclude all files with .py extension by passing `*.py` as an argument.
- **.scanignore file**: The user can also put all the excluded patterns in a .scanignore file in the root folder of the scan. The .scanignore file should have one pattern per line. The software will read the .scanignore file and ignore all files that match any of the patterns in it.
- **Error handling**: The software can handle errors gracefully and log them to a file. If there is any problem with scanning or copying a file, such as permission denied, file not found, or encoding error, the software will log an error message and continue with the next file. The software will also log an info message when the scan is complete and the results are saved.
- **Logging**: The Code Scanner application utilizes Python's logging module to capture important events and errors. The log messages are stored in a file named `scan.log` in the application directory. The logging configuration is set as follows:

  - **To `scan.log`:**

    - **ERROR:** Logs critical errors that prevent the application from functioning properly.
    - **CRITICAL:** Denotes a critical error that leads to an application crash or major malfunction.

  - **To Standard Output (stdout):**

    - **INFO:** Provides high-level confirmation of the application's normal operation, displayed in the console.

- **Validation**: The software performs validation to ensure that the input and output of the software are correct, consistent, and complete. The software validates the following aspects of the input and output:
  - **Input validation**: The software checks if the input arguments passed by the user are valid and meet the requirements of the software. The input arguments include the folder path to scan, the output file name, and the exclude patterns. The software validates the input arguments using the following criteria and rules:
    - The folder path must be a valid path that exists on the system and is a directory.
    - The output file name must be a valid file name that does not contain any illegal characters or reserved words.
    - The exclude patterns must be valid glob patterns that do not contain any syntax errors or invalid characters.

## Integration Test Cases

The tests check if the output text file created by the software is correct, consistent, and complete. The output text file contains the content of all the files scanned by the software. The tests validate the output text file using the following criteria and rules:

- The output text file must have the same name as specified by the user or the default name if not specified.
- The output text file must have the format of source file name, followed by a colon, followed by a newline, followed by its content, followed by two newlines, for each file scanned.
- The output text file must include all the files that are not excluded by the user or by the .scanignore file.
- The output text file must exclude all the files that match any of the exclude patterns specified by the user or by the .scanignore file.
- The output text file must not contain any errors or warnings from scanning or copying files.

## How to use

```bash
python scan.py <folder_path> -o <output_file> [-e <exclude_pattern>]
```

- `<folder_path>`: Path to the folder to scan.
- `-o <output_file>`: Output text file name. (default: `output.txt`)
- `-e <exclude_pattern>`: Patterns to exclude files. You can provide multiple patterns separated by space.

### Excluding Files

Exclude patterns can be specified in the following ways:

1. **Using `.scanignore` File:**
   Create a `.scanignore` file in your project directory and list the patterns you want to exclude, one per line.

   Example `.scanignore` content:

   ```
   .venv/
   .pytest_cache/
   output.txt
   __pycache__/
   .git/
   ```

   When the tool is run, it will automatically use these patterns for exclusion.

2. **Command Line Argument:**
   You can also specify exclude patterns directly via the `-e` or `--exclude` option when running the tool.

   Example:

   ```bash
   python scan.py <folder_path> -o <output_file> -e "*.log" "*.tmp"
   ```

   In this example, files with the extensions `.log` and `.tmp` will be excluded from the scan.

The software uses various methods to perform validation, such as using built-in functions, modules, and libraries from Python, using try-except blocks to handle exceptions, using logging module to log messages, and using unit testing module to test the functionality of the software.

## Design

Using object oriented, dependency inversion, interface or abstract class, modular, polymorphic principles, the Code Scanner is designed for flexibility and extensibility.

### Classes and Modules

1. **Scanner Class:**

   - Responsible for scanning files and generating the output text file.
   - Utilizes methods to handle exclusion patterns and error logging.
   - Uses file handling functions to read from `.scanignore` and write to the output text file.

2. **Logger Module:**

   - Manages logging functionalities, capturing errors and info messages.
   - Implements Python's logging module to ensure comprehensive logging.

3. **Validator Class:**
   - Performs input and output validation.
   - Utilizes various validation methods for folder paths, file names, and exclude patterns.

### Error Handling

- Uses try-except blocks to catch specific exceptions like `PermissionError`, `FileNotFoundError`, and `UnicodeDecodeError`.
- Logs detailed error messages with relevant context information.
- Ensures the software continues processing remaining files even after encountering errors.

### Unit Testing

- Employs `pytest` module for comprehensive testing.
- Covers different scenarios including valid inputs, exclusion pattern handling, error scenarios, and edge cases.
- Ensures robustness and reliability of the Code Scanner application.
