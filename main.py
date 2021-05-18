import os
from decode import decode

test_file_name = "/compressed-test-data/default-compressed.txt"
test_file_output_name = "/res.txt"
test_bit_size = 8

if __name__ == "__main__":
    print("Running file")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = dir_path + test_file_name
    output_file_name = dir_path + test_file_output_name

    result = decode(file_name, output_file_name)

    # Print result
    if result == -1:
        # Operation failed
        print("Failed operation")
    else:
        # Operation successful
        print("Operation successful")
