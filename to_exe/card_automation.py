import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os
import sys

# Constants
DEFAULT_TEMPLATE_PATH = "bg.jpg"  # Path to the default template image
OUTPUT_FOLDER = "generated_menus"  # Folder to save output images

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for both bundled and non-bundled cases. """
    try:
        # PyInstaller creates a temp folder and stores paths in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def create_menu_image(date, breakfast, lunch, dinner, template_path, output_filename):
    # Paths to the fonts
    regular_font_path = resource_path("fonts/Garet-Book.ttf")
    bold_font_path = resource_path("fonts/Garet-Heavy.ttf")

    # Load the template image
    background = Image.open(resource_path(template_path))
    
    # Create a drawing context
    draw = ImageDraw.Draw(background)

    # Load fonts
    date_font = ImageFont.truetype(regular_font_path, 45)  # Font size for the date
    bold_font = ImageFont.truetype(bold_font_path, 55)     # Larger size and bold for labels
    regular_font = ImageFont.truetype(regular_font_path, 50)  # Font size for the menu items

    # Define text positions
    date_position = (500, 380)
    menu_position = (400, 500)  # Starting position for the menu

    # Draw the date
    draw.text(date_position, date, font=date_font, fill="black")

    # Define the menu sections with bold labels
    menu_sections = {
        "Breakfast": breakfast,
        "Lunch": lunch,
        "Dinner": dinner
    }

    # Line spacing
    line_spacing = 20  # Increased line spacing

    # Draw each menu section
    y_position = menu_position[1]
    
    for label, items in menu_sections.items():
        # Add space before the label
        y_position += line_spacing
        
        # Draw the label (e.g., "Breakfast", "Lunch", "Dinner") in bold
        label_bbox = draw.textbbox((menu_position[0], y_position), label, font=bold_font)
        label_width = label_bbox[2] - label_bbox[0]
        item_x = menu_position[0] + 600 / 2 - label_width / 2  # Center align label
        draw.text((item_x, y_position), label, font=bold_font, fill="black")
        
        # Update y_position for menu items
        y_position += label_bbox[3] - label_bbox[1] + line_spacing  # Add space after label
        
        # Draw the menu items in regular font
        menu_items_lines = items.split('\n')
        
        for line in menu_items_lines:
            # Calculate the bounding box for the line of text
            line_bbox = draw.textbbox((menu_position[0], y_position), line, font=regular_font)
            line_width = line_bbox[2] - line_bbox[0]
            item_x = menu_position[0] + 600 / 2 - line_width / 2  # Center align text
            draw.text((item_x, y_position), line, font=regular_font, fill="black")
            
            # Update the position for the next line
            y_position += line_bbox[3] - line_bbox[1] + line_spacing  # Add space after each item
        
        # Add a one-line space after each section's items (except the last section)
        if label != "Dinner":
            y_position += line_spacing  # Add a space between sections

    # Optional: Adjust the bottom position if needed
    if y_position > background.height - 50:  # Ensure it doesn't go out of bounds
        print("Warning: Menu items exceed image bounds!")

    # Save the image
    background.save(output_filename)

def generate_image():
    date = datetime.now().strftime("%d-%m-%Y")  # Format: DD-MM-YYYY
    breakfast = breakfast_entry.get("1.0", tk.END).strip()
    lunch = lunch_entry.get("1.0", tk.END).strip()
    dinner = dinner_entry.get("1.0", tk.END).strip()
    output_filename = os.path.join(OUTPUT_FOLDER, f"menu_{date}.png")

    create_menu_image(date, breakfast, lunch, dinner, DEFAULT_TEMPLATE_PATH, output_filename)
    messagebox.showinfo("Success", f"Menu image created: {output_filename}")

# Create the GUI window
root = tk.Tk()
root.title("Menu Image Generator")

# Create and place the widgets
ttk.Label(root, text="Breakfast Items:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
breakfast_entry = tk.Text(root, height=5, width=40)
breakfast_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Lunch Items:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
lunch_entry = tk.Text(root, height=5, width=40)
lunch_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Dinner Items:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
dinner_entry = tk.Text(root, height=5, width=40)
dinner_entry.grid(row=2, column=1, padx=10, pady=5)

generate_button = ttk.Button(root, text="Generate Menu Image", command=generate_image)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
