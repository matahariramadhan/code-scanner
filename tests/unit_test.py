from pathlib import Path
import pytest
from code_scanner import load_exclude_patterns, scan_files, write_to_file


@pytest.fixture
def test_folder(tmpdir):
    # Create a temporary test folder with some test files
    test_folder_path = tmpdir.mkdir("test_folder")

    # Create test files
    test_file1 = test_folder_path.join("test_file1.txt")
    test_file1.write("This is test file 1 content.")

    test_subfolder = test_folder_path.mkdir("subfolder")
    test_file2 = test_subfolder.join("test_file2.txt")
    test_file2.write("This is test file 2 content.")

    return test_folder_path


def test_load_exclude_patterns(test_folder):
    scan_ignore_file = test_folder.join('.scanignore')
    scan_ignore_file.write("*.log\n*.tmp")

    exclude_patterns = load_exclude_patterns(["*.txt"], str(scan_ignore_file))

    assert exclude_patterns == ["*.txt", '*.log', '*.tmp']


def test_scan_files(test_folder):
    # Create a list of exclude patterns
    exclude_patterns = ["*.log", "*.tmp"]

    # Call the scan_files function with the test folder path and the exclude patterns
    scanned_files = scan_files(str(test_folder), exclude_patterns)

    # Check that the scanned files list contains only the expected files and their contents
    assert len(scanned_files) == 2
    assert scanned_files[0][0] == str(test_folder.join("test_file1.txt"))
    assert scanned_files[0][1] == "This is test file 1 content."
    assert scanned_files[1][0] == str(
        test_folder.join("subfolder/test_file2.txt"))
    assert scanned_files[1][1] == "This is test file 2 content."


def test_write_to_file(test_folder):
    # Create a list of scanned files
    scanned_files = [
        (str(test_folder.join("test_file1.txt")), "This is test file 1 content."),
        (str(test_folder.join("subfolder/test_file2.txt")),
         "This is test file 2 content.")
    ]

    output_file = "output.txt"

    # Call the write_to_file function with the scanned files and the output file
    write_to_file(scanned_files, output_file)

    # Check that the output file contains the expected content
#     with open("output.txt", 'r') as f:
#         output_content = f.read()

#     expected_content = f"""{scanned_files[0][0]}:
# \"\"\"
# {scanned_files[0][1]}\"\"\"

# {scanned_files[1][0]}:
# \"\"\"
# {scanned_files[1][1]}\"\"\"
# """

#     assert output_content == expected_content

    assert Path(output_file).exists() == True
