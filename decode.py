from baseChange import b32_2_b10, b64_2_b10, b128_2_b10, b256_2_b10


# This function decodes the file
def decode(file_name, output_file_name, encoding, base_value):
    # This variable holds main dict used for decoding
    code_dict = {}
    if encoding == "utf-8":
        bit_size = 256
    else:
        bit_size = 65535

    # Read file to decode
    with open(file_name, 'r', encoding=encoding) as f:
        # Read every line at once
        compressed_data = f.read()

        # Holds result decoded data
        decoded_data = ""

        # Put every code in array by spliting space char
        code_arr = []
        if base_value == 10 or base_value == 16:
            code_arr = [int(i, base=base_value) for i in compressed_data.split(" ")]
        elif base_value == 32:
            code_arr = [b32_2_b10(i) for i in compressed_data.split(" ")]
        elif base_value == 64:
            code_arr = [b64_2_b10(i) for i in compressed_data.split(" ")]
        elif base_value == 128:
            code_arr = [b128_2_b10(i) for i in compressed_data.split(" ")]
        elif base_value == 256:
            code_arr = [b256_2_b10(i) for i in compressed_data.split(" ")]
        else:
            return -1
            
        if len(code_arr) == 0:
            # No data in the file was found
            return -1

        # Set code_dict corresponding to code type
        code_dict = {i: chr(i) for i in range(bit_size)}
        # Handle and set common words in code dict
        common_words = []
        with open("./mostCommonWords.txt", encoding="utf-8") as c_f:
            common_words = c_f.readlines()
        for i, cw in enumerate(common_words):
            code_dict[bit_size + i] = cw[:-1]

        # Handle first code and remove it from array
        prev = code_arr.pop(0)
        decoded_data = code_dict[prev]
        hold = code_dict[prev]
        count = bit_size + len(common_words)
        # print(decoded_data)
        for code in code_arr:
            if code in code_dict:
                # Code is in dict
                decoded_data += code_dict[code]
                hold = code_dict[code][0]
            else:
                # Code is not in dict
                decoded_data += code_dict[prev] + hold
                # print(decoded_data)
                hold = code_dict[prev][0]

            code_dict[count] = code_dict[prev] + hold
            count += 1
            prev = code

        # Write decoded data to output file
        with open(output_file_name, "w", encoding=encoding) as o:
            o.write(decoded_data)            

    return 1