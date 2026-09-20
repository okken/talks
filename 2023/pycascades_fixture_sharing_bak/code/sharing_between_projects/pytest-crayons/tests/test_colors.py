def test_colors_get_printed(pytester):
    pytester.copy_example("examples/test_example.py")
    pytester.makepyfile(__init__ = "")
    result = pytester.runpytest("-s")
    result.stdout.fnmatch_lines(
        [
            "*[31mtest_colors: this should be in red*[0m",
            "*[32mtest_colors: this should be in green*[0m",
            "*[33mtest_colors: this should be in yellow*[0m",
            "*[34mtest_colors: this should be in blue*[0m",
            "*[35mtest_colors: this should be in magenta*[0m",
            "*[36mtest_colors: this should be in cyan*[0m",
        ],
    )
