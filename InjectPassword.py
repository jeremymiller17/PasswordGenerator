import shutil

from SecurePass import SecurePass


def hide_secret(original, output, data: str):
    shutil.copyfile(original, output)

    with open(output, 'ab') as jpg:
        byte_data = data.encode()
        jpg.write(byte_data)


def find_hidden(file):
    with open(file, 'rb') as jpg:
        content = jpg.read()
        offset = content.index(b'\xff\xd9')
        data = content[offset + 2:].decode()
        print(data)


# read_file_bytes('images/palletcleanser.jpg')

password = SecurePass()
hide_secret('images/palletcleanser.jpg', 'output.jpg',
            data=password.create_password(length=20, symbols=True, uppercase=True))
find_hidden('output.jpg')
