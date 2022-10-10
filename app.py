import SecurePass as sp
import InjectPassword as ip

"""CAUTION: Saving a password anywhere is compromising. However, if you need to do it make it a tiny bit harder to spot.
Once your .jpg of choice is injected move it out of the programs directory to a secure/secret location.
"""


def main():
    # Add any .jpg to root directory
    base_image = 'images/palletcleanser.jpg'  # image to be changed
    output_image = 'output.jpg'  # The password injected image.

    """NOTE: new_password is generated based off of 3 parameters, length, symbols, and uppercase.
    For strongest results generate a password with a length that is the maximum the platform allows,
    use symbols and add uppercase letters."""
    new_password = sp.create_password(length=20, symbols=True, uppercase=True)
    print(new_password)
    # baseimage is copied then injected with new_password in the root directory
    ip.hide_secret(base_image, output_image, new_password)

    # find_hidden reads the bytes of the .jpg file and looks for hidden text.
    ip.find_hidden('output.jpg')


if __name__ == "__main__":
    main()
