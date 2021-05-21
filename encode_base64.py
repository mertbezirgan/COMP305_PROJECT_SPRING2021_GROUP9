from baseChange import b10_2_b64
# This function encodes the file
def encode(file_name):
    encoding_dict = {}
    output_name = file_name.split(".")[0] + "_encodedBase64" + ".txt"
    string_to_compress = ""
    compressed_string = ""
    curr = 0
    length = 0
    dict_num = 255

    #read the text that is going to be compressed
    with open(file_name, encoding="utf-8") as file:
        string_to_compress = file.read()

    length = len(string_to_compress)

    #generate dictionary by initializing it first to ascii
    encoding_dict = {chr(i) : i for i in range(256)}

    p = string_to_compress[curr]
    
    while curr < (length - 1):
        curr += 1
        c = string_to_compress[curr]
        if p + c in encoding_dict:
            p = p + c
        else:
            compressed_string += (str(b10_2_b64(encoding_dict[p])) + " ")
            encoding_dict[p + c] = dict_num + 1
            dict_num += 1
            p = c
    compressed_string = compressed_string[:-1]
    output = open(output_name, "w")
    output.write(compressed_string)
    output.close()
    return 1
