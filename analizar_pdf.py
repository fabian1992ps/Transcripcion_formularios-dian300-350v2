import pdfplumber
import sys

filename = sys.argv[1]

with pdfplumber.open(filename) as pdf:
    page = pdf.pages[0]
    words = page.extract_words(keep_blank_chars=True, x_tolerance=3, y_tolerance=3)
    for i, w in enumerate(words):
        x0 = w["x0"]
        top = w["top"]
        x1 = w["x1"]
        text = w["text"]
        print(f"  [{i:3d}] x0={x0:7.1f} top={top:7.1f} x1={x1:7.1f} text={text!r}")
