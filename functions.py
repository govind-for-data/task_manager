def read_file(filepath='list.txt'):
    with open('list.txt','r') as read_file:
        todos_local = read_file.readlines()
    return todos_local

def write_file(todos_arg, filepath='list.txt'):
    with open('list.txt','w') as write_file:
        write_file.writelines(todos_arg)
    