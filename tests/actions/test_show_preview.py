from pro_filer.actions.main_actions import show_preview


def test_show_preview_1(capsys):
    context = {"all_files": [], "all_dirs": []}

    show_preview(context=context)
    captured = capsys.readouterr()

    assert captured.out == "Found 0 files and 0 directories\n"


def test_show_preview_2(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/utils/file1.py",
            "src/utils/file2.py",
            "src/utils/file3.py",
            "src/utils/file4.py",
            "src/utils/file5.py",
            "src/utils/file6.py",
            "src/utils/file7.py",
        ],
        "all_dirs": [
            "src",
            "src/utils",
            "src/utils/dir1",
            "src/utils/dir2",
            "src/utils/dir3",
            "src/utils/dir4",
            "src/utils/dir5",
            "src/utils/dir6",
            "src/utils/dir7",
        ],
    }

    show_preview(context=context)
    captured = capsys.readouterr()

    assert captured.out == (
        "Found 10 files and 9 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py', 'src/utils/file1.py', "
        "'src/utils/file2.py']\n"
        "First 5 directories: ['src', 'src/utils', "
        "'src/utils/dir1', 'src/utils/dir2', 'src/utils/dir3']\n"
    )


def test_show_preview_3(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }

    show_preview(context=context)
    captured = capsys.readouterr()

    assert captured.out == (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )
