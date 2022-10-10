import shutil


def hide_secret(original, output, data: str):
    shutil.copyfile(original, output)
    # Appends 'data' parameter to end of .jpg file
    with open(output, 'ab') as jpg:
        byte_data = data.encode()
        jpg.write(byte_data)

# 'find_hidden' prints anything after the last byte of a .jpg
def find_hidden(file):
    with open(file, 'rb') as jpg:
        content = jpg.read()
        offset = content.index(b'\xff\xd9')
        data = content[offset + 2:].decode()
        print(data)
