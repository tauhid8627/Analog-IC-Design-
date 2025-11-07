import csv
import matplotlib.pyplot as plt
import os
import sys

# --- Check command line arguments ---
if len(sys.argv) != 2:
    print("Usage: python plot_csv.py <path_to_csv>")
    sys.exit(1)

csvpath = sys.argv[1]

if not os.path.exists(csvpath):
    print("Error: File not found.")
    sys.exit(1)

x, y = [], []

# --- Read CSV ---
with open(csvpath, 'r', encoding="utf-8") as csvFile:
    reader = csv.reader(csvFile)
    header = next(reader, None)  # Try to read header row

    xaxis = header[0] if header and len(header) > 0 else "X"
    yaxis = header[1] if header and len(header) > 1 else "Y"

    for i, row in enumerate(reader, start=2):
        if not row or len(row) < 2:
            continue
        try:
            x.append(float(row[0]))
            y.append(float(row[1]))
        except ValueError:
            print(f"Skipping invalid row {i}: {row}")

# --- Plot setup ---
fig, ax = plt.subplots(figsize=(9, 6))
sc = ax.scatter(x, y, color='blue', s=40, picker=True)  # ✅ make points clickable
ax.plot(x, y, linestyle='solid', color='lightgray', alpha=0.6)

ax.set_xlabel(xaxis, fontsize=12)
ax.set_ylabel(yaxis, fontsize=12)
title=os.path.basename(csvpath)
newtitle=title.split('.')
ax.set_title(newtitle[0], fontsize=13)
plt.yticks(rotation=25)
ax.grid(True)

#plt.tight_layout()

# --- Click event handler ---
def on_pick(event):
    ind = event.ind[0]
    xval, yval = x[ind], y[ind]
    print(f"Selected point → X: {xval}, Y: {yval}")
    ax.scatter(xval, yval, color='red', s=100, zorder=3, label=f"({xval:.3g}, {yval:.3g})")
    ax.legend(loc="best")
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('pick_event', on_pick)

plt.show()
