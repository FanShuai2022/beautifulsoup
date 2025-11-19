
# Milestone 3: SoupReplacer API Extension

Milestone 2 had a simple API: `SoupReplacer("b", "blockquote")` replaces all `<b>` tags with `<blockquote>`. It's fast and easy, but limited to tag renaming.

Milestone 3 adds a more flexible API with transformer functions: `SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`. The `name_xformer` transforms tag names, `attrs_xformer` returns new attribute dictionaries, and `xformer` can perform side effects. You can use them separately or combine them.
