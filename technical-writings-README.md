# Technical Writings

This folder contains technical writings with LaTeX content rendered using MathJax.

## How to Add a New Technical Writing

1. Create a new folder in the `technical writings` directory with your topic name (e.g., `technical writings/New Topic`).

2. Add your LaTeX files and images to this folder.

3. Convert any PDF images to PNG for better web display:
   ```
   mkdir -p technical-writings-images
   pdftoppm "technical writings/New Topic/your-image.pdf" "technical-writings-images/your-image" -png -singlefile
   ```

4. Copy the `technical-writing-template.html` file and rename it to match your topic (e.g., `new-topic.html`):
   ```
   cp technical-writing-template.html new-topic.html
   ```

5. Edit the new HTML file:
   - Replace `[TITLE]` with your topic name
   - Add your LaTeX content in the `math-content` div
   - Update image paths to point to your PNG images

6. Add a link to your new topic in the `technical-writings.html` file by adding a new folder container:
   ```html
   <a href="new-topic.html" class="folder-container">
     <div class="folder-icon">📝</div>
     <h3>New Topic</h3>
   </a>
   ```

7. Commit and push your changes:
   ```
   git add .
   git commit -m "Add new technical writing: New Topic"
   git push origin master
   ```

## MathJax Tips

- Inline math: Use `\(` and `\)` to delimit inline math expressions.
- Display math: Use `\begin{align}` and `\end{align}` for aligned equations.
- For more complex LaTeX, refer to the [MathJax documentation](https://docs.mathjax.org/).

## File Structure

```
/
├── technical-writings.html        # Main page listing all technical writings
├── power-calculation.html         # Individual technical writing page
├── technical-writing-template.html # Template for new technical writings
├── technical-writings-images/     # Directory for converted images
│   └── normals.png
└── technical writings/            # Original LaTeX files and PDFs
    └── Power Calculation/
        ├── main.tex
        └── normals.pdf
``` 