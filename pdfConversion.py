from docx2pdf import convert
import os

def convert_docs_to_pdf(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for file in os.listdir(src_dir):
        if file.endswith(".docx"):
            input_path = os.path.join(src_dir, file)
            output_path = os.path.join(dest_dir, file.replace(".docx", ".pdf"))
            convert(input_path, output_path)
            print(f"✅ Converted: {input_path} → {output_path}")

# Jenkins workspace paths
source_dir = "C:/ProgramData/Jenkins/.jenkins/workspace/test"
destination_dir = "C:/ProgramData/Jenkins/.jenkins/workspace/test"

convert_docs_to_pdf(source_dir, destination_dir)
