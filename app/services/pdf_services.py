from pathlib import Path
from weasyprint import HTML, CSS

def save_pdf(html_file: Path) -> Path:
    """
    Convert an HTML file to a PDF file and save it.

    Args:
        html_file (Path): The path to the HTML file to convert.

    Returns:
    path: Path to the generated PDF file.
    """
    pdf_dir = Path("generated/pdf")
    pdf_dir.mkdir(parents=True, exist_ok=True)
    pdf_file = pdf_dir / f"{html_file.stem}.pdf"
    HTML(filename=str(html_file)).write_pdf(str(pdf_file))
    return pdf_file