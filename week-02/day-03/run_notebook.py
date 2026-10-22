import nbformat
from pathlib import Path
from nbclient import NotebookClient

folder = Path(__file__).parent
notebook_path = folder / "eda_report.ipynb"

notebook = nbformat.read(notebook_path, as_version=4)
client = NotebookClient(
    notebook,
    timeout=180,
    kernel_name="python3",
    allow_errors=False
)

client.execute(cwd=str(folder))
nbformat.write(notebook, notebook_path)

print("SUCCESS: EDA notebook executed.")
print("Notebook outputs saved:", notebook_path)
