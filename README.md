# Generate PDFs from LaTeX template and Excel table

This script takes an Excel file and a Template in LaTeX document.
It allows for a dictionary of replacements of structure
  
  key: value

For every row in the Excel file (except the first one taken as header) it creates a copy of the TeX template, replaces the text "{{value}}" in templateFile by content of column of header "key" in Excel, and compiles the TeX.

The output pdfs are renamed using one of the keys and stored in a targed folder. 
