# pytest Fixtures

* Presentation with Transitions: [pdf](presentation.pdf)
* Presentation without Transitions: [pdf](presentation_short.pdf) - better for printing

## To run the code

```
$ cd code
$ python3 -m venv venv --prompt noaa
$ source venv/bin/activate  
(noaa) $ pip install -r requirements.txt 
(noaa) $ pytest
========================= test session starts ==========================
collected 16 items                                                     

test_builtin.py .                                                [  6%]
test_no_fixtures.py .                                            [ 12%]
test_pytest.py .                                                 [ 18%]
test_scope.py .                                                  [ 25%]
test_unittest.py .                                               [ 31%]
test_xunit.py .                                                  [ 37%]
tests/test_count.py ..                                           [ 50%]
tests/test_crud.py .......                                       [ 93%]
tests/test_update.py .                                           [100%]

========================== 16 passed in 0.06s ==========================
```