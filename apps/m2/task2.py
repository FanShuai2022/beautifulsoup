from bs4 import BeautifulSoup, SoupStrainer  # Import BeautifulSoup and SoupStrainer

def print_all_links_optimized(file_path):
    # Read HTML file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create SoupStrainer object to parse only <a> tags
    # SoupStrainer("a") means only parse elements with tag name "a"
    # All other tags will be ignored during parsing and no corresponding objects will be created
    only_a_tags = SoupStrainer("a")
    
    # Pass SoupStrainer object using parse_only parameter
    # BeautifulSoup will parse according to SoupStrainer rules, only parsing <a> tags
    soup = BeautifulSoup(content, 'html.parser', parse_only=only_a_tags)
    
    # Find all <a> tags (due to SoupStrainer, only <a> tags will be found here)
    links = soup.find_all('a')
    
    # Print the number of links found
    print(f"\n{file_path}: Found {len(links)} links")
    
    # Iterate through all links and print information
    for i, link in enumerate(links, 1):
        # Get href attribute value, return 'no href' if it doesn't exist
        href = link.get('href', 'no href')
        # Get link text content, strip=True removes leading and trailing whitespace
        text = link.get_text(strip=True)
        # Print link information
        print(f"{i}. {text} -> {href}")

if __name__ == "__main__":
    # Define list of test files
    test_files = [                    #string[] testFiles =new string[]
        '../test_files/file2_links.html',
        '../test_files/file4_nested.html'
    ]
    
    # Iterate through and process each test file
    for test_file in test_files:
        try:
            # Try to use SoupStrainer to optimize link printing
            print_all_links_optimized(test_file)
        except FileNotFoundError:
            # If file doesn't exist, catch exception and print message
            print(f"File not found: {test_file}\n")

