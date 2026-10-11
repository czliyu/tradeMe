import os
from pypdf import PdfReader

SRC = "/home/ericli/workspace/tradeMd/以交易为生.pdf"
OUT = "/home/ericli/workspace/tradeMd/_extract/pdf"
os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
os.makedirs(os.path.join(OUT, "text"), exist_ok=True)

reader = PdfReader(SRC)
for i, page in enumerate(reader.pages, start=1):
    try:
        text = page.extract_text() or ""
    except Exception:
        text = ""
    text = text.encode("utf-8", "replace").decode("utf-8")
    with open(os.path.join(OUT, "text", f"p{i:03d}.txt"), "w") as f:
        f.write(text)
    for j, im in enumerate(page.images, start=1):
        fn = f"p{i:03d}_{j}.jpg"
        with open(os.path.join(OUT, "images", fn), "wb") as f:
            f.write(im.data)
print("done")
