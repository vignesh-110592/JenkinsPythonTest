import os
import sys
import tempfile
import shutil
import subprocess
from docx import Document
from pathlib import Path

def create_mock_docx(filepath, content_lines):
    doc = Document()
    for line in content_lines:
        doc.add_paragraph(line)
    doc.save(filepath)

def test_replace_script_with_args():
    # Setup temp repo-like structure
    temp_root = tempfile.mkdtemp()
    input_dir = Path(temp_root) / "inputs"
    output_dir = Path(temp_root) / "outputs"
    input_dir.mkdir()
    output_dir.mkdir()

    anschreiben_content = [
        "__DATE__",
        "Company_name",
        "Greeting Person_name, applying for Position_name."
    ]
    lebenslauf_content = ["__DATE__"]

    create_mock_docx(input_dir / "AnschreibenRaw.docx", anschreiben_content)
    create_mock_docx(input_dir / "LebenslaufRaw.docx", lebenslauf_content)

    # Copy the script into temp_root/scripts
    script_dir = Path(temp_root) / "scripts"
    script_dir.mkdir()
    script_path = script_dir / "replace_docx_text.py"

    original_script = Path("replace_docx_text.py").read_text()
    # Patch __file__-based repo path resolution for testability
    patched_script = original_script.replace("dirname(dirname(__file__))", f'"{temp_root}"')
    script_path.write_text(patched_script)

    # Arguments to pass
    args = ["OpenAI", "Dear", "Alice", "Engineer"]

    # Run the script with arguments
    result = subprocess.run(
        [sys.executable, str(script_path)] + args,
        cwd=str(script_dir),
        capture_output=True,
        text=True,
    )

    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    assert result.returncode == 0

    # Verify Anschreiben.docx
    anschreiben_out = Document(output_dir / "Anschreiben.docx")
    text_a = "\n".join(p.text for p in anschreiben_out.paragraphs)
    assert "__DATE__" not in text_a
    assert "Company_name" not in text_a
    assert "Greeting" not in text_a
    assert "Person_name" not in text_a
    assert "Position_name" not in text_a
    assert "OpenAI" in text_a
    assert "Dear" in text_a
    assert "Alice" in text_a
    assert "Engineer" in text_a

    # Verify Lebenslauf.docx
    lebenslauf_out = Document(output_dir / "Lebenslauf.docx")
    text_l = "\n".join(p.text for p in lebenslauf_out.paragraphs)
    assert "__DATE__" not in text_l

    # Clean up (optional in dev, automatic in CI)
    shutil.rmtree(temp_root)
