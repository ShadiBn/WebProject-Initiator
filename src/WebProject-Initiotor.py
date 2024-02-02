import os
import subprocess
import json

def create_project(template):
    """
    Creates a new project using npm Vite with the specified template.

    Parameters:
        template (str): The template to use for creating the project.

    Raises:
        subprocess.CalledProcessError: If an error occurs during the subprocess execution.
    """
    try:
        print("Running npm vite to create project and template... Please Wait")
        subprocess.run(["npm", "init", "vite@latest", file_name, "--", "--template", template], shell=True, check=True)
        os.chdir(new_folder_location)
  
        # Install dependencies
        print('Running Npm install Please wait...')
        subprocess.run(["npm", "install"], shell=True, check=True)

        # Open Visual Studio Code
        print("Opening VS Code... Please Wait...")
        subprocess.run(['code', '.'], shell=True, check=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

    except subprocess.CalledProcessError as e:
        # Display the output only when there are errors
        print(f"Error: {e}")
        print(f"Output:\n{e.stdout}\n{e.stderr}")

# Get project information
file_name = input('Enter Project Name: ').lower()
new_folder_location = os.path.join(os.getcwd(), file_name)
print(new_folder_location)

# Display project options
options = """Options: 
1- Default init (html, css, JS) for Simple test and projects
2- Vanilla
3- Vanilla TypeScript
4- React
5- React TypeScript
6- Preact
7- Preact TypeScript
8- Vue
9- Vue TypeScript
"""
print(options)

while True:
    # Select project option
    selected_input = input("Select Option number: ")
  
    if selected_input == "1":
        index_html_content = "<!DOCTYPE html>i\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <link rel=\"stylesheet\" href=\"./style.css\">\n    <title>Document</title>\n</head>\n<body>\n\n    <header>\n\n    </header>\n\n    <main>\n        <div class=\"container\">\n\n        </div>\n    </main>\n\n    <footer>\n\n    </footer>\n\n    <script src=\"./script.js\"></script>\n</body>\n</html>"
        style_css_content= "\n/* The Reset Repository: https://github.com/ShadiBn/My-Css-Reset/tree/main */\n\n/* Css Reset  */\n\n/* Box sizing rules */\n*,\n*::before,\n*::after {\n  box-sizing: border-box;\n}\n\n/* Prevent font size inflation */\nhtml {\n  -moz-text-size-adjust: none;\n  -webkit-text-size-adjust: none;\n  text-size-adjust: none;\n  hanging-punctuation: first last;\n}\n\n/* Remove default margin and padding in favour of better control in authored CSS */\n*{\n    margin: 0;\n    padding: 0;\n    font: inherit;\n}\n\n/* Remove list styles on ul, ol elements with a list role, which suggests default styling will be removed */\nul[role='list'],\nol[role='list'] {\n  list-style: none;\n}\n\n/* Set core body defaults */\nbody {\n  min-height: 100vh;\n  line-height: 1.5;\n}\n\n/* Set shorter line heights on headings and interactive elements */\nh1, h2, h3, h4,\nbutton, input, label {\n  line-height: 1.1;\n}\n\n/* Balance text wrapping on headings */\nh1, h2,\nh3, h4,\nh5, h6 {\n  text-wrap: balance;\n}\n\ninput, button,\ntextarea, select,\np{\n    text-wrap: pretty;\n    max-width: 75ch;\n    margin-bottom: 2em;\n}\n\n/* A elements that don't have a class get default styles */\na:not([class]) {\n  text-decoration-skip-ink: auto;\n  color: currentColor;\n}\n\n/* Make images easier to work with */\nimg,picture,\nsvg,video {\n  max-width: 100%;\n  display: block;\n}\n\n/* Make sure textareas without a rows attribute are not tiny */\ntextarea:not([rows]) {\n  min-height: 10em;\n}\n\n/* Anything that has been anchored to should have extra scroll margin */\n:target {\n  scroll-margin-block: 5ex;\n}\n\n/* Set core root defaults */\nhtml:focus-within,\n:has(:target) {\n  scroll-behavior: smooth;\n}\n\n/* Remove all animations, transitions and smooth scroll for people that prefer not to see them */\n@media (prefers-reduced-motion: reduce) {\n  html:focus-within,\n  :has(:target) {\n    scroll-behavior: auto;\n  }\n  *,\n  *::before,\n  *::after {\n    animation-duration: 0.01ms !important;\n    animation-iteration-count: 1 !important;\n    transition-duration: 0.01ms !important;\n    scroll-behavior: auto !important;\n  }\n}\n\n/* Start Here */\n"
        script_js_content = ""
  
        if not os.path.exists(new_folder_location):
            os.mkdir(new_folder_location)
            print(f'Folder "{new_folder_location}" created successfully.')
        else:
            print(f'Folder "{new_folder_location}" already exists.')
  
        os.chdir(new_folder_location)
  
        file_contents = {
            "index.html": index_html_content,
            "style.css": style_css_content,
            "script.js": script_js_content
        }
  
        # Create project files
        for file_name, file_content in file_contents.items():
            with open(file_name, "w") as file:
                file.write(file_content)
                print(f'File "{file_name}" created successfully.')
  
        # Open Visual Studio Code
        print("Opening VS Code... Please Wait...")
        subprocess.run(['code', '.'], shell=True, check=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        break
  
    elif selected_input.isdigit() and 1 <= int(selected_input) <= 9:
        # Select project template
        templates = [
            "vanilla",
            "vanilla-ts",
            "react",
            "react-ts",
            "preact",
            "preact-ts",
            "vue",
            "vue-ts"
        ]
        template = templates[int(selected_input) - 2]
        create_project(template)
        break

    else:
        print("Invalid option. Please select a valid option.")
