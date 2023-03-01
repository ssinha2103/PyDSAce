import os


def print_():
    # Set the output file name and open the file for writing
    output_file = "output.txt"
    with open(output_file, "w") as f_out:
        # Loop through all the files in the current directory
        for file_name in os.listdir("."):

            # Only consider Python files other than main.py
            if file_name.endswith(".py") and file_name != "main.py":

                # Print the file name to the output file
                f_out.write(f"\n\n# --- {file_name} ---\n\n")

                # Open the file for reading
                with open(file_name, "r") as f_in:

                    # Loop through each line in the file
                    for line in f_in:
                        # Write the line to the output file
                        f_out.write(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_()
