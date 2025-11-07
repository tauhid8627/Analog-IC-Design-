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
