# Import SoupReplacer class
from bs4 import SoupReplacer

def test_multiple_replacements():
    # Test HTML content containing multiple tags that need to be replaced
    html = """
    <html>
    <head><title>Test</title></head>
    <body>
        <h1>Title</h1>
        <p>Paragraph with <b>bold</b> and <i>italic</i> text</p>
        <div>
            <b class="important">Important content</b>
            <i id="note">Note</i>
        </div>
    </body>
    </html>
    """
    
    print("Test 1: Replace multiple tags simultaneously\n")
    print("Original HTML snippet:")
    print(html)
    
    # Define replacement rules: replace 3 types of tags simultaneously
    # Replace b tags with strong, i tags with em, div tags with section
    replacements = {
        'b': 'strong',
        'i': 'em',
        'div': 'section'
    }
    
    # Create SoupReplacer object and perform replacement
    replacer = SoupReplacer(html, replacements)
    result = replacer.get_html()
    
    # Print replaced HTML
    print(result)
    
    # Verify replacement results
    # Verify that old tags are completely removed
    assert '<b>' not in result, "Error: <b> tags still exist"
    assert '<i>' not in result, "Error: <i> tags still exist"
    
    # Verify that new tags are correctly generated
    assert '<strong>' in result, "Error: <strong> tags were not generated"
    assert '<em>' in result, "Error: <em> tags were not generated"
    
    # Verify that attributes are preserved
    # class="important" should be preserved on strong tag
    assert 'class="important"' in result, "Error: class attribute was not preserved"
    
    # If all assertions pass, print success message
    print("Test passed")

if __name__ == "__main__":
    test_multiple_replacements()

