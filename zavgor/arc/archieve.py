def archieve():    
    with open("input.txt", "r") as f:
        text = f.read()

    punctuation = {'.', ',', ';', ':', '!', '?'}
    output = ''
    skip_space = False

    for char in text:
        if skip_space:
            if char != ' ':
                output += char
                skip_space = False
        else:
            if char in punctuation:
                skip_space = True
                output += char
            elif char != ' ':
                output += char

    with open("output.txt", "w") as f:
        f.write(output)
        
def dearchieve():
    with open('output.txt', 'r') as file:
        text = file.read()

    text_with_spaces = ''
    for char in text:
        if char in ['.', ',', ':', ';', '!', '?']:
         text_with_spaces += char + ' '
        else:
            text_with_spaces += char

    with open('outputtt.txt', 'w') as file:
        file.write(text_with_spaces)