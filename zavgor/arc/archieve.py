with open('X:\Programmes\hardhw\hardhw\zavgor\\arc\in.txt', 'r') as f_in:
    data = f_in.read()

compressed_data = ''
for char in data:
    if char in ['.', ',', '!', '?', ':', ';']:
        compressed_data += char + ''
    else:
        compressed_data += char

with open('X:\Programmes\hardhw\hardhw\zavgor\\arc\out.txt', 'w') as f_out:
    f_out.write(compressed_data)