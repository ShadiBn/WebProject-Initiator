# WebProject-Initiator

WebProject-Initiator is a Python script (converted to EXE) designed to quickly initialize new projects using npm Vite with various templates. This script supports default templates for simple HTML, CSS with a reset, and JavaScript projects, as well as different options for popular frameworks like React, Vue, Preact, and more.

## Prerequisites

Ensure that you have the following software installed on your machine:

- [Node.js](https://nodejs.org/en)
- [Visual Studio Code (VsCode)](https://code.visualstudio.com/)

## Getting Started

Follow these steps to use the script:

1. **Download:** Visit the [Releases](https://github.com/ShadiBn/WebProject-Initiotor/releases) page.
2. **Download EXE:** Choose the latest release and download the `WebProject-Initiotor.exe` file.
3. **Run EXE:** Double-click on `WebProject-Initiotor.exe` to execute the script.
4. **Follow Prompts:** Follow the on-screen prompts to select the desired project template.

## Important Note

This script utilizes Python's OS and Subprocesses, which might trigger antivirus warnings. If you encounter this situation, consider the following options:

### Option 1 - Bypass Antivirus and Allow on Device

### Option 2 - Build the Source File to an EXE Application

1. **Download the source file:** Navigate to [src/WebProject-Initiotor.py](https://github.com/ShadiBn/WebProject-Initiotor/blob/main/src/WebProject-Initiotor.py) and download or copy the file.
2. **Install Python on your computer:** Visit [Python.org](https://www.python.org/downloads/) to download and install Python.
3. **Install PyInstaller:** Open your terminal and type the following:
   ```bash
   pip install pyinstaller
   ```
4. **Open terminal in the folder containing the Python source folder:** It's recommended to create a new folder and copy the Python source code downloaded earlier.
5. **Build Your App:** Type the following command in the correct PATH to build the EXE app:
   ```bash
   pyinstaller --onefile Path/To/Folder/WebProject-Initiotor.py
   ```
6. **Find your app:** You will find your EXE app in the `dist` folder.
7. **Have Fun Coding!**

### Project Templates

- **Default Init:** Create a simple project with HTML, CSS, and JavaScript files.
- **Vanilla:** Create a project with a vanilla JavaScript template.
- **Vanilla - TypeScript:** Create a project with a vanilla TypeScript template.
- **React:** Initialize a React project.
- **React - TypeScript:** Initialize a React project with TypeScript.
- **Vue:** Set up a project with Vue.js.
- **Vue - TypeScript:** Set up a project with Vue.ts.

## Feedback and Contributions

Feel free to provide feedback, report issues, or contribute to the project by opening [issues](https://github.com/ShadiBn/WebProject-Initiotor/issues) or submitting [pull requests](https://github.com/ShadiBn/WebProject-Initiotor/pulls).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
