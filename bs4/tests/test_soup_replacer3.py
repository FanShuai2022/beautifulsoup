# Test cases for Milestone-3 SoupReplacer API
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from bs4 import BeautifulSoup, SoupReplacer


def test_name_xformer_basic():
    """Test 1: Basic name_xformer functionality - replace b tags with blockquote"""
    html_doc = "<p>Hello <b>world</b>!</p>"
    
    b_to_blockquote = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
    soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)
    
    result = soup.prettify()
    print("Test 1: Basic name_xformer")
    print(f"Original: {html_doc}")
    print(f"Result: {result}")
    
    # Verify transformation
    assert '<b>' not in result, "Error: <b> tags still exist"
    assert '<blockquote>' in result, "Error: <blockquote> tags were not generated"
    assert soup.find('blockquote') is not None, "Error: blockquote tag not found in soup"
    print("Test 1 passed\n")


def test_name_xformer_multiple_tags():
    """Test 2: name_xformer with multiple tag types"""
    html_doc = "<div><b>bold</b> and <i>italic</i> text</div>"
    
    def name_transformer(tag):
        if tag.name == "b":
            return "strong"
        elif tag.name == "i":
            return "em"
        return tag.name
    
    replacer = SoupReplacer(name_xformer=name_transformer)
    soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
    
    result = soup.prettify()
    print("Test 2: name_xformer with multiple tag types")
    print(f"Original: {html_doc}")
    print(f"Result: {result}")
    
    # Verify transformations
    assert '<b>' not in result, "Error: <b> tags still exist"
    assert '<i>' not in result, "Error: <i> tags still exist"
    assert '<strong>' in result, "Error: <strong> tags were not generated"
    assert '<em>' in result, "Error: <em> tags were not generated"
    assert soup.find('strong') is not None, "Error: strong tag not found"
    assert soup.find('em') is not None, "Error: em tag not found"
    print("Test 2 passed\n")


def test_attrs_xformer_add_class():
    """Test 3: attrs_xformer to add class attribute"""
    html_doc = '<p>Paragraph 1</p><p id="p2">Paragraph 2</p>'
    
    def attrs_transformer(tag):
        new_attrs = dict(tag.attrs) if tag.attrs else {}
        new_attrs['class'] = 'test'
        return new_attrs
    
    replacer = SoupReplacer(attrs_xformer=attrs_transformer)
    soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
    
    result = soup.prettify()
    print("Test 3: attrs_xformer to add class attribute")
    print(f"Original: {html_doc}")
    print(f"Result: {result}")
    
    # Verify all p tags have class="test"
    p_tags = soup.find_all('p')
    assert len(p_tags) == 2, "Error: Expected 2 p tags"
    for p in p_tags:
        assert p.get('class') == ['test'] or p.get('class') == 'test', f"Error: p tag missing class='test': {p}"
    print("Test 3 passed\n")


def test_attrs_xformer_remove_class():
    """Test 4: attrs_xformer to remove class attribute"""
    html_doc = '<p class="old">Paragraph 1</p><p class="old other">Paragraph 2</p>'
    
    def attrs_transformer(tag):
        new_attrs = dict(tag.attrs) if tag.attrs else {}
        if 'class' in new_attrs:
            del new_attrs['class']
        return new_attrs
    
    replacer = SoupReplacer(attrs_xformer=attrs_transformer)
    soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
    
    result = soup.prettify()
    print("Test 4: attrs_xformer to remove class attribute")
    print(f"Original: {html_doc}")
    print(f"Result: {result}")
    
    # Verify all p tags have no class attribute
    p_tags = soup.find_all('p')
    assert len(p_tags) == 2, "Error: Expected 2 p tags"
    for p in p_tags:
        assert p.get('class') is None, f"Error: p tag still has class attribute: {p}"
    print("Test 4 passed\n")


def test_xformer_remove_class():
    """Test 5: xformer to remove class attribute (side effects)"""
    html_doc = '<p class="old">Paragraph 1</p><p class="old other">Paragraph 2</p>'
    
    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    
    class_deleter = SoupReplacer(xformer=remove_class_attr)
    soup = BeautifulSoup(html_doc, "html.parser", replacer=class_deleter)
    
    result = soup.prettify()
    print("Test 5: xformer to remove class attribute")
    print(f"Original: {html_doc}")
    print(f"Result: {result}")
    
    # Verify all p tags have no class attribute
    p_tags = soup.find_all('p')
    assert len(p_tags) == 2, "Error: Expected 2 p tags"
    for p in p_tags:
        assert p.get('class') is None, f"Error: p tag still has class attribute: {p}"
    assert 'class=' not in result, "Error: class attribute still exists in output"
    print("Test 5 passed\n")


def test_combined_transformers():
    """Test 6: Combined name_xformer, attrs_xformer, and xformer"""
    html_doc = '<b class="important">Bold text</b><i>Italic text</i>'
    
    def name_transformer(tag):
        if tag.name == "b":
            return "strong"
        return tag.name
    
    def attrs_transformer(tag):
        new_attrs = dict(tag.attrs) if tag.attrs else {}
        # Add data-transformed attribute to all tags that were transformed from b
        if tag.name == "strong":
            new_attrs['data-transformed'] = 'true'
        return new_attrs
    
    def general_transformer(tag):
        # Add a custom attribute using xformer's side effect capability
        if tag.name == "strong":
            tag['transformed-by'] = 'xformer'
    
    replacer = SoupReplacer(
        name_xformer=name_transformer,
        attrs_xformer=attrs_transformer,
        xformer=general_transformer
    )
    soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
    
    result = soup.prettify()
    print("Test 6: Combined transformers")
    print(f"Original: {html_doc}")
    print(f"Result: {result}")
    
    # Verify combined transformations
    assert '<b>' not in result, "Error: <b> tags still exist"
    strong_tag = soup.find('strong')
    assert strong_tag is not None, "Error: strong tag not found"
    assert strong_tag.get('data-transformed') == 'true', "Error: data-transformed attribute missing"
    # Verify xformer added custom attribute via side effects
    assert strong_tag.get('transformed-by') == 'xformer', "Error: transformed-by attribute not added by xformer"
    assert strong_tag.get('class') == ['important'] or strong_tag.get('class') == 'important', "Error: original class attribute not preserved"
    print("Test 6 passed\n")


if __name__ == "__main__":
    print("=" * 60)
    print("Running Milestone-3 SoupReplacer API Tests")
    print("=" * 60 + "\n")
    
    test_name_xformer_basic()
    test_name_xformer_multiple_tags()
    test_attrs_xformer_add_class()
    test_attrs_xformer_remove_class()
    test_xformer_remove_class()
    test_combined_transformers()
    
    print("=" * 60)
    print("All tests passed!")
    print("=" * 60)

