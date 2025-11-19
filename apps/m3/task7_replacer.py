# Import SoupReplacer class and BeautifulSoup, os module
import sys
import os
# Add beautifulsoup directory to path to import local bs4 package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from bs4 import BeautifulSoup, SoupReplacer


def add_class_to_paragraphs(input_file, output_file=None):
    # If no output file specified, overwrite input file
    if output_file is None:
        output_file = input_file
    
    # Read HTML file content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\nProcessing: {input_file}")
    
    # Count original p tags for display
    p_count = content.count('<p')
    print(f"Found {p_count} <p> tags")
    
    # Define attrs_xformer to add class="test" to p tags
    def add_test_class(tag):
        # Create new attributes dictionary
        new_attrs = dict(tag.attrs) if tag.attrs else {}
        # Set class attribute to "test"
        new_attrs['class'] = 'test'
        return new_attrs
    
    # Create SoupReplacer with attrs_xformer
    # Only apply to p tags by checking tag name in transformer
    def attrs_transformer(tag):
        if tag.name == 'p':
            return add_test_class(tag)
        # Return original attributes for non-p tags
        return dict(tag.attrs) if tag.attrs else {}
    
    replacer = SoupReplacer(attrs_xformer=attrs_transformer)
    
    # Parse HTML with replacer - attributes will be transformed during parsing
    soup = BeautifulSoup(content, "html.parser", replacer=replacer)
    
    # Verify transformations
    p_tags = soup.find_all('p')
    print(f"Processing {len(p_tags)} <p> tags")
    for i, p_tag in enumerate(p_tags, 1):
        old_class = p_tag.get('class')
        p_text = p_tag.get_text(strip=True)[:30]
        if old_class:
            print(f"  {i}. class={old_class}, content: {p_text}...")
        else:
            print(f"  {i}. Added class='test', content: {p_text}...")
    
    # Save transformed HTML to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    # Get the script directory and apps directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # From beautifulsoup/apps/m3, go up one level to beautifulsoup/apps
    apps_dir = os.path.normpath(os.path.join(script_dir, '..'))
    
    # Create output directory (if it doesn't exist)
    output_dir = os.path.join(script_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Define test files relative to apps directory
    test_files_dir = os.path.join(apps_dir, 'test_files')
    test_files = [
        os.path.join(test_files_dir, 'file1_simple.html'),
        os.path.join(test_files_dir, 'file8_paragraphs.html'),
        os.path.join(test_files_dir, 'file3_ids.html')
    ]
    
    # Process each test file
    for test_file in test_files:
        test_file = os.path.normpath(test_file)
        if not os.path.exists(test_file):
            print(f"File not found: {test_file}\n")
            continue
        try:
            # Generate output file path (saved in output directory)
            output_file = os.path.join(output_dir, os.path.basename(test_file))
            # Execute add class operation
            add_class_to_paragraphs(test_file, output_file)
        except Exception as e:
            # If any error occurs, print message
            print(f"Error processing {test_file}: {e}\n")

