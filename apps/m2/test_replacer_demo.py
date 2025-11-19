import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from bs4 import BeautifulSoup, SoupReplacer

html_doc = "<p>Hello <b>world</b>!</p>"

b_to_blockquote = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)

print(soup.prettify())

