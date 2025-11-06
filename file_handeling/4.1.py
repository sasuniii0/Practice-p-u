import sys

def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())
    
if __name__ == "__main__":
    filename = sys.argv[1]
    num_lines = count_lines(filename)
    print(f"The file '{filename}' has {num_lines} lines.")