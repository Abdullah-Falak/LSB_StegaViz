import tkinter as tk
from tkinter import filedialog, messagebox

# Import the math logic from our other file
from stego_logic import hide_image, extract_image

class StegaVizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LSB-StegaViz: Image-in-Image Steganography")
        self.root.geometry("500x350")
        self.root.configure(padx=20, pady=20)
        self.root.resizable(False, False)

        # Title Label
        title = tk.Label(root, text="LSB-StegaViz Tool", font=("Helvetica", 18, "bold"))
        title.pack(pady=(0, 15))

        # Instructions Label
        instructions = tk.Label(root, text="Select an operation below:", font=("Helvetica", 10))
        instructions.pack(pady=(0, 15))

        # --- Section 1: Hiding Data ---
        hide_frame = tk.LabelFrame(root, text=" 🔒 Hide Data ", font=("Helvetica", 10, "bold"), padx=15, pady=15)
        hide_frame.pack(fill="x", pady=5)

        tk.Button(hide_frame, text="Hide Secret Image inside Cover Image", 
                  command=self.process_hide, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), pady=5).pack(fill="x")

        # --- Section 2: Extracting Data ---
        extract_frame = tk.LabelFrame(root, text=" 🔓 Extract Data ", font=("Helvetica", 10, "bold"), padx=15, pady=15)
        extract_frame.pack(fill="x", pady=15)

        tk.Button(extract_frame, text="Extract Secret Image from Stego Image", 
                  command=self.process_extract, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"), pady=5).pack(fill="x")

    def process_hide(self):
        cover_path = filedialog.askopenfilename(title="Select Cover Image", filetypes=[("Image Files", "*.png *.jpg *.bmp")])
        if not cover_path: return
        
        secret_path = filedialog.askopenfilename(title="Select Secret Image", filetypes=[("Image Files", "*.png *.jpg *.bmp")])
        if not secret_path: return
        
        output_path = filedialog.asksaveasfilename(title="Save Stego Image As", defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("BMP Files", "*.bmp")])
        if not output_path: return
        
        # Call the logic file and get the result
        success, message = hide_image(cover_path, secret_path, output_path)
        
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def process_extract(self):
        stego_path = filedialog.askopenfilename(title="Select Stego Image", filetypes=[("PNG Files", "*.png"), ("BMP Files", "*.bmp")])
        if not stego_path: return
        
        output_path = filedialog.asksaveasfilename(title="Save Extracted Image As", defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("BMP Files", "*.bmp")])
        if not output_path: return
        
        # Call the logic file and get the result
        success, message = extract_image(stego_path, output_path)
        
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = StegaVizApp(root)
    root.mainloop()
