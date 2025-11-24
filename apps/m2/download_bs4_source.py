import os  # Used for file path operations

def locate_bs4_source():
    try:
        # Import bs4 module
        import bs4
        # Get the file path of the bs4 module (usually the path of __init__.py)
        bs4_path = bs4.__file__
        # Extract the directory path (remove the file name, keep only the directory)
        bs4_dir = os.path.dirname(bs4_path)      
        
        # Print source code location
        print("Source code location:", bs4_dir)
        
        # List key source files
        files = ['__init__.py', 'element.py', 'builder/__init__.py']
        for f in files:
            # Construct full file path
            full_path = os.path.join(bs4_dir, f)
            # If file exists, print the path
            if os.path.exists(full_path):
                print(f"  {f}: {full_path}")
        
        return bs4_dir
    except ImportError:
        # If import fails, BeautifulSoup is not installed
        print("BeautifulSoup not found, install it first: pip install beautifulsoup4")
        return None

def find_api_definitions():
    # First locate the bs4 source code directory
    bs4_dir = locate_bs4_source()
    if not bs4_dir:
        # If not found, exit directly
        return
    
    print("\nAPI locations:")
    
    # Define the list of API functions to look for
    apis = [
        'find_all',      # Find all matching elements
        'find',          # Find the first matching element
        'select',        # Find elements using CSS selectors
        'find_parent',   # Find parent element
        'find_next_sibling',      # Find next sibling element
        'find_previous_sibling',  # Find previous sibling element
        'new_tag',       # Create a new tag
        'replace_with',  # Replace a tag
        'prettify'       # Pretty-print HTML output
    ]
    
    # element.py contains most Tag class method definitions
    element_file = os.path.join(bs4_dir, 'element.py')
    if os.path.exists(element_file):
        print(f"\nMost definitions are in element.py")
        
        # Read content of element.py
        with open(element_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Search for each API function definition
        for api in apis:
            # Look for the function definition line
            for i, line in enumerate(lines, 1):
                # Match function definition (format: def function_name)
                if f'def {api}' in line:
                    # Print function name and its line number
                    print(f"  {api}(): line {i}")
                    break

if __name__ == "__main__":
    # Locate API function definitions
    find_api_definitions()
