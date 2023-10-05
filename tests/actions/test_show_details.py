from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_show_details_file_not_found(capsys):
    context = {"base_path": "/home/trybe/????"}
    show_details(context)
    cap = capsys.readouterr()
    assert cap.out == "File '????' does not exist\n"


def test_show_details_result(tmp_path, capsys):
    tmp_file = tmp_path / "test_file.py"
    tmp_file.touch()
    context = {"base_path": str(tmp_file)}

    expected_result = (
        f"File name: {tmp_file.name}\n"
        f"File size in bytes: {tmp_file.stat().st_size}\n"
        f"File type: {'file' if tmp_file.is_file() else 'directory'}\n"
        f"File extension: {tmp_file.suffix}\n"
        f"Last modified date: {date.today()}\n"
    )

    show_details(context)
    captured = capsys.readouterr()

    assert captured.out == expected_result


def test_show_details_no_extension(tmp_path, capsys):
    tmp_file = tmp_path / "test_file"
    tmp_file.touch()
    context = {"base_path": str(tmp_file)}

    file_name = f"File name: {tmp_file.name}\n"
    file_size = f"File size in bytes: {tmp_file.stat().st_size}\n"
    file_type = f"File type: {'file' if tmp_file.is_file() else 'directory'}\n"
    file_extension = "File extension: [no extension]\n"
    file_date = f"Last modified date: {date.today()}\n"

    expected_result = (
        file_name + file_size + file_type + file_extension + file_date
    )

    show_details(context)
    captured = capsys.readouterr()

    assert captured.out == expected_result
