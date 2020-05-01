class: center, middle

# Multiply your Testing Effectiveness with Parametrized Testing

Brian Okken

<a href="https://twitter.com/brianokken"> <img src="images/twitter-logo.png" width="20"> @brianokken</a>

Code and slides 

[github.com/okken/talks](https://github.com/okken/talks/tree/master/2020/pycon_2020)

???

Thank you pushing play on this video. 
And at the very least startign to listen to my talk about parametrization.

Parametrized testing is one of the superpowers of pytest.  
And it's really one that I think can you save you tons of time.

---
layout: true

<div class="footer"><img src="images/twitter-logo.png" width="20"> @brianokken</div>

---

# Brian Okken

.left-column[
Work

<img src="images/r_s_logo.png" width="300">

Podcasts

<a href="https://testandcode.com">
<img src="images/testandcode.jpg" width="140"></a>
<a href="https://pythonbytes.fm">
<img src="images/pb.png" width="190"></a>
]
.right-column[
Book
 
<a href="https://t.co/AKfVKcdDoy?amp=1">
<img src="images/book.jpg" style="border-style: solid;color:black;" width="300">
</a>
]

???
I am Brian Okken. 

I wrote "Python Testing with pytest" because pytest is a really powerful test framework 
and I wanted other people to be able to start using it right away.

I host a couple podcasts:

* Test & Code, was created because software engineers don't talk about testing enough.
* Python Bytes, is co-hosted by Michael Kennedy. We sometimes tell bad jokes at the end. Occasionally good jokes.


During the day, I'm a mild mannered team lead at at Rohde & Schwarz,  
where help build communication test equipment by writing  
a lot of C++ code   
a lot of Python code   
and generally trying to avoid meetings as best I can.


---

# Value of Tests

A passing test suite

* Gives you confidence in what you are building
    * I didn't break anything that used to work
    * Future changes won’t break current features
* Allows you to have pride in your work
    * I can refactor until I'm proud of the code
* Lets you play with the code and change it with less fear
* Helps build team trust
    * Code reviews can focus on team understanding and ownership

Only works if:

* New features are tested with new tests
* Everyone can read the tests
* **Tests are easy and fast to write**  <- *this is what we're focusing on*

???

* Automated tests are valuable because a passing test suite
    * gives you confidence in what you are building
    * allows you to have pride in your work
    * lets you play with the code 
    * and change it with less fear
    * and helps build team trust

* It's a bonus if the test cases are 
    * quick to write
    * easy to maintain

That's the part we are focusing on today

---

# Takeaways

* Why parametrization is useful

* Your choices 
    * function
    * fixture
    * `pytest_generate_tests`
    
* How to 
    * run subsets of test cases
    * use `pytest.param` for ids and markers
    * use `indirect` to intercept parameters with fixtures

???
* We're going to see the code for 3 ways to parametrize tests.
    * fixture 
    * function 
    * and pytest_generate_tests
   
* I'll show you how to run a subset of the parametrizations

* And lastly, I'll introduce you to 
    * pytest.param
    * and indirect 
    
* Mostly just so that you've seen pytest.param and indirect once, and know  
  to look them up when you need them.

---

# Parametrize vs Parameterize

**parameter** + **ize**

* paramet_erize_ (US)
* paramet_rize_ (UK)

`pytest` uses `parametrize`, the UK spelling.

???

Before we go further. 

parametrize 

* There is no "e" between t and r
* Both spellings are allowed in English
* But only one is allowed in pytest, and it's the UK spelling
    * I submitted a ticket to allow both
    * It was rejected
    * I've gotten over it. 
    
---

# Something to Test

`triangles.py`:
```python
def triangle_type(a, b, c):
    """
    Given three angles,
    return 'right', 'obtuse', 'acute', or 'invalid'.
    """
    angles = (a, b, c)
    if 90 in angles:
        return "right"
    if any([a > 90 for a in angles]):
        return "obtuse"
    if all([a < 90 for a in angles]):
        return "acute"
    if sum(angles) != 180:
        return "invalid"
```
Right ![](images/right_triangle.png),
Acute ![](images/acute_triangle.png),
Obtuse ![](images/obtuse_triangle.png),

???
* I'm going to write some test code to test `triangle_type`.
  
* Given 3 angles
    * Return 
        * Right if there's a 90 degree angle
        * Obtuse if one angle is > 90
        * And acute if all angles are < 90
        
* If you remembered what obtuse and acute triangles were, you rock. 
* I had to look it up.

* There is at least one bug in the code,   
  on purpose, so we can see some test failures

---
# pytest.ini

I wanted all the examples to include:
* `--tb=no` for "no tracebacks" to hide tracebacks
* `-v` for verbose to show the test names

So those are in a `pytest.ini` file:
```
[pytest]
addopts = --tb=no -v
markers =
    smoke : smoke tests
```

We're going to use the "smoke" marker later, so it's registered here also.

???

If you are following along at home, I've done a little prep work.

For all examples

* I want -v for verbose, to see the test names
* tb=no, to hide the tracebacks
* Putting them in a pytest.ini lets me get a way with not typing them all the time.

---

# without Parametrization

```python
def test_right():
    assert triangle_type(90, 60, 30) == "right"

def test_obtuse():
    assert triangle_type(100, 40, 40) == "obtuse"

def test_acute():
    assert triangle_type(60, 60, 60) == "acute"

def test_invalid():
    assert triangle_type(0, 0, 0) == "invalid"
```
```
$ pytest test_1.py
=================== test session starts ===================

test_1.py::test_right PASSED                        [ 25%]
test_1.py::test_obtuse PASSED                       [ 50%]
test_1.py::test_acute PASSED                        [ 75%]
test_1.py::test_invalid FAILED                      [100%]

=============== 1 failed, 3 passed in 0.03s ===============
```

???

Here's a reasonable first attempt at some test code for triangle_type.

* 4 outcomes
* 4 test cases 

We probably should have more.

Nonetheless, this is a reasonable first set.

The tests are simple. just 1 line

When tests get more complex, the redundancy will get more painful.

But even with these simple tests, we can do better.

---

# Moving to one test (don't do this)
```python
def test_type():
    many_triangles = [
        (90, 60, 30, "right"),
        (100, 40, 40, "obtuse"),
        (60, 60, 60, "acute"),
        (0, 0, 0, "invalid"),
    ]
    for a, b, c, expected in many_triangles:
        assert triangle_type(a, b, c) == expected
```

```shell
$ pytest test_2.py
=================== test session starts ===================

test_2.py::test_type FAILED                         [100%]

==================== 1 failed in 0.03s ====================
```

???
What if we move all the test cases into a list and just loop  
through them in the test?

It's easier to extend now.  
And when everything passes, it seems fine. 

But don't do this.

* There really are 4 test cases, 
* but pytest only shows 1.
* any failure fails everything 
* and we can't tell test case failed without seeing the traceback

So how do we fix this?

---

# Function Parametrization
```python
*@pytest.mark.parametrize( 'a, b, c, expected', [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid")])
*def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
???
Function Parametrization, of course

This is the basic syntax 

Let's run it and see what it looks like.

---

# Function Parametrization
```python
@pytest.mark.parametrize( 'a, b, c, expected', [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid")])
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
```shell 
$ pytest test_3.py
=================== test session starts ===================

test_3.py::test_func[90-60-30-right] PASSED         [ 25%]
test_3.py::test_func[100-40-40-obtuse] PASSED       [ 50%]
test_3.py::test_func[60-60-60-acute] PASSED         [ 75%]
test_3.py::test_func[0-0-0-invalid] FAILED          [100%]

=============== 1 failed, 3 passed in 0.03s ===============
```
???
* Pretty good
* the test name, from test_ through the brackets is called a node id

So far, we've puth the test cases right in the parametrize decorator.  
But as we add more test cases, this can get harder to read.

---
# Parameters from a named list

```python
*many_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid")
]

*@pytest.mark.parametrize( 'a, b, c, expected', many_triangles)
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
???
So instead, we can 

* move the parameters to a named list
* and just pass in the list in the parametrize decorator


---
# Parameters from a function

```python
*def many_triangles():
    return [ (90, 60, 30, "right"),
             (100, 40, 40, "obtuse"),
             (60, 60, 60, "acute"),
             (0, 0, 0, "invalid") ]

*@pytest.mark.parametrize( 'a, b, c, expected', many_triangles())
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
???
Or instead of a fixed list, we can have a function return the set of test cases.

---
# Parameters from a generator

```python
*def many_triangles():
    for t in [ (90, 60, 30, "right"),
               (100, 40, 40, "obtuse"),
               (60, 60, 60, "acute"),
               (0, 0, 0, "invalid")]:
*        yield t

*@pytest.mark.parametrize( 'a, b, c, expected', many_triangles())
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
???
It can also be a generator.

---
# Parameters from a file
triangle_data.csv
```csv
90,60,30,right
100,40,40,obtuse
60,60,60,acute
0,0,0,invalid
```
```python
import csv

def many_triangles():
    with open('triangle_data.csv') as csvfile:
        for a, b, c, expected in csv.reader(csvfile):
            yield (int(a), int(b), int(c), expected)

@pytest.mark.parametrize( 'a, b, c, expected', many_triangles)
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
???
Or we can read parameters from a file.

Once you are using a function to generate parameters,   
you really have a lot of control.

Keep in mind that the entire file will be read at collection time,  
not at test run time.  

Still, it's a pretty powerful technique.

---
# Back to a List
```python
many_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid")
]

@pytest.mark.parametrize('a, b, c, expected', many_triangles)
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected

```
```
$ pytest test_7.py 
=================== test session starts ===================

test_7.py::test_func[90-60-30-right] PASSED         [ 25%]
test_7.py::test_func[100-40-40-obtuse] PASSED       [ 50%]
test_7.py::test_func[60-60-60-acute] PASSED         [ 75%]
test_7.py::test_func[0-0-0-invalid] FAILED          [100%]

=============== 1 failed, 3 passed in 0.03s ===============

```
???
* But let's go back to the list for now.
* and look at some tricks with running parametrized tests.


* We have a failure here.

---
# Run the last failing test case
```
*$ pytest --tb=short --lf test_7.py 
=================== test session starts ===================
collected 4 items / 3 deselected / 1 selected             
run-last-failure: rerun previous 1 failure

test_7.py::test_func[0-0-0-invalid] FAILED          [100%]

======================== FAILURES =========================
________________ test_func[0-0-0-invalid] _________________
test_7.py:14: in test_func
    assert triangle_type(a, b, c) == expected
E   AssertionError: assert 'acute' == 'invalid'
E     - acute
E     + invalid
============= 1 failed, 3 deselected in 0.03s =============
```
???
* We can use --lf to show the last failure
* and tb=short to turn on tracebacks

---
# Run test cases with 60 degree angles 
```
*$ pytest -k 60 test_7.py 
=================== test session starts ===================

test_7.py::test_func[90-60-30-right] PASSED         [ 50%]
test_7.py::test_func[60-60-60-acute] PASSED         [100%]

============= 2 passed, 2 deselected in 0.01s =============
```
???
We can run all test cases with 60 degree angles by using -k. 

---
# Run an individual test case 
```
*$ pytest test_7.py::test_func[0-0-0-invalid]
=================== test session starts ===================

test_7.py::test_func[0-0-0-invalid] FAILED          [100%]

==================== 1 failed in 0.03s ====================
```
???
We can even run a specific test case by specifying the full node id


---
# Fixture Parametrization

Function: `test_7.py`
```python
@pytest.mark.parametrize('a, b, c, expected', many_triangles)
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected

```

Fixture: `test_8.py` 
```python
*@pytest.fixture(params=many_triangles)
*def a_triangle(request):
*    return request.param

*def test_fix(a_triangle):
*    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected
```

???
Now let's move to the next parametrization technique, fixture parametrization.

* I'm showing function parametrization on the top
* and fixture parametrization on the bottom

* The basic syntax is easy enough

* The parameters are passed to the fixture decorator
* request.param will be filled with each tuple from many_triangles 
* Since the `a_triangle` fixture returns request.param
* the test will receive each parameter set one at a time

---
# Object parameters get non-helpful names
```python
many_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid")]

@pytest.fixture(params=many_triangles)
def a_triangle(request):
    return request.param

def test_fix(a_triangle):
    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected
```
```
$ pytest test_8.py 
=================== test session starts ===================
*test_8.py::test_fix[a_triangle0] PASSED             [ 25%]
*test_8.py::test_fix[a_triangle1] PASSED             [ 50%]
*test_8.py::test_fix[a_triangle2] PASSED             [ 75%]
*test_8.py::test_fix[a_triangle3] FAILED             [100%]
=============== 1 failed, 3 passed in 0.03s ===============

```
???
* We have an issue here with the names
* If we parametrize with objects, like tuples here, 
    * pytest doesn't try to come up with a good name 
    * it just names the parameters with a counter

* there are a few ways to fix it.


---
# An ids list
```python
many_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid") ]

@pytest.fixture(params=many_triangles,
*                ids=['right', 'obtuse', 'acute', 'invalid'])
def a_triangle(request):
    return request.param

def test_fix(a_triangle):
    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected
```
```
$ pytest test_9.py 
=================== test session starts ===================
*test_9.py::test_fix[right] PASSED                   [ 25%]
*test_9.py::test_fix[obtuse] PASSED                  [ 50%]
*test_9.py::test_fix[acute] PASSED                   [ 75%]
*test_9.py::test_fix[invalid] FAILED                 [100%]
=============== 1 failed, 3 passed in 0.03s ===============
```
???
One way to have better names is to pass in a list of identifiers   
with the `ids` argument.



---
# An ids function
```python
many_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid") ]

@pytest.fixture(params=many_triangles, 
*                ids=str)  # or repr, or lambda t:t[3]
def a_triangle(request):
    return request.param

def test_fix(a_triangle):
    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected

```
```
$ pytest test_10.py 
=================== test session starts ===================
*test_10.py::test_fix[(90, 60, 30, 'right')] PASSED  [ 25%]
*test_10.py::test_fix[(100, 40, 40, 'obtuse')] PASSED [ 50%]
*test_10.py::test_fix[(60, 60, 60, 'acute')] PASSED  [ 75%]
*test_10.py::test_fix[(0, 0, 0, 'invalid')] FAILED   [100%]
=============== 1 failed, 3 passed in 0.03s ===============

```
???
Or you can pass in an ids function

* It needs to return a string
* often, str, or repr, or a simple lambda does the trick


---
# Custom ids function
```python
*def idfn(a_triangle):
*    a, b, c, expected = a_triangle
*    return f'{a}-{b}-{c}-{expected}'

*@pytest.fixture(params=many_triangles, ids=idfn)
def a_triangle(request):
    return request.param

def test_fix(a_triangle):
    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected
```

```
$ pytest test_11.py 
=================== test session starts ===================
*test_11.py::test_fix[90-60-30-right] PASSED         [ 25%]
*test_11.py::test_fix[100-40-40-obtuse] PASSED       [ 50%]
*test_11.py::test_fix[60-60-60-acute] PASSED         [ 75%]
*test_11.py::test_fix[0-0-0-invalid] FAILED          [100%]
=============== 1 failed, 3 passed in 0.03s ===============
```
???
You can also write a custom function

---
# pytest_generate_tests()
```python
*def pytest_generate_tests(metafunc):
*    if "gen_triangle" in metafunc.fixturenames:
*        metafunc.parametrize("gen_triangle",
*                             many_triangles,
*                             ids=idfn)

def test_gen(gen_triangle):
    a, b, c, expected = gen_triangle
    assert triangle_type(a, b, c) == expected
```

```
$ pytest test_12.py 
=================== test session starts ===================

test_12.py::test_gen[90-60-30-right] PASSED         [ 25%]
test_12.py::test_gen[100-40-40-obtuse] PASSED       [ 50%]
test_12.py::test_gen[60-60-60-acute] PASSED         [ 75%]
test_12.py::test_gen[0-0-0-invalid] FAILED          [100%]

=============== 1 failed, 3 passed in 0.03s ===============
```
???
Now it's time for the third parametrization technique.

The third technique is to use the hook function `pytest_generate_tests`.

This is especially useful   
if we want to use information in `metafunc`  
when coming up with the parameter list.
    
---
# metafunc

From [docs.pytest.org/en/latest/reference.html#metafunc](https://docs.pytest.org/en/latest/reference.html#metafunc)

* Metafunc objects are passed to the pytest_generate_tests hook.  
* They help to inspect a test function and to generate tests according to 
    * test configuration 
    * or values specified in the class or module where a test function is defined.
???
I suggest looking up in the pytest docs all the stuff you can grab out of metafunc. 

One thing metafunc has is access to command line flag info. 

So you could use this to generate the test case list based on command line flags.

But there's other config info in there.


---
# test.param
```python
smoke = pytest.mark.smoke

many_triangles = [
*    pytest.param(90, 60, 30, "right", marks=smoke),
*    pytest.param(100, 40, 40, "obtuse", marks=smoke),
    (90, 60, 30, "right"),
*    pytest.param(0, 0, 0, "invalid", id='zeros'),
]
```
```
*$ pytest -m smoke test_13.py 
=================== test session starts ===================
test_13.py::test_func[90-60-30-right] PASSED        [ 50%]
test_13.py::test_func[100-40-40-obtuse] PASSED      [100%]
============= 2 passed, 4 deselected in 0.01s =============
```
```
*$ pytest -k zeros test_13.py 
=================== test session starts ===================
test_13.py::test_func[zeros] PASSED                 [100%]
============= 1 passed, 3 deselected in 0.01s =============
```
???
Now I'm going to switch gears a bit and talk about `test.param` and `indirect`.

You can use pytest.param
* to add markers to individual test cases
* or change the identifier

I usually use pytest.param for the marker feature. 

---
# indirect parameter
```python
@pytest.fixture()
*def expected(request):
    if request.param == 'obtuse':
        print('\nthis is one of the obtuse cases')
    return request.param


@pytest.mark.parametrize('a, b, c, expected', many_triangles,
*                         indirect=['expected'])
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```

The parameter value goes through a fixture before making
it to the test, an "indirect" route.

???

`indirect` is definitely a weird feature. But also kinda cool. 

You can set `indirect` to a list of parameter names.  
Those parameters will have their value passed through a fixture of the same name before getting to the test. 

You can also set it to `True` if you want this to happen with all the parameters.

---
# indirect example
```python
def many_triangles():
    with open('triangle_data.csv') as csvfile:
        for a, b, c, expected in csv.reader(csvfile):
            yield (a, b, c, expected)

@pytest.fixture()
def a(request):
    return int(request.param)

@pytest.fixture()
def b(request):
    return int(request.param)

@pytest.fixture()
def c(request):
    return int(request.param)

@pytest.mark.parametrize('a, b, c, expected', many_triangles(), 
                         indirect=['a', 'b', 'c'])
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
???
As an example, when we were pulling data from a csv file.  
We could have used indirect for the integer conversion.  

In this case, I don't think it improves the code. 

---


# More test cases

```python
many_triangles = [
    (  1, 1, 178, "obtuse"), # big angles
    ( 91, 44, 45, "obtuse"), # just over 90
    (0.01, 0.01, 179.98, "obtuse"), # floats

    (90, 60, 30, "right"), # check 90 for each angle
    (10, 90, 80, "right"),
    (85,  5, 90, "right"),

    (89, 89,  2, "acute"), # just under 90
    (60, 60, 60, "acute"),

    (0, 0, 0, "invalid"),     # zeros
    (61, 60, 60, "invalid"),  # sum > 180
    (90, 91, -1, "invalid"),  # negative numbers
]
``` 

For more on test case selection:
* [Test & Code 38](https://testandcode.com/38) : Prioritize software tests with RCRCRC
* [Test & Code 39](https://testandcode.com/39) : equivalence partitioning, boundary value analysis, decision tables
???

The beauty of parametrization is that when we want to extend our test cases, it's just another line of code.

We started with 4 test cases. 
Here's 11. And it's just as easy to read as before. 

* with parametrization 
    * easy to have a more full set of test cases 
    * without much extra work 
    * without much increased maintenance costs
    
If you are having trouble coming up with a good set of test cases, I talked 
about several techniques on episodes 38 & 39 of Test & Code.

---
# Review

```python
@pytest.mark.parametrize('a, b, c, expected', many_triangles)
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
```
```python
@pytest.fixture(params=many_triangles, ids=idfn)
def a_triangle(request):
    return request.param

def test_fix(a_triangle):
    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected
```
```python
def pytest_generate_tests(metafunc):
    if "gen_triangle" in metafunc.fixturenames:
        metafunc.parametrize("gen_triangle",
                             many_triangles, ids=idfn)

def test_gen(gen_triangle):
    a, b, c, expected = gen_triangle
    assert triangle_type(a, b, c) == expected
```
???
We've covered a lot, but it's really not complicated syntax. 

Here are the three techniques all together.

---
# Combining Techniques

You can have multiple parametrizations for a test function.

* can have multiple `@pytest.mark.parametrize()` decorators.
* can parameterize multiple fixtures per test
* can use pytest_generate_tests() to parametrize multiple parameters
* can use a combination of techniques 
* can blow up into lots and lots of test cases very fast
???
You can also combine techniques. And really should play with them to understand  
their power and their quirks.

When you combine techniques, the number of test cases can multiply rapidly, so   
just be aware of that. 

---

# Resources

.left-two-thirds[
* [Python Testing with pytest](https://t.co/AKfVKcdDoy?amp=1) 
    * The fastest way to get super productive with pytest
* pytest docs on 
    * [parametrization, in general](https://docs.pytest.org/en/latest/parametrize.html) 
    * [function parametrization](https://docs.pytest.org/en/latest/parametrize.html#pytest-mark-parametrize)
    * [fixture parametrization](https://docs.pytest.org/en/latest/fixture.html#fixture-parametrize)
    * [pytest_generate_tests](https://docs.pytest.org/en/latest/parametrize.html#basic-pytest-generate-tests-example)
    * [indirect](http://doc.pytest.org/en/latest/example/parametrize.html#apply-indirect-on-particular-arguments)
* podcasts
    * [Test & Code](https://testandcode.com) 
    * [Python Bytes](https://pythonbytes.fm)
    * [Talk Python](https://talkpython.fm)
* slack community: [Test & Code Slack](https://testandcode.com/slack) 
* Twitter: [@brianokken](https://twitter.com/brianokken), 
* Training: [testandcode.com/training](https://testandcode.com/training)
* This code, and markdown for slides, on [github.com/okken/talks](https://github.com/okken/talks/tree/master/2020/pycon_2020)
]
.right-third[
<a href="https://t.co/AKfVKcdDoy?amp=1">
<img src="images/book.jpg" style="border-style: solid;color:black;" width="200">
</a>
]
???
If you want to learn more about pytest, there's this book called "Python Testing with pytest."

I've listed other great reasources, as well.

Feel free to reach out to me if you have questions.  

I'm also available for corporate training.   
I started that last year, and it's really a lot of fun.

I hope this talk was useful to you. 
If you come up with some cool parametrization uses, I'd love to hear about it. 

Thank you for listening.

Cheers
