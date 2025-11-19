# Import SoupReplacer class
from bs4 import SoupReplacer

def test_nested_tags():
    # Test HTML content containing multi-level nested b tags
    html = """
    <html>
    <body>
        <div>
            <div>
                <div>
                    <b>Deeply nested bold</b>
                </div>
                <b>Second level bold</b>
            </div>
            <b>First level bold</b>
        </div>
        <p>Normal paragraph with <b>bold<b>nested bold</b></b></p>
    </body>
    </html>
    """
    
    # Print original HTML
    print(html)
    
    # Create SoupReplacer object, replace b tags with blockquote
    replacer = SoupReplacer(html, {'b': 'blockquote'})
    # Perform replacement and get result
    result = replacer.get_html()
    
    # Print replaced HTML
    print("\nAfter replacement:")
    print(result)
    
    # Verify that all b tags have been replaced
    # If <b> tags still exist in the result, replacement failed
    assert '<b>' not in result, "Error: <b> tags still exist, replacement incomplete"
    # Verify that blockquote tags have been generated
    assert '<blockquote>' in result, "Error: <blockquote> tags were not generated"
    
    # Count the number of replaced tags
    # Confirm how many b tags were replaced by counting <blockquote> tags
    count = result.count('<blockquote>')
    print(f"\nTotal {count} <b> tags replaced")
    
    # If all assertions pass, print success message
    print("Test passed")

if __name__ == "__main__":
    test_nested_tags()

