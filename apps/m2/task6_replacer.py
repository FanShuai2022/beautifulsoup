# Import SoupReplacer class and os module
import sys
import os
# Add beautifulsoup directory to path to import local bs4 package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from bs4 import SoupReplacer

def replace_b_tags_new_method(input_file, output_file):
    # Read HTML file content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Print file being processed
    print(f"\nProcessing: {input_file}")
    
    # Create SoupReplacer object
    # Replacement rule: replace b tags with blockquote tags
    replacer = SoupReplacer(content, {'b': 'blockquote'})
    # Perform parsing and replacement
    replacer.parse_and_replace()
    
    # Count the number of b tags in original file (for display)
    # Note: This counts the original content, the count after replacement should be the same
    b_count = content.count('<b>')
    print(f"Found {b_count} <b> tags")
    
    # Save replaced HTML to file
    replacer.save_to_file(output_file)
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    # Create output directory (if it doesn't exist)
    os.makedirs('output/milestone2', exist_ok=True)
    
    # Define list of test files
    test_files = [
        'test_files/file7_bold.html',
        'test_files/file10_mixed.html'
    ]
    
    # Iterate through and process each test file
    for test_file in test_files:
        try:
            # Generate output file path (saved in output/milestone2 directory)
            output_file = f"output/milestone2/{os.path.basename(test_file)}"
            # Perform replacement operation
            replace_b_tags_new_method(test_file, output_file)
        except FileNotFoundError:
            # If file doesn't exist, catch exception and print message
            print(f"File not found: {test_file}")

