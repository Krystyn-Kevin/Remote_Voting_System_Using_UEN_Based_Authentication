import tkinter as tk
from tkinter import messagebox

def Generate_UEN():
    # Clear any existing table
    for widget in table_frame.winfo_children():
        widget.destroy()

    try:
        x = str(series.get())
        y = int(count.get())
        if y==0 :
            messagebox.showerror("Warning","Enter integer other than 0")
    except ValueError:
        messagebox.showerror("Warning","Enter +ve integer only ")
        return

    # Generate UENs
    UEN = []
    for i in range(1,y+1):
        b = len(str(y)) - len(str(i))
        a = str(x) + (b * "0") + str(i)
        UEN.append(a)

    rows = 20   # number of rows to display before scroll
    cols = 20  # number of columns per row

    # Display in grid format
    for idx, val in enumerate(UEN):
        r = idx // cols
        c = idx % cols
        label = tk.Label(table_frame, text=val, borderwidth=1, relief="solid",
                         width=15, height=1, font=("Courier", 9))
        label.grid(row=r, column=c, padx=1, pady=1)

    # Update scroll region
    table_canvas.update_idletasks()
    table_canvas.config(scrollregion=table_canvas.bbox("all"))

# --- GUI setup ---
root = tk.Tk()
root.title("UEN Generator")

tk.Label(root, text="Enter the starting series of UEN:").pack()
series = tk.Entry(root)
series.pack()

tk.Label(root, text="Enter number of UEN required:").pack()
count = tk.Entry(root)
count.pack()

tk.Button(root, text="Generate UEN", command=Generate_UEN).pack(pady=5)

# Create a frame for the scrollable table
table_container = tk.Frame(root)
table_container.pack(fill="both", expand=True, pady=10)

# Canvas + Scrollbars
table_canvas = tk.Canvas(table_container)
scrollbar_y = tk.Scrollbar(table_container, orient="vertical", command=table_canvas.yview)
scrollbar_x = tk.Scrollbar(table_container, orient="horizontal", command=table_canvas.xview)
table_frame = tk.Frame(table_canvas)

# Configure scrolling
table_frame.bind(
    "<Configure>",
    lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all"))
)

table_canvas.create_window((0, 0), window=table_frame, anchor="nw")
table_canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

# Pack everything
table_canvas.grid(row=0, column=0, sticky="nsew")
scrollbar_y.grid(row=0, column=1, sticky="ns")
scrollbar_x.grid(row=1, column=0, sticky="ew")

table_container.grid_rowconfigure(0, weight=1)
table_container.grid_columnconfigure(0, weight=1)

tk.Button(root, text="Quit", command=root.quit).pack(pady=5)

root.mainloop()
