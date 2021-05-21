import os
import timeit
from encode_base64 import encode
from decode_base64 import decode

start = timeit.default_timer()

test_file_name = "/test-data/alice29_encodedBase64.txt"
test_file_output_name = "/resBase64.txt"
test_bit_size = 8

if __name__ == "__main__":
    print("Running file")
    encode("test-data/alice29.txt")
    
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
        
stop = timeit.default_timer()

print('Time: ', stop - start) 
