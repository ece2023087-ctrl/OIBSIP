import tkinter as tk
from tkinter import ttk, messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        weight_unit = weight_unit_combobox.get()
        height_unit = height_unit_combobox.get()
        
        if weight_unit == "lbs":
            weight = weight * 0.45359237
            
        if height_unit == "inches":
            height = height * 0.0254
        elif height_unit == "meters":
            if height > 3.0: 
                height = height / 100.0
        
        if height <= 0 or weight <= 0:
            messagebox.showerror("Input Error", "Height and Weight must be greater than 0.")
            return

        bmi = weight / (height ** 2)
        
        # Determine Category and Color Theme dynamically
        if bmi < 18.5:
            category = "Underweight"
            status_bg = "#AED6F1"   # Soft Blue
            status_fg = "#1B4F72"   # Dark Blue Text
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            status_bg = "#ABEBC6"   # Soft Green
            status_fg = "#145A32"   # Dark Green Text
        elif 24.9 <= bmi < 29.9:
            category = "Overweight"
            status_bg = "#F9E79F"   # Soft Yellow/Orange
            status_fg = "#7D6608"   # Dark Yellow Text
        else:
            category = "Obese"
            status_bg = "#FADBD8"   # Soft Red
            status_fg = "#78281F"   # Dark Red Text
            
        suggested_min_weight = 18.5 * (height ** 2)
        suggested_max_weight = 24.9 * (height ** 2)
        
        # 1. Update text content
        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {category}")
        weight_range_label.config(text=f"Suggested weight range: {suggested_min_weight:.2f} - {suggested_max_weight:.2f} kg")
        height_range_label.config(text="Suggested Height Range: 1.53 - 1.77 meters")
        
        # 2. Update background and text colors based on the calculation result
        for label in [bmi_label, category_label, weight_range_label, height_range_label]:
            label.config(bg=status_bg, fg=status_fg)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

# --- Color Configuration ---
BG_MAIN = "#F4F6F7"       # Soft Light Gray background for the app window
TEXT_COLOR = "#2C3E50"    # Dark gray text color for entry labels
BG_DEFAULT_LABEL = "#E5E8E8" # Default grey for labels before calculation
BTN_COLOR = "#34495E"     # Dark slate button color

# --- UI Setup ---
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("520x480")
root.configure(padx=25, pady=25, bg=BG_MAIN)

# Weight Row
tk.Label(root, text="Weight:", font=("Arial", 12, "bold"), bg=BG_MAIN, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", pady=12)
weight_entry = tk.Entry(root, font=("Arial", 12), width=15, bg="#FFFFFF", fg=TEXT_COLOR, relief="solid", bd=1)
weight_entry.grid(row=0, column=1, pady=12, padx=10)
weight_entry.insert(0, "58") 

weight_unit_combobox = ttk.Combobox(root, values=["kg", "lbs"], font=("Arial", 11), width=8, state="readonly")
weight_unit_combobox.grid(row=0, column=2, pady=12)
weight_unit_combobox.set("kg")

# Height Row
tk.Label(root, text="Height:", font=("Arial", 12, "bold"), bg=BG_MAIN, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", pady=12)
height_entry = tk.Entry(root, font=("Arial", 12), width=15, bg="#FFFFFF", fg=TEXT_COLOR, relief="solid", bd=1)
height_entry.grid(row=1, column=1, pady=12, padx=10)
height_entry.insert(0, "167") 

height_unit_combobox = ttk.Combobox(root, values=["meters", "inches"], font=("Arial", 11), width=8, state="readonly")
height_unit_combobox.grid(row=1, column=2, pady=12)
height_unit_combobox.set("meters")

# Calculate Button
calculate_btn = tk.Button(
    root, text="Calculate", bg=BTN_COLOR, fg="white", 
    font=("Arial", 12, "bold"), padx=15, pady=5, 
    activebackground="#2C3E50", activeforeground="white",
    relief="raised", bd=2, command=calculate_bmi
)
calculate_btn.grid(row=2, column=0, columnspan=3, pady=25)

# Output Labels (Configured with default gray color initially)
bmi_label = tk.Label(root, text="BMI: 0.00", font=("Arial", 12, "bold"), bg=BG_DEFAULT_LABEL, fg=TEXT_COLOR, width=42, anchor="w", padx=10, pady=6)
bmi_label.grid(row=3, column=0, columnspan=3, sticky="w", pady=6)

category_label = tk.Label(root, text="Category: ", font=("Arial", 12), bg=BG_DEFAULT_LABEL, fg=TEXT_COLOR, width=42, anchor="w", padx=10, pady=6)
category_label.grid(row=4, column=0, columnspan=3, sticky="w", pady=6)

weight_range_label = tk.Label(root, text="Suggested weight range: ", font=("Arial", 12), bg=BG_DEFAULT_LABEL, fg=TEXT_COLOR, width=42, anchor="w", padx=10, pady=6)
weight_range_label.grid(row=5, column=0, columnspan=3, sticky="w", pady=6)

height_range_label = tk.Label(root, text="Suggested Height Range: ", font=("Arial", 12), bg=BG_DEFAULT_LABEL, fg=TEXT_COLOR, width=42, anchor="w", padx=10, pady=6)
height_range_label.grid(row=6, column=0, columnspan=3, sticky="w", pady=6)

root.mainloop()
