import json
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        sys.exit(1)

def compare_json(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)
    
    if data1.keys() != data2.keys():
        print("The JSON files have different keys.")
        return
    
    for key in data1:
        if sorted(data1[key]) != sorted(data2[key]):
            print(f"Mismatch found in key: {key}")
            return
    
    print("The JSON files contain the same data.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_json.py <file1.json> <file2.json>")
        sys.exit(1)
    
    file1, file2 = sys.argv[1], sys.argv[2]
    compare_json(file1, file2)
