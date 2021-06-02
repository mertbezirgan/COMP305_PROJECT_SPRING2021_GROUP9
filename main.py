import timeit
import sys
import getopt
from encode import encode
from decode import decode


if __name__ == "__main__":
    # Handle passed arguments
    # <method> <input_file_name> <encoding> <output_file_name> <base_value> <recursive>
    arg_dict = {
        # Initiliaze with default values
        "base_value": 10,
        "recursive": False,
        "encoding": "utf-8",
    }
    argumentList = sys.argv[1:]
    # Options
    options = "b:r"
    # Long options
    long_options = ["base =", "recursive"]
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # Checking each argument with options
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-b", "--base"):
                arg_dict["base_value"] = int(currentValue)
            elif currentArgument in ("-r", "--recursive"):
                arg_dict["recursive"] = True

        # Check rest of the arguments
        if len(values) < 4:
            raise getopt.error("Required arguments were not given correctly")
        arg_dict["method"] = values[0]
        arg_dict["input_file_name"] = values[1]
        arg_dict["encoding"] = values[2]
        arg_dict["output_file_name"] = values[3]

        # Call method with arguments passed as parameters
        if arg_dict["method"] == "encode":
            result = encode(
                file_name=arg_dict["input_file_name"],
                output_name=arg_dict["output_file_name"],
                encoding=arg_dict["encoding"],
                base_value=arg_dict["base_value"]
            )
        elif arg_dict["method"] == "decode":
            result = decode(
                file_name=arg_dict["input_file_name"],
                output_file_name=arg_dict["output_file_name"],
                encoding=arg_dict["encoding"],
                base_value=arg_dict["base_value"]
            )
        else:
            # Invalid method was given
            raise getopt.error("Invalid method was given, enter 'encode' or 'decode' in the arguments")
        
        if result == -1:
            # Operation failed
            raise Exception()
        else:
            # Operation successful
            print("Operation successful")

    # Output error, and return
    except getopt.error as err:
        print(str(err))
    except Exception as err:
        print(str(err))
        print("An error has occurred")
        
