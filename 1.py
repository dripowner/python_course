import os
from package.src.tex_package_ilya_goldobin.func import latex_table

def get_first_artifact():
    table = [
        ["Header 1", "Header 2", "Header 3"],
        ["Row 1, Col 1", "Row 1, Col 2", "Row 1, Col 3"],
        ["Row 2, Col 1", "Row 2, Col 2", "Row 2, Col 3"],
    ]

    latex_code = latex_table(table, is_document=True)

    with open(os.path.join("artifacts", "2.1.tex"), 'w') as f:
        f.write(latex_code)

get_first_artifact()