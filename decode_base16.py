
# This function decodes the file
def decode(file_name, output_file_name, code_type = "base10", bit_size = 256):
    print("Inside decode")
    # This variable holds main dict used for decoding
    code_dict = {}

    # Read file to decode
    with open(file_name, 'r', encoding="utf-8") as f:
        # Read every line at once
        compressed_data = f.read()

        # Holds result decoded data
        decoded_data = ""

        # Put every code in array by spliting space char
        code_arr = [int(i, base=16) for i in compressed_data.split(" ")]
        if len(code_arr) == 0:
            # No data in the file was found
            return -1

        # Set code_dict corresponding to code type
        if code_type == "base10":
            code_dict = {i: chr(i) for i in range(bit_size)}
        else:
            return -1

        # Handle first code and remove it from array
        prev = code_arr.pop(0)
        decoded_data = code_dict[prev]
        hold = code_dict[prev]
        count = bit_size

        for code in code_arr:
            if code in code_dict:
                # Code is in dict
                decoded_data += code_dict[code]
                hold = code_dict[code][0]
            else:
                # Code is not in dict
                decoded_data += code_dict[prev] + hold
                hold = code_dict[prev][0]

            code_dict[count] = code_dict[prev] + hold
            count += 1
            prev = code

        # Write decoded data to output file
        with open(output_file_name, "w", encoding="utf-8") as o:
            o.write(decoded_data)            

    return 1