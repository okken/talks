def test_colors_get_printed(pytester):
    pytester.copy_example("examples/test_example.py")
    pytester.makepyfile(__init__ = "")
    result = pytester.runpytest("-s")
    result.assert_outcomes(passed=1)
    result.stdout.fnmatch_lines(
        [
            "*[31mtest_colors: this should be red*[0m",
            "*[32mtest_colors: this should be green*[0m",
            "*[33mtest_colors: this should be yellow*[0m",
            "*[34mtest_colors: this should be blue*[0m",
            "*[35mtest_colors: this should be magenta*[0m",
            "*[36mtest_colors: this should be cyan*[0m",
        ],
    )
