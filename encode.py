from baseChange import b10_2_b32, b10_2_b64, b10_2_b128, b10_2_b256


# This function encodes the file
def encode(file_name, output_name, encoding, base_value):
    compressed_string = ""
    curr = 0
    if encoding == "utf-8":
        dict_num = 255
    else:
        dict_num = 65534
    

    #read the text that is going to be compressed
    with open(file_name, encoding=encoding) as file:
        string_to_compress = file.read()

    length = len(string_to_compress)
    if length == 0:
        return -1

    #generate dictionary by initializing it first to ascii
    encoding_dict = {chr(i) : i for i in range(dict_num + 1)}

    common_words = []
    with open("./mostCommonWords.txt", encoding="utf-8") as file:
        common_words = file.readlines()
    for l in common_words:
        encoding_dict[l[:-1]] = dict_num + 1
        dict_num += 1

    p = string_to_compress[curr]
    
    while curr < (length - 1):
        curr += 1
        c = string_to_compress[curr]
        if p + c in encoding_dict:
            p = p + c
            if curr == (length - 1):
                if base_value == 10:
                    compressed_string += (str(encoding_dict[p]) + " ")
                elif base_value == 16:
                    compressed_string += (str(format(encoding_dict[p], 'x')) + " ")
                elif base_value == 32:
                    compressed_string += (str(b10_2_b32(encoding_dict[p])) + " ")
                elif base_value == 64:
                    compressed_string += (str(b10_2_b64(encoding_dict[p])) + " ")
                elif base_value == 128:
                    compressed_string += (str(b10_2_b128(encoding_dict[p])) + " ")
                elif base_value == 256:
                    compressed_string += (str(b10_2_b256(encoding_dict[p])) + " ")
        else:
            # Encode based on the base_value
            if base_value == 10:
                compressed_string += (str(encoding_dict[p]) + " ")
            elif base_value == 16:
                compressed_string += (str(format(encoding_dict[p], 'x')) + " ")
            elif base_value == 32:
                compressed_string += (str(b10_2_b32(encoding_dict[p])) + " ")
            elif base_value == 64:
                compressed_string += (str(b10_2_b64(encoding_dict[p])) + " ")
            elif base_value == 128:
                compressed_string += (str(b10_2_b128(encoding_dict[p])) + " ")
            elif base_value == 256:
                compressed_string += (str(b10_2_b256(encoding_dict[p])) + " ")

            encoding_dict[p + c] = dict_num + 1
            dict_num += 1
            p = c
            if curr == (length - 1):
                if base_value == 10:
                    compressed_string += (str(encoding_dict[c]) + " ")
                elif base_value == 16:
                    compressed_string += (str(format(encoding_dict[c], 'x')) + " ")
                elif base_value == 32:
                    compressed_string += (str(b10_2_b32(encoding_dict[c])) + " ")
                elif base_value == 64:
                    compressed_string += (str(b10_2_b64(encoding_dict[c])) + " ")
                elif base_value == 128:
                    compressed_string += (str(b10_2_b128(encoding_dict[p])) + " ")
                elif base_value == 256:
                    compressed_string += (str(b10_2_b256(encoding_dict[p])) + " ")

    
    
    compressed_string = compressed_string[:-1]
    with open(output_name, "w", encoding=encoding) as output:
        output.write(compressed_string)

    return 1
