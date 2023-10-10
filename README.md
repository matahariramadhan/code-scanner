# Scan Code

A simple command-line tool to recursively scan files in a folder and create a text file containing their content. This tool provides flexibility in excluding specific files or patterns during scanning.

## Usage

```bash
python scan.py <folder_path> -o <output_file> [-e <exclude_pattern>]
```

- `<folder_path>`: Path to the folder to scan.
- `-o <output_file>`: Output text file name. (default: `output.txt`)
- `-e <exclude_pattern>`: Patterns to exclude files. You can provide multiple patterns separated by space.

## Excluding Files

Exclusion patterns can be specified in the following ways:

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
   You can also specify exclusion patterns directly via the `-e` or `--exclude` option when running the tool.

   Example:

   ```bash
   python scan.py <folder_path> -o <output_file> -e "*.log" "*.tmp"
   ```

   In this example, files with the extensions `.log` and `.tmp` will be excluded from the scan.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/matahariramadhan/scan-code.git
   cd scan-code
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   This will create a virtual environment named `venv` in your project directory.

3. Activate the virtual environment:

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS and Linux:**
     ```bash
     source venv/bin/activate
     ```

   Your command prompt should now show the virtual environment name, indicating it's active.

4. Install project dependencies inside the virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

While the virtual environment is active, you can run tests using `pytest`:

```bash
pytest tests/
```

## Running the Scan Tool

Ensure the virtual environment is active, then you can run the scan tool as described in the Usage section.

## Deactivating the Virtual Environment

When you're done working on your project, deactivate the virtual environment:

```bash
deactivate
```

This will return you to your global Python environment.

## Contributors

- [Matahari Ramadhan](https://github.com/matahariramadhan)

Feel free to contribute by opening issues or pull requests!

---
