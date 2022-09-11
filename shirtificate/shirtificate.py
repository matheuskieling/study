from fpdf import FPDF


name = input("Name: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 42)
pdf.cell(0, 40, "CS50 Shirtificate", align='C')
pdf.image("./shirtificate.png", x=0, y=60)
pdf.set_font("helvetica", "B", 28)
pdf.set_text_color(255, 255, 255)
pdf.cell(-190, 230, f"{name} took CS50", align='C')
pdf.output("shirtificate.pdf")
