from pro_filer.actions.main_actions import show_disk_usage


def test_show_disk_usage_file_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage_list(tmp_path, capsys):
    first_test_file = tmp_path / "test1.py"
    second__test_file = tmp_path / "test2.py"
    first_test_path = str(first_test_file)
    second_test_path = str(second__test_file)
    with open(first_test_path, "w") as test1:
        test1.write("this is the first file to test")
    with open(second_test_path, "w") as test2:
        test2.write("second test")

    context = {"all_files": [first_test_path, second_test_path]}

    first_line = f"'{first_test_path[:27]}...{first_test_path[-30:]}':".ljust(
        71
    )
    first_line2 = f"30 ({int(30 / 41 * 100)}%)"
    second_line = (
        f"'{second_test_path[:27]}...{second_test_path[-30:]}':".ljust(71)
    )
    second_line2 = f"11 ({int(11 / 41 * 100)}%)"
    first_result = f"{first_line}{first_line2}\n"
    second_result = f"{second_line}{second_line2}\n"
    result = first_result + second_result + "Total size: 41\n"

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == result
