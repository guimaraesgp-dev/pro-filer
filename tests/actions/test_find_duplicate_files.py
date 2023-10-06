from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_diferents(tmp_path):
    file1_test = tmp_path / "file1_test.py"
    file2_test = tmp_path / "file2_test.py"
    file1_test.write_text("Test 1")
    file2_test.write_text("Test 2")
    context = {"all_files": [str(file1_test), str(file2_test)]}
    result = find_duplicate_files(context)
    assert result == []


def test_find_duplicate_files_not_found_file(tmp_path):
    file1_test = tmp_path / "file1_test.py"
    file2_test = tmp_path / "file2_test.py"

    file1_test.write_text("Test 1")

    context = {"all_files": [str(file1_test), str(file2_test)]}

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)


def test_find_duplicate_files_empty():
    context = {"all_files": []}
    result = find_duplicate_files(context)
    assert result == []
