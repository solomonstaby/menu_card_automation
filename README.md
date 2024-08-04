# Menu Image Generator

Menu Image Generator is a desktop application built with Python and Tkinter that allows users to generate menu images with custom breakfast, lunch, and dinner items. This application uses a background image template and custom fonts to create visually appealing menu images.

## Features

- Simple GUI to input menu items for breakfast, lunch, and dinner.
- Generates a PNG image with the specified menu items and date.
- Uses a customizable background template and fonts for text styling.

## Requirements

- Python 3.x
- PIL (Pillow)
- Tkinter (included with Python standard library)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/menu-image-generator.git
    cd menu-image-generator
    ```

2. **Install the required Python packages:**

    ```bash
    pip install Pillow
    ```

3. **Run the application:**

    ```bash
    python card_automation.py
    ```

## Usage

1. Launch the application.
2. Enter the menu items for breakfast, lunch, and dinner in the respective text fields.
3. Click the "Generate Menu Image" button.
4. The generated menu image will be saved in the `generated_menus` directory with the current date as the filename.

## Building the Executable

If you want to distribute the application as a standalone executable, you can use PyInstaller:

1. **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2. **Build the executable:**

    ```bash
    pyinstaller --onefile --add-data "bg.jpg;." --add-data "fonts/Garet-Book.ttf;fonts" --add-data "fonts/Garet-Heavy.ttf;fonts" card_automation.py
    ```

3. The executable will be generated in the `dist` directory.

## Files and Directories

- **card_automation.py**: Main script containing the application logic.
- **bg.jpg**: Background image used for the menu template.
- **fonts/**: Directory containing the font files (`Garet-Book.ttf`, `Garet-Heavy.ttf`).
- **generated_menus/**: Directory where generated menu images are saved.

## Contributing

Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the contributors and the community for their support and feedback.

