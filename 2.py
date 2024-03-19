from tex_package_ilya_goldobin.func import latex2pdf, latex_image, latex_document
from tex_package_ilya_goldobin.func import latex_table
import os

def get_second_artifact():
    table = [
        ["Header 1", "Header 2", "Header 3"],
        ["Row 1, Col 1", "Row 1, Col 2", "Row 1, Col 3"],
        ["Row 2, Col 1", "Row 2, Col 2", "Row 2, Col 3"],
    ]
    image_latex = latex_image("./img.jpg")
    table_latex = latex_table(table)
    b, e = latex_document(with_image=True)
    with open(os.path.join("artifacts", "2.2.tex"), 'w') as f:
        f.write(b + table_latex + image_latex + e)
    return latex2pdf(os.path.join("artifacts", "2.2.tex"))

get_second_artifact()