#!/bin/bash

# Script to rebuild HTML files from .tex files
echo "Starting to rebuild HTML files from .tex files..."

# Find all .tex files in the technical writings directory
find "technical writings" -name "main.tex" | while read tex_file; do
    # Get the directory name (which is the title)
    dir_name=$(dirname "$tex_file")
    title=$(basename "$dir_name")
    
    # Create a sanitized filename from the title
    filename=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g')
    
    echo "Converting $tex_file to $filename.html..."
    
    # Use pandoc to convert .tex to HTML
    pandoc "$tex_file" \
        --standalone \
        --mathjax \
        --css=styles/main.css \
        --from=latex \
        --to=html5 \
        --output="$filename.html" \
        --metadata title="$title" \
        --template=html_template.html
    
    if [ $? -eq 0 ]; then
        echo "Successfully converted $tex_file to $filename.html"
    else
        echo "Failed to convert $tex_file"
    fi
done

echo "HTML rebuild complete!" 