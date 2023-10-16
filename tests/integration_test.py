import os
import subprocess
import pytest

# Define the path to the CLI tool script
CLI_TOOL_SCRIPT = "main.py"

file1_content = "This is test file 1 content."
file2_content = "This is test file 2 content."


@pytest.fixture
def test_folder(tmpdir):
    # Create a temporary test folder with some test files
    test_folder_path = tmpdir.mkdir("test_folder")

    # Create test files
    test_file1 = test_folder_path.join("test_file1.txt")
    test_file1.write(file1_content)

    test_subfolder = test_folder_path.mkdir("subfolder")
    test_file2 = test_subfolder.join("test_file2.txt")
    test_file2.write(file2_content)

    return test_folder_path


def test_scan_folder_without_exclude(test_folder):
    # Run the CLI tool without excluding any files
    output_file = test_folder.join("output.txt")
    cmd = f"python {CLI_TOOL_SCRIPT} {test_folder} -o {output_file}"

    # Execute the command
    subprocess.check_call(cmd, shell=True)

    # Check if the output file was created
    assert output_file.exists()

    # Check the content of the output file
    with open(test_folder.join("output.txt"), 'r') as file:
        content = file.read()

    # Ensure that content of both files is present
    assert file1_content in content
    assert file2_content in content


def test_scan_folder_with_exclude_in_root_folder(test_folder):
    # Run the CLI tool excluding files with specific extensions
    output_file = test_folder.join("output.txt")

    md_file = test_folder.join("README.md")
    md_content = "This is a README file."
    with open(md_file, 'w') as file:
        file.write(md_content)

    cmd = f"python {CLI_TOOL_SCRIPT} {test_folder} -o {output_file} -e *.md"

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
    assert md_content not in content


def test_scan_folder_with_exclude_in_sub_folder(test_folder):
    # Run the CLI tool excluding files with specific extensions
    output_file = test_folder.join("output.txt")

    subfolder_test = test_folder.mkdir('subfolder_test')
    md_file = subfolder_test.join("README.md")
    md_content = "This is a README file from subfolder test."
    with open(md_file, 'w') as file:
        file.write(md_content)

    cmd = f"python {CLI_TOOL_SCRIPT} {test_folder} -o {output_file} -e *.md"

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
    assert md_content not in content
