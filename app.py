import sys
import SecurePass as sp
import InjectPassword as ip

"""CAUTION: Saving a password anywhere is compromising. However, if you need to do it make it a tiny bit harder to spot.
Once your .jpg of choice is injected move it out of the programs directory to a secure/secret location.
"""

"""NOTE: new_password is generated based off of 3 parameters, length, symbols, and uppercase.
   For strongest results generate a password with a length that is the maximum the platform allows,
   use symbols and add uppercase letters."""


def password_generator():
    # TODO(Add file parameter argument to cmd)

    # Add any .jpg to root directory,
    base_image = 'images/palletcleanser.jpg'  # image to be changed
    output_image = 'output.jpg'  # The password injected image.

    # Default parameters
    length = 20
    symbols = True
    uppercase = True
    accepted_commands = ['-h', '-l', '-s', '-u']

    line_border = '*************************************************'

    """NOTE: new_password is generated based off of 3 parameters, length, symbols, and uppercase.
    For strongest results generate a password with a length that is the maximum the platform allows,
    use symbols and add uppercase letters."""

    # Default if no arguments given
    if len(sys.argv) == 1:
        print(f"{line_border}\nParameters:default")
        print("$PASSWORD GENERATION$")

        # Password is generated with 20 chars, including symbols, and uppercase letters
        new_password = sp.create_password(length, symbols, uppercase)
        print(f'New password with default parameters- \nPassword: {new_password}')
        print(line_border)

        print("$IMAGE CREATION$")
        print(f"Injecting {base_image}...\nNew image found at {output_image}")
        # baseimage is copied then injected with new_password in the root directory
        ip.hide_secret(base_image, output_image, new_password)
        print(line_border)

    # If parameters entered in commandline
    if len(sys.argv) > 1:
        print("$PASSWORD GENERATION$")
        print(f"{line_border}\nParameters:edited")
        # Iterates through sys.argv skipping initial argument
        for num in range(1, len(sys.argv)):
            args = sys.argv[num]

            if args not in accepted_commands:
                print(f"Sorry '{args}' is not valid command, use '-h' for command help!\n{line_border}")

                return

            # TODO: Create help parameter
            if args == '-h':
                print("TODO:Command help section")
                return

            if args == "-l":
                length_input = ""
                while not length_input.isdigit():
                    length_input = input("Enter password length as positive integer:")

                length = int(length_input)
                print(f"Password length set to {length}.")

            if args == "-s":
                symbols = False
                print(f"Symbols set to false.")

            if args == "-u":
                uppercase = False
                print(f"Uppercase letters set to false.")

        new_password = sp.create_password(length, symbols, uppercase)
        print(f'Generated password based on parameters provided-\nPassword: {new_password}\n')
        print(line_border)

        print("$IMAGE CREATION$")
        print(f"Injecting {base_image}...\nNew image found at '{output_image}'")
        ip.hide_secret(base_image, output_image, new_password)
        print(line_border)


# TODO: Add '-r' to allow 'find_hidden from command line
# find_hidden reads the bytes of the .jpg file and looks for hidden text.
# ip.find_hidden('output.jpg')

if __name__ == "__main__":
    password_generator()
