# pytest-crayons

A pytest plugin for colorful print statements.

## Installation

```
pip install pytest-crayons
```

## Usage

Include a color fixture in the param list of a test. 
Then use it instead of `print`.

```python
def test_something(blue):
    ... # some code
    blue("a print statement, that shows up blue")
    ... # more test code
```

## Available colors

* red
* green
* yellow
* blue
* magenta
* cyan

Example with all colors: 

```python
def test_colors(red, green, yellow, blue, magenta, cyan):
    print("") # for the newline
    red("this should be red")
    green("this should be green")
    yellow("this should be yellow")
    blue("this should be blue")
    magenta("this should be magenta")
    cyan("this should be cyan")
```

<!-->
Shows up like this:

TODO: fill in this with a screen shot
-->