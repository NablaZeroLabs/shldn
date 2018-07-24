# Testing

Using [unittest](https://docs.python.org/3/library/unittest.html#unittest.TestSuite) to test shldn finding division functionality. Not using [pytest](https://www.google.com/search?q=pytest&rlz=1C5CHFA_enUS803US803&oq=pytest&aqs=chrome..69i57j69i60l3j35i39j0.882j0j1&sourceid=chrome&ie=UTF-8) to keep low list of dependencies.

## Running the tests
Inside the parent directory of `tests/` run
```
python3 -m unittest [-v] tests/test.py
```

## The Tests

### Testing Division Cases in Python source files
- Normal division
- Nested division e.g. `1/(2/3)`
- Division in print statement
- No division
- Syntax Error

### Different Python source file extensions
In order to test:
- add extension to `EXTENSIONS` constant in `leonard.py`
- add file with different extension to `EXT_FILES` constant 
    - *i.e.* `div.py` or `monte.mpy`
    - file should contain:
        - ONLY 1 division 
        - between two numbers 
        - in line 1