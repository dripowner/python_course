import os
import posixpath

def latex_table(table: list[list], is_document: bool=False) -> str:
    """
    Generates LaTeX code for a table from a list of lists.

    :table: A list of lists, where each inner list represents a row of the table.
    :is_document: if True then returns  complete document with \documentclass{article}, else only the tabular environment.
    :return: A string containing the LaTeX code for the table.
    """
    latex = "\\begin{table}[ht]\n\\centering"\
            "\n\\begin{tabular}{|c|c|c|}\n\\hline\n"

    for row in table:
        for item in row:
            latex += f"{item} & "
        latex = latex[:-2] + "\\\\\n\\hline\n"  # remove the last " & " and add "\\" for a new row

    latex += "\end{tabular}\n\end{table}\n"
    if is_document:
        preamble, ending = latex_document()
        return preamble + latex + ending
    else:
        return latex

def latex_image(image_path: str, width: int=8, height: int=4, is_document: bool=False) -> str:
    """
    Generate a LaTeX command for inserting an image with a given width, height, and DPI.

    Args:
        image_path (str): The path to the image file.
        width (int, optional): The desired width of the image in centimeters. Defaults to 8.
        height (int, optional): The desired height of the image in centimeters. Defaults to 4.
        dpi (int, optional): The resolution of the image in dots per inch. Defaults to 300.
        is_document (bool, optional) : If True, returns complete document environment including preamble and end.

    Returns:
        str: A LaTeX command for inserting the image with the specified dimensions.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    
    image_directory = os.path.dirname(image_path)
    image_basename = os.path.basename(image_path)
    path = posixpath.join(image_directory, image_basename.split('.')[0])
    latex = f"\\includegraphics[width={width}cm, height={height}cm]{{{path}}}\n"

    if is_document:
        preamble, ending = latex_document(with_image=True)
        return preamble + latex + ending
    else:
        return latex

def latex_document(with_image: bool=False) -> tuple[str, str]:
    """
    Generate the beginning and ending parts of a LaTeX document.

    If `with_image` is True, then the code to include an image is added to the
    preamble.

    Returns:
        A tuple containing the LaTeX document preamble and ending.
    """
    preamble = "\\documentclass{article}\n"
    if with_image:
        preamble += "\\usepackage{graphicx}\n"
    preamble += "\\begin{document}\n"
    ending = "\\end{document}"
    return preamble, ending

def latex2pdf(tex_path: str) -> None:
    """
    This function, `latex2pdf`, takes in a single argument, `tex_path`, which is a string representing the file path of a LaTeX file.
    The function converts the given LaTeX file into a PDF using the `pdflatex` command.
    It then cleans up the generated auxiliary files, specifically deleting the `.log` and `.aux` files associated with the LaTeX file.
    
    Args:
        tex_path (str): The file path of the input LaTeX file.
    
    Returns:
        None: This function does not return any value, but instead performs the conversion and cleanup operations in-place.
    
    Raises:
        FileNotFoundError: If the `pdflatex` command is not found in the system's PATH.
        OSError: If there is any issue with executing the `pdflatex` command or deleting the generated files.
    """
    if not os.path.exists(tex_path):
        raise FileNotFoundError("The specified TeX file does not exist.")

    basename = os.path.basename(tex_path)
    os.system(f"pdflatex {tex_path}")
    os.remove(f"{basename[:-4]}.log")
    os.remove(f"{basename[:-4]}.aux")
    
