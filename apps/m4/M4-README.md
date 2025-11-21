# Milestone 4: BeautifulSoup Iteration

Added `__iter__` method to the `BeautifulSoup` class so you can iterate over it directly. The implementation uses depth-first traversal through the document tree, following the `next_element` pointer chain just like the existing `descendants` property.

The algorithm starts from the first child element and follows `next_element` pointers until it reaches the end. It yields each element as it goes, so it's lazy - no need to collect everything into a list first, which is good for memory efficiency on large documents.

The method handles empty soup objects by returning an empty iterator. Five tests verify it works correctly for different scenarios including simple HTML, empty documents, and proper depth-first ordering.

## Files Modified

Modified `beautifulsoup/bs4/__init__.py` to add the `__iter__` method around line 1130. 

## Test Files

Created `beautifulsoup/bs4/tests/test_iteration.py` with 5 test cases covering basic iteration, empty documents, different tag types, traversal order, and iterator stopping behavior.

## Running Tests

You can run the tests in a couple ways. From the project root, just run

```
python beautifulsoup/bs4/tests/test_iteration.py
```

Or if you're already in the beautifulsoup directory

```
python -m bs4.tests.test_iteration
```
