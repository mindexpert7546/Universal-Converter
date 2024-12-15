# Universal Converter Template

## Overview

The **Universal Converter Template** is a Kivy-based Python application designed as a foundation for developers looking to create a versatile unit converter. The app provides essential conversion functionality across various metric categories, including length, mass, time, and more. This template serves as a starting point for creating a comprehensive unit converter and can be extended with additional categories, units, and features.

---

## Features

- **Modular Codebase**: Organized screen, widget, and unit modules enable easy expansion.
- **Real-time Conversions**: Inputs update instantly as values are entered.
- **Customizable UI**: Built with Kivy and KivyMD for flexible and dynamic user interface customization.

---

## Table of Contents

1. [App Structure](#app-structure)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Extending the App](#extending-the-app)
6. [Customization Options](#customization-options)
7. [Building the APK](#building-the-apk)
8. [Download and Support](#download-and-support)
9. [Troubleshooting](#troubleshooting)
10. [License](#license)

---

## App Structure

The app is organized as follows:

- **`main.py`**: The main entry point, initializing the app and managing screen transitions.
- **`main.kv`**: Defines the root UI layout for the app.
- **`presplash.png`**: Displayed during app loading.
- **`icon.png`**: App icon.
- **`buildozer.spec`**: Configuration file for building the app on mobile devices using Buildozer.

### `assets/`

Resources used by the app:
- **`fonts/`**: Custom fonts.
- **`ui/`**: UI assets, including icons and background images.

### `app/`

The core app directory, containing:

1. **`screens/`**

   - **`menuscreen/`**: Contains `menuscreen.py` and `menuscreen.kv`, defining the main menu and navigation to each metric’s conversion screen.
   - **`conversionscreen/`**: Contains `conversionscreen.py` and `conversionscreen.kv`, which handle conversion logic and UI for individual metrics.

2. **`customwidgets/`**

   Defines reusable custom widgets:
   - **`custombuttons/`**: Includes `custombuttons.py` and `custombuttons.kv`, providing custom-styled buttons.
   - **`customlayouts/`**: Contains `customlayouts.py` and `customlayouts.kv`, defining layout structures for UI elements.
   - Additional `.kv` files for popups, labels, and text inputs.

3. **`units/`**

   Contains conversion logic for various metric categories:
   - **`mass.py`**: Mass conversion functions.
   - **`time.py`**: Time conversion functions.
   - **Additional Categories**: Files for other metrics such as length, temperature, and volume.

---

## Requirements

- **Python**: Version 3.11.9 (compatible with Python 3.7+).
- **Kivy**: Version 2.3.0.
- **KivyMD**: Latest development version: https://github.com/kivymd/KivyMD/archive/master.zip.

---

## Setup

### Installation

Download and install the necessary libraries:

```bash
pip install kivy==2.3.0
pip install https://github.com/kivymd/KivyMD/archive/master.zip
pip install materialyoucolor exceptiongroup asyncgui asynckivy
```

### Running the App

Start the app by running:

```bash
python main.py
```

---

## Usage

### Getting Started

When launched, the app opens the Main Menu, where you can select a metric category (e.g., Length, Mass, or Volume). Each category opens a Conversion Screen tailored to that metric, allowing for real-time conversions between units.

### Conversion Workflow

1. Select a Metric: Choose a metric category from the main menu.
2. Enter and Convert: Input a value and select the source and target units.
3. View Results: Converted values update instantly as you adjust inputs.

---

## Extending the App

### Adding New Metrics

To add a new metric:

1. Create a Conversion Class: In the `units/` directory, add a Python file for the new metric (e.g., energy.py) containing conversion logic.
2. Define Units and Conversion Logic: Add unit names and conversion methods to the class.
3. Update UI: Add a button in menuscreen.py for the new metric, and link it to the conversionscreen.

### Adding Custom Widgets

New widgets can be added to the `customwidgets/` directory. Define the widget’s behavior and style in Python and .kv files as necessary.

---

## Customization Options

### UI Customization

Customize the app’s appearance by modifying colors, fonts, and layouts:

1. Colors: Set unique colors for each metric in `menuscreen.kv` and `conversionscreen.kv.`
2. Button and Label Styles: Modify button styles and text labels in the .kv files under `customwidgets/`.

---

## Building the APK

### Using GitHub Actions to Build the APK

The app includes a GitHub workflow configuration (.github/workflows/build.yml) and a buildozer.spec file to streamline the APK creation process.

1. Commit and Push the code to your GitHub repository.
2. Navigate to the Actions tab on your repository’s GitHub page.
3. Select the build.yml workflow and manually trigger it or wait for it to start.
4. Once completed, download the APK from the generated artifacts section of the workflow run.

Note: Ensure all required fields in buildozer.spec are correctly configured before initiating the build process.

### Local APK Build (Optional)

To build the APK locally using Buildozer:

1. Install Buildozer on your machine.
2. Run buildozer android debug to generate an APK file in the bin/ directory.

---

## Download and Support

This template is available for free (minimum price set to $0) on my [Ko-fi](https://ko-fi.com/ouchentech) shop. If you try the template and find it helpful, please consider supporting further development by contributing or leaving a donation. Your support is greatly appreciated and helps enhance and maintain this project.

---

## Troubleshooting

### Common Issues

1. App Not Starting: Ensure all dependencies are installed, particularly the correct versions of Kivy and KivyMD.
2. Incorrect Conversion Results: Verify conversion formulas in the classes within the `units/` folder.

---

## License

This template is distributed under the MIT License. See the LICENSE file for more details.

---

© *OuchenTech 2024*
