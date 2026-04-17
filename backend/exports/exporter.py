from fpdf import FPDF

def export_pdf(text, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(filename)
    return filename


def export_markdown(text, filename="report.md"):
    with open(filename, "w") as f:
        f.write(text)

    return filename