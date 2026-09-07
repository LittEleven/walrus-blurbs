import os

src = "txt_files"
out = "."

for fname in os.listdir(src):
    if fname.endswith(".txt"):
        with open(os.path.join(src, fname), encoding="utf-8") as f:
            content = f.read()
        title = fname.replace(".txt", "")
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title></head>
<body>
<h1>{title}</h1>
<pre>{content}</pre>
</body></html>"""
        with open(os.path.join(out, fname.replace(".txt", ".html")), "w", encoding="utf-8") as f:
            f.write(html)