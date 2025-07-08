"""
file_reader.py
Simple Python script demonstrating file reading and writing.
Author: Francisco Castanedo
"""

def main():
    filename = "sample_python.txt"

    # Write to the file
    with open(filename, "w") as f:
        f.write("This file was created and written by Francisco Castanedo.\n")

    # Read from the file
    with open(filename, "r") as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    main()
