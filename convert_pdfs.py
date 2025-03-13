import os
import subprocess
from pathlib import Path
import re
from bs4 import BeautifulSoup

# Base directory for technical writings
base_dir = "technical writings"

# Function to convert second page of PDF to PNG
def convert_pdf_to_png(pdf_path, output_dir):
    # Extract filename without extension
    filename = os.path.basename(pdf_path)
    filename_no_ext = os.path.splitext(filename)[0]
    output_path = os.path.join(output_dir, f"{filename_no_ext}.png")
    
    # Use pdftoppm for conversion, specifying the second page (-f 2 -l 2)
    try:
        subprocess.run([
            "pdftoppm", "-png", "-f", "2", "-l", "2", "-singlefile", 
            pdf_path, os.path.join(output_dir, filename_no_ext)
        ], check=True)
        # Rename the output file if necessary
        potential_output = os.path.join(output_dir, f"{filename_no_ext}-2.png")
        if os.path.exists(potential_output):
            os.rename(potential_output, output_path)
        print(f"Converted page 2 of {pdf_path} to {output_path}")
        return filename_no_ext + ".png"
    except subprocess.CalledProcessError:
        # Fallback to ImageMagick if pdftoppm fails
        try:
            subprocess.run([
                "convert", "-density", "300", f"{pdf_path}[1]", "-quality", "90", 
                output_path
            ], check=True)
            print(f"Converted page 2 of {pdf_path} to {output_path} using ImageMagick")
            return filename_no_ext + ".png"
        except subprocess.CalledProcessError:
            print(f"Failed to convert {pdf_path}")
            return None

# Process each project folder
for project_dir in os.listdir(base_dir):
    project_path = os.path.join(base_dir, project_dir)
    
    # Skip if not a directory
    if not os.path.isdir(project_path):
        continue
    
    latex_dir = os.path.join(project_path, "latex")
    html_dir = os.path.join(project_path, "html")
    
    # Skip if latex or html directory doesn't exist
    if not os.path.isdir(latex_dir) or not os.path.isdir(html_dir):
        print(f"Skipping {project_dir}: missing latex or html directory")
        continue
    
    print(f"Processing project: {project_dir}")
    
    # Find all PDF files in the latex directory that match the pattern
    pdf_files = [f for f in os.listdir(latex_dir) if f.lower().endswith('.pdf') and 'coverage_' in f]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(latex_dir, pdf_file)
        
        # Convert PDF to PNG (second page)
        png_filename = convert_pdf_to_png(pdf_path, html_dir)
        
        if png_filename:
            print(f"Successfully converted {pdf_file} to {png_filename}")

print("Conversion complete!")