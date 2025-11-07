# Analog-IC-Design-

##Common Sorce Amplifier Design

This Python script helps analog and circuit designers quickly visualize transistor characteristics from CSV files — such as:

  -Id–Vgs plots
  -Gm–Width plots
  
These graphs are essential for MOSFET sizing and common-source amplifier design.

The script automatically:

  -Reads CSV data and extracts labels from the header.
  -Plots the data with proper scaling and grid.
  -Automatically switches to scientific notation for large or small values.
  -Lets you click on any data point to view its exact coordinates.

  python plot_csv.py ./CSV_Files/id_vgs_NMOS.csv
