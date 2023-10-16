import os
from pathlib import Path
from typing import List, Tuple


def load_exclude_patterns(exclude_patterns: List[str], scan_ignore_path: str) -> List[str]:
    scan_ignore_file = Path(scan_ignore_path).resolve()
    if os.path.exists(scan_ignore_file):
        with open(scan_ignore_file, 'r') as f:
            exclude_patterns += f.read().splitlines()
    return exclude_patterns


def scan_files(folder_path: str, exclude_patterns: List[str]):
    scanned_files = []

    for file_path in Path(folder_path).rglob('*'):
        if file_path.is_file() and not any(file_path.match(pattern) for pattern in exclude_patterns):
            with file_path.open('r', errors='ignore') as f:
                content = f.read()

            scanned_files.append((str(file_path), content))
    return scanned_files


def write_to_file(scanned_files: List[Tuple[str, str]], output_file: str) -> None:
    with open(output_file, 'w') as f:
        for file, content in scanned_files:
            f.write(f"{file}:\n\"\"\"\n{content}\"\"\"\n\n")
