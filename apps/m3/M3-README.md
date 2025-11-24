
# Milestone 3: SoupReplacer API Extension

Milestone 2 had a simple API: `SoupReplacer("b", "blockquote")` replaces all `<b>` tags with `<blockquote>`. It's fast and easy, but limited to tag renaming.

Milestone 3 adds a more flexible API with transformer functions: `SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`. The `name_xformer` transforms tag names, `attrs_xformer` returns new attribute dictionaries, and `xformer` can perform side effects. You can use them separately or combine them.

### Task 7 – Add `class="test"` to all `<p>` tags using SoupReplacer

The script `task7_replacer.py` reimplements Milestone-1 Task-7 using the extended `SoupReplacer` API.  
Instead of walking the tree after parsing, it uses `attrs_xformer` so that all `<p>` tags get `class="test"` **during parsing**.

**What it does:**

- Reads several HTML test files from `beautifulsoup/apps/test_files/`:
  - `file1_simple.html`
  - `file8_paragraphs.html`
  - `file3_ids.html`
- For every `<p>` tag, sets/overwrites the `class` attribute to `"test"` via `SoupReplacer(attrs_xformer=...)`.
- Writes the transformed HTML into `beautifulsoup/apps/m3/output/` with the same file names.

**How to run Task-7:**

```bash
cd beautifulsoup/apps/m3
python task7_replacer.py

