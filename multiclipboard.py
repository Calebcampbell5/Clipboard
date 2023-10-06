import sys
import clipboard
import json

# Saved data variable
SAVED_DATA = "clipboard.json"


# Write json file function
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# Read json file function
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# Setting 2 command line arguments 
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

# Save command adding new key's to dict
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

# Load command checks for valid key and saves value to user's clipboard
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist.")
# Delete command delete's key's and values from json file
    elif command == "del":
        key = input("Enter a key to remove: ")
        if key in data:
            del data[key]
            save_data(SAVED_DATA, data)
            print("Key removed from saved data")
        else:
            print("Unknown key!")
    # List command print's out saved key's and values
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
