from pro_filer.actions.main_actions import show_preview


def test_show_preview():
    test_cases = [
        {
            "name": "Test 1: consideram apenas all_files e all_dirs vazios",
            "context": {"all_files": [], "all_dirs": []},
        },
        {
            "name": "Test 2: Diretório com mais de 5 arquivos e diretórios",
            "context": {
                "all_files": [
                    "file1.txt",
                    "file2.txt",
                    "file3.txt",
                    "file4.txt",
                    "file5.txt",
                    "file6.txt",
                ],
                "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"],
            },
        },
        {
            "name": "Test 3: Diretório com arquivos e diretórios",
            "context": {
                "all_files": ["file1.txt", "file2.txt", "file3.txt"],
                "all_dirs": ["dir1", "dir2"],
            },
        },
    ]

    for test_case in test_cases:
        print(test_case["name"])
        show_preview(test_case["context"])
        print()


if __name__ == "__main__":
    test_show_preview()
