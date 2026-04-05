import pdfplumber
with pdfplumber.open(r"Formularios de ejemplo\Ejemplo formulario 350 retencion.pdf") as pdf:
    page = pdf.pages[0]
    words = page.extract_words(keep_blank_chars=True, x_tolerance=3, y_tolerance=3)
    for w in words:
        if 55 <= w["top"] <= 78 and 120 <= w["x0"] <= 300:
            print(f'  top={w["top"]:.1f} x0={w["x0"]:.1f} text={repr(w["text"])}')
    print()
    # Also check near the "4290" text that appeared in the extract_text output
    for w in words:
        if "4290" in w["text"] or "1 . 1" in w["text"]:
            print(f'  MATCH: top={w["top"]:.1f} x0={w["x0"]:.1f} text={repr(w["text"])}')
    print()
    # Also check what's near x0=130-210, top=60-80
    for w in words:
        if 55 <= w["top"] <= 80 and 130 <= w["x0"] <= 500:
            print(f'  AREA: top={w["top"]:.1f} x0={w["x0"]:.1f} text={repr(w["text"])}')
