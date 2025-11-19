from bs4 import BeautifulSoup, SoupStrainer  # Import BeautifulSoup and SoupStrainer
from collections import Counter  # Import Counter class for counting tag occurrences

def print_all_tags_optimized(file_path):
    # Read HTML file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Method 1: Parse all tags normally (full parsing)
    # This method parses all tags in the document and creates a complete DOM tree
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extract names of all tags
    all_tags = [tag.name for tag in soup.find_all()]
    # Use Counter to count occurrences of each tag
    tag_counter = Counter(all_tags)
    
    # Print statistics
    print(f"\n{file_path}")
    print(f"Total tags: {len(all_tags)}")
    # most_common(10) returns the top 10 most common tags
    for tag_name, count in tag_counter.most_common(10):
        print(f"  {tag_name}: {count}")
    
    # Method 2: Only count p and div tags (optimized with SoupStrainer)
    # This method only parses p and div tags, other tags will be ignored
    print("\nOnly p and div tags:")
    # SoupStrainer(name=['p', 'div']) creates a filter to parse only p and div tags
    # name parameter can be a string (single tag) or a list (multiple tags)
    only_p_div = SoupStrainer(name=['p', 'div'])
    # Pass SoupStrainer using parse_only parameter to parse only specified tags
    soup2 = BeautifulSoup(content, 'html.parser', parse_only=only_p_div)
    # Extract filtered tag names
    filtered_tags = [tag.name for tag in soup2.find_all()]
    # Count filtered tags
    filtered_counter = Counter(filtered_tags)
    # Print filtered statistics
    for tag_name, count in filtered_counter.items():
        print(f"  {tag_name}: {count}")

if __name__ == "__main__":
    # Define list of test files
    test_files = [
        'test_files/file6_tags.html',
        'test_files/file10_mixed.html'
    ]
    
    # Iterate through and process each test file
    for test_file in test_files:
        try:
            # Try to use SoupStrainer to optimize tag statistics printing
            print_all_tags_optimized(test_file)
        except FileNotFoundError:
            # If file doesn't exist, catch exception and print message
            print(f"File not found: {test_file}\n")

