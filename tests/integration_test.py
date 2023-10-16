import os
import subprocess
import pytest

# Define the path to the CLI tool script
CLI_TOOL_SCRIPT = "main.py"


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

    return str(test_folder_path)


def test_scan_folder_without_exclude(test_folder, tmpdir):
    # Run the CLI tool without excluding any files
    output_file = tmpdir.join("output.txt")
    cmd = f"python {CLI_TOOL_SCRIPT} {test_folder} -o {output_file}"

    # Execute the command
    subprocess.check_call(cmd, shell=True)

    # Check if the output file was created
    assert output_file.exists()

    # Check the content of the output file
    with open(output_file, 'r') as file:
        content = file.read()

    # Ensure that content of both files is present
    assert "This is test file 1 content." in content
    assert "This is test file 2 content." in content
    # Ensure excluded file is not present
    assert "This is test file 3 content." not in content

    # Additional Assertions
    # Ensure correct number of entries in the output
    assert len(content.strip().split('\n\n')) == 2


def test_scan_folder_with_exclude(test_folder, tmpdir):
    # Run the CLI tool excluding files with specific extensions
    output_file = tmpdir.join("output.txt")
    cmd = f"python {CLI_TOOL_SCRIPT} {test_folder} -o {output_file} -e *.txt"

    # Execute the command
    subprocess.check_call(cmd, shell=True)

    # Check if the output file was created
    assert output_file.exists()

    # Check the content of the output file
    with open(output_file, 'r') as file:
        content = file.read()

    # Ensure that only the file content from .txt files is present
    assert "This is test file 1 content." in content
    assert "This is test file 2 content." in content
    # Ensure excluded file is not present
    assert "This is test file 3 content." not in content

    # Additional Assertions
    # Ensure correct number of entries in the output
    assert len(content.strip().split('\n\n')) == 2
