from bs4 import BeautifulSoup, SoupStrainer  # Import BeautifulSoup and SoupStrainer

def print_tags_with_id_optimized(file_path):
    # Read HTML file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create SoupStrainer object to parse only tags with id attribute
    # id=True means filter condition is "id attribute exists" (regardless of id value)
    # This is a powerful feature of SoupStrainer, allowing filtering by attribute existence
    has_id = SoupStrainer(id=True)
    
    # Pass SoupStrainer object using parse_only parameter
    # BeautifulSoup will parse according to SoupStrainer rules, only parsing tags with id attribute
    soup = BeautifulSoup(content, 'html.parser', parse_only=has_id)
    
    # Find all tags (due to SoupStrainer, only tags with id attribute will be found here)
    tags_with_id = soup.find_all()
    
    # Print the number of tags found
    print(f"\n{file_path}")
    print(f"Tags with id: {len(tags_with_id)}\n")
    
    # Iterate through all found tags and print information
    for i, tag in enumerate(tags_with_id, 1):
        # Get the id attribute value of the tag
        tag_id = tag.get('id')
        # Get partial text content of the tag (first 30 characters) to avoid long output
        tag_text = tag.get_text(strip=True)[:30]
        # Print tag information: tag name and id value
        print(f"{i}. <{tag.name}> id={tag_id}")
        # If tag has text content, print partial text
        if tag_text:
            print(f"   {tag_text}...")

if __name__ == "__main__":
    # Define list of test files
    test_files = [
        '../test_files/file3_ids.html',
        '../test_files/file10_mixed.html'
    ]
    
    # Iterate through and process each test file
    for test_file in test_files:
        try:
            # Try to use SoupStrainer to optimize printing tags with id attribute
            print_tags_with_id_optimized(test_file)
        except FileNotFoundError:
            # If file doesn't exist, catch exception and print message
            print(f"File not found: {test_file}\n")

