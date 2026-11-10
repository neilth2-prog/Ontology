"""Build the single-file Ontograph page: index.html with vendor.js inlined."""
import sys, datetime
src, vendor, out = sys.argv[1], sys.argv[2], sys.argv[3]
html = open(src, encoding="utf-8").read(); js = open(vendor, encoding="utf-8").read()
tag = '<script src="vendor.js"></script>'
assert html.count(tag) == 1, "vendor script tag not found exactly once"
assert "</script" not in js.lower() and "<!--" not in js, "vendor.js needs escaping before it can be inlined"
note = "<!-- Ontograph, standalone build of %s. One file: three.js, 3d-force-graph and three-spritetext are bundled inline. Voice and sentence structuring need the hosted page in Claude. -->\n" % datetime.date.today().isoformat()
html = html.replace(tag, "<script>\n" + js + "\n</script>")
html = html.replace("<!DOCTYPE html>\n", "<!DOCTYPE html>\n" + note, 1)
open(out, "w", encoding="utf-8").write(html)
print(out, len(html.encode("utf-8")), "bytes")
