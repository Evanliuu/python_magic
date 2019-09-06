import hashlib


def get_file_md5(path):
    with open(path, 'r') as file:
        data = file.read()

    diff_check = hashlib.md5()
    diff_check.update(data.encode())
    return diff_check.hexdigest()


if __name__ == '__main__':
    md5_code = get_file_md5(path=r'C:\Users\evaliu\Desktop\sample.txt')
    print(md5_code)
