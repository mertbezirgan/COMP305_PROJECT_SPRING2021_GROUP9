
# This function encodes the file
def encode(file_name):
    encoding_dict = {}
    output_name = file_name.split(".")[0] + "_encoded" + ".txt"
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

    P = string_to_compress[curr]
    
    while curr < (length - 1):
        curr += 1
        C = string_to_compress[curr]
        if P + C in encoding_dict:
            P = P + C
        else:
            compressed_string += (str(encoding_dict[P]) + " ")
            encoding_dict[P + C] = dict_num + 1
            dict_num += 1
            P = C
    compressed_string = compressed_string[:-1]
    output = open(output_name, "w")
    output.write(compressed_string)
    output.close()
    return 1
