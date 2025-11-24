# Milestone-3

## Technical Brief: SoupReplacer API Comparison

### Milestone 2 API (Simple Tag Replacement)

Milestone 2 provides a simple, straightforward API for tag renaming:

```python
replacer = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(html, "html.parser", replacer=replacer)
```

**Characteristics:**
-  Fast and easy to use
-  Direct tag name replacement
-  Limited to simple tag renaming only
-  Cannot modify attributes
-  No conditional logic

**Use Case:** Replace all `<b>` tags with `<blockquote>` tags.

### Milestone 3 API (Flexible Transformer Functions)

Milestone 3 extends the API with three transformer functions for advanced manipulation:

```python
replacer = SoupReplacer(
    name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name,
    attrs_xformer=lambda tag: {**tag.attrs, "class": "test"} if tag.name == "p" else tag.attrs,
    xformer=lambda tag: tag.string.replace("old", "new") if tag.string else None
)
soup = BeautifulSoup(html, "html.parser", replacer=replacer)
```

**Characteristics:**
-  Transform tag names conditionally
-  Modify tag attributes dynamically
-  Perform side effects on tags
-  Combine multiple transformers
-  Full control over transformation logic

**Use Case:** Add `class="test"` to all `<p>` tags, replace `<b>` with `<strong>`, and modify tag content.

### API Comparison

| Feature | Milestone 2 | Milestone 3 |
|---------|-------------|-------------|
| **API Style** | Simple constructor | Transformer functions |
| **Tag Renaming** | Direct replacement | Conditional transformation |
| **Attribute Modification** | Not supported | Via `attrs_xformer` |
| **Side Effects** | Not supported | Via `xformer` |
| **Conditional Logic** | Not supported | Full support |
| **Complexity** | Low | Medium to High |
| **Performance** | Fast | Fast (same parsing speed) |
| **Backward Compatible** | N/A | Auto-detects API style |

### When to Use Which?

- **Use Milestone 2 API** when you need simple, one-to-one tag replacement (e.g., `<b>` → `<blockquote>`)
- **Use Milestone 3 API** when you need:
  - Conditional transformations based on tag properties
  - Attribute manipulation (add, remove, modify)
  - Content modification or side effects
  - Complex transformation logic

Both APIs work together - the implementation automatically detects which API you're using based on the constructor arguments.

## Test cases for new API

- `bs4/tests/test_soup_replacer3.py` : lines 9-192

## How to Test

```bash
python -m pytest bs4/tests/test_soup_replacer3.py -v
```

Or run the test file directly:

```bash
python bs4/tests/test_soup_replacer3.py
```

## How to run?

1. **Navigate to m3 directory**:
   ```bash
   cd beautifulsoup/apps/m3
   ```

2. **Run the task script**:
   ```bash
   python task7_replacer.py
   ```

The script will:
- Process test files from `beautifulsoup/apps/test_files/`:
  - `file1_simple.html`
  - `file8_paragraphs.html`
  - `file3_ids.html`
- Save output files to `m3/output/` directory
- Display processing information in the console
