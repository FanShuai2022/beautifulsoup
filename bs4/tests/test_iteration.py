# Test cases for Milestone 4: BeautifulSoup iteration
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString


def test_iterate_simple_html():
    """Test 1: Iterate over a simple HTML document"""
    html_doc = "<html><head><title>Page</title></head><body><p>Hello</p></body></html>"
    soup = BeautifulSoup(html_doc, "html.parser")
    
    elements = list(soup)
    
    print("Test 1: Iterate simple HTML")
    print(f"HTML: {html_doc}")
    print(f"Found {len(elements)} elements")
    
    # Verify we got elements
    assert len(elements) > 0, "Error: No elements found"
    
    # Verify we get both tags and strings
    has_tags = any(isinstance(e, Tag) for e in elements)
    has_strings = any(isinstance(e, NavigableString) for e in elements)
    assert has_tags, "Error: No Tag elements found"
    assert has_strings, "Error: No NavigableString elements found"
    
    # Verify order: html -> head -> title -> "Page" -> body -> p -> "Hello"
    assert elements[0].name == 'html', "Error: First element should be html tag"
    
    print("Test 1 passed\n")


def test_iterate_empty_soup():
    """Test 2: Iterate over an empty Soup object"""
    soup = BeautifulSoup("", "html.parser")
    
    elements = list(soup)
    
    print("Test 2: Iterate empty soup")
    print(f"Found {len(elements)} elements")
    
    # Empty soup should yield no elements
    assert len(elements) == 0, f"Error: Expected 0 elements, got {len(elements)}"
    
    print("Test 2 passed\n")


def test_iterate_different_tag_types():
    """Test 3: Iterate over document with different tag types and string nodes"""
    html_doc = "<div><span>Text</span><p>Paragraph</p></div>"
    soup = BeautifulSoup(html_doc, "html.parser")
    
    elements = list(soup)
    
    print("Test 3: Iterate different tag types")
    print(f"HTML: {html_doc}")
    print(f"Found {len(elements)} elements")
    
    # Get tag names
    tag_names = [e.name for e in elements if isinstance(e, Tag)]
    print(f"Tag names in order: {tag_names}")
    
    # Verify we have different tag types
    assert 'div' in tag_names, "Error: div tag not found"
    assert 'span' in tag_names, "Error: span tag not found"
    assert 'p' in tag_names, "Error: p tag not found"
    
    # Verify we have string nodes
    strings = [str(e) for e in elements if isinstance(e, NavigableString)]
    assert len(strings) > 0, "Error: No string nodes found"
    
    print("Test 3 passed\n")


def test_iterate_depth_first_order():
    """Test 4: Verify traversal order is depth-first"""
    html_doc = "<html><head><title>Page</title></head></html>"
    soup = BeautifulSoup(html_doc, "html.parser")
    
    elements = list(soup)
    
    print("Test 4: Verify depth-first order")
    print(f"HTML: {html_doc}")
    
    # Get element names/types in order
    element_info = []
    for e in elements:
        if isinstance(e, Tag):
            element_info.append(f"<{e.name}>")
        else:
            element_info.append(f"'{str(e)[:20]}'")
    print(f"Element order: {' -> '.join(element_info)}")
    
    # Expected order: html -> head -> title -> "Page"
    # Find indices
    html_idx = next(i for i, e in enumerate(elements) if isinstance(e, Tag) and e.name == 'html')
    head_idx = next(i for i, e in enumerate(elements) if isinstance(e, Tag) and e.name == 'head')
    title_idx = next(i for i, e in enumerate(elements) if isinstance(e, Tag) and e.name == 'title')
    
    # Verify depth-first order: html comes before head, head before title
    assert html_idx < head_idx, "Error: html should come before head"
    assert head_idx < title_idx, "Error: head should come before title"
    
    # Title should come before its string content
    title_str_idx = next((i for i, e in enumerate(elements) if isinstance(e, NavigableString) and 'Page' in str(e)), None)
    if title_str_idx:
        assert title_idx < title_str_idx, "Error: title tag should come before its content"
    
    print("Test 4 passed\n")


def test_iterator_stops_correctly():
    """Test 5: Ensure iterator stops correctly after traversal"""
    html_doc = "<p>First</p><p>Second</p>"
    soup = BeautifulSoup(html_doc, "html.parser")
    
    # Convert to list first
    elements_list = list(soup)
    print(f"Test 5: Iterator stops correctly")
    print(f"HTML: {html_doc}")
    print(f"Found {len(elements_list)} elements")
    
    # Verify we can iterate multiple times
    first_iteration = list(soup)
    second_iteration = list(soup)
    
    assert len(first_iteration) == len(second_iteration), "Error: Iteration results differ"
    assert len(first_iteration) > 0, "Error: No elements in iteration"
    
    # Verify iterator is exhausted correctly
    iterator = iter(soup)
    count = 0
    try:
        while True:
            next(iterator)
            count += 1
            # Safety check to avoid infinite loop
            if count > 100:
                assert False, "Error: Iterator does not stop"
    except StopIteration:
        pass
    
    assert count == len(elements_list), f"Error: Iterator count {count} != list length {len(elements_list)}"
    
    # Verify iterator raises StopIteration when exhausted
    try:
        next(iterator)
        assert False, "Error: Iterator should raise StopIteration when exhausted"
    except StopIteration:
        pass
    
    print("Test 5 passed\n")


if __name__ == "__main__":
    print("=" * 60)
    print("Running Milestone-4 BeautifulSoup Iteration Tests")
    print("=" * 60 + "\n")
    
    test_iterate_simple_html()
    test_iterate_empty_soup()
    test_iterate_different_tag_types()
    test_iterate_depth_first_order()
    test_iterator_stops_correctly()
    
    print("=" * 60)
    print("All tests passed!")
    print("=" * 60)

