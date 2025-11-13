# Analog-IC-Design-

## Plot MOSFET Characteristics using Python
This Python script helps analog and circuit designers quickly visualize transistor characteristics from CSV files — such as:

    -Id vs Vgs plots  
    -Gm vs MOS Width plots
  
These graphs are essential for MOSFET sizing and amplifier or any analog circuit design.

The script automatically:

    -Reads CSV data and extracts labels from the header.  
    -Plots the data with proper scaling and grid.  
    -Lets you click on any data point to view its exact coordinates.


Run the code using:

  `python plot_csv.py ./CSV_Files/id_vgs_NMOS.csv`

Preview:
<img width="900" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/352a6221-5ca4-4a54-b425-c02dbd3202e4" />

  


## Combine_CDL_FIles

This Python script helps VLSI and analog designers merge multiple CDL (Circuit Description Language) netlists into a single file.

If you have a library of standard cell CDL files, this tool saves time by automatically combining them so you can import all netlists at once into tools like Cadence Virtuoso or HSPICE.

    -Combines all CDL files matching a given regex pattern
    -Reads files safely using UTF-8 encoding
    -Automatically adds file names as headers for clarity
    -Skips files that can’t be read
    -Outputs a single, ready-to-import CDL file

Usage:

`python fileCat.py <fileRegeX> <outputFileName> <Directory>`

Example:

`python fileCat.py "\.cdl$" combined_lib.cdl ./StandardCells`

** Useful for merging any other file type eg:- .py, .txt, .html, etc **
