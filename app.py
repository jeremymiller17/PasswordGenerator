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

    line_border = '*************************************************'

    """NOTE: new_password is generated based off of 3 parameters, length, symbols, and uppercase.
    For strongest results generate a password with a length that is the maximum the platform allows,
    use symbols and add uppercase letters."""

    # Default if no arguments given
    if len(sys.argv) == 1:

        print(f"{line_border}\nParameters:default\n")

        # Password is generated with 20 chars, including symbols, and uppercase letters
        new_password = sp.create_password(length, symbols, uppercase)
        print(f'New password with default parameters: \n{new_password}]n')
        # baseimage is copied then injected with new_password in the root directory
        ip.hide_secret(base_image, output_image, new_password)

    # If parameters entered in commandline
    if len(sys.argv) > 1:

        print(f"{line_border}\nParameters:edited\n")
        # Iterates through sys.argv skipping initial argument
        for num in range(1, len(sys.argv)):

            args = sys.argv[num]
            #TODO: Create help parameter
            if args == '-h':
                print("TODO:Command help section")
                return

            if args == "-l":
                length = int(input("Enter password length:"))
                print(f"Password length set to {length}.\n")

            if args == "-s":
                symbols = False
                print(f"Symbols set to false.\n")

            if args == "-u":
                uppercase = False
                print(f"Uppercase letters set to false.\n")

        new_password = sp.create_password(length, symbols, uppercase)
        print(f'Generated password based on parameters provided:\n{new_password}\n')

    print(line_border)

    ip.hide_secret(base_image, output_image, new_password)


# find_hidden reads the bytes of the .jpg file and looks for hidden text.
# ip.find_hidden('output.jpg')

if __name__ == "__main__":
    password_generator()
