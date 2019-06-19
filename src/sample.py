def hello_name(name: str):
    return 'Hello, {name}'.format(name=name)


def read_file(file_name):
    file = open(file_name)
    content = file.readline()
    return content
