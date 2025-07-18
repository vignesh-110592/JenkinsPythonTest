from docx2pdf import convert
import os

source = os.path.abspath("Lebenslauf.docx")
dest = os.path.abspath("Lebenslauf.pdf")
convert(source, dest)

source = os.path.abspath("Anschreiben.docx")
dest = os.path.abspath("Anschreiben.pdf")
convert(source, dest)
