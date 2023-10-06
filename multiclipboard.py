import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"


# Save Data
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# Load Json Data
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

# Save command
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

# Load command
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist.")

    elif command == "del":
        key = input("Enter a key to remove: ")
        if key in data:
            del data[key]
            save_data(SAVED_DATA, data)
            print("Key removed from saved data")
        else:
            print("Unknown key!")
    
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")