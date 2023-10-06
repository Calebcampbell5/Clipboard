# Clipboard
User Clipboard
This project is a Python automation script for managing clipboard data using a JSON file. It allows you to save and load data from the clipboard for quick access to frequently used text snippets or file paths.

## Getting Started

To get started with this automation script, follow these steps:

1. Clone the repository to your local machine:
2. Install the required dependencies:
pip install clipboard

3. Run the script with one of the following commands:

- `python script.py save` to save clipboard data.
- `python script.py load` to load data from the clipboard.
- `python script.py clear` to clear the clipboard.
- `python script.py del` to delete a key from the saved data.

## Example Usage

You can use the JSON file provided (`clipboard.json`) to save keys as script names and values as file paths. This can help you manage and access your scripts and files more efficiently.

Example JSON data in `clipboard.json`:

```json
{
 "Script Name 1": "/path/to/script1.py",
 "Script Name 2": "/path/to/script2.py",
 "File 1": "/path/to/file1.txt"
}
