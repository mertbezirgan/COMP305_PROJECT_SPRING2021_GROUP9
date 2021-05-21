import os
import sys
from encode import encode
from decode import decode

file = sys.argv[1]
count = sys.argv[2]

if __name__ == "__main__":
    print("Running file")
    for x in range(int(count)):
        encoded = encode("test-data/" + file + ".txt", "test-data/" + file + "_e.txt")
        file += "_e"
        # Print result
        if encoded == -1:
        # Operation failed
            print("Failed encryption" + str(x+1))
        else:
        # Operation successful
            print("Encryption " + str(x+1) + " successful")

    for x in range(int(count)):
        result = decode("test-data/" + file + ".txt", "test-data/" + file + "_d.txt")
        file += "_d"
        # Print result
        if result == -1:
        # Operation failed
            print("Failed decryption" + str(x+1))
        else:
        # Operation successful
            print("Decryption " + str(x+1) + " successful")
