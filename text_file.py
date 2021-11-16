# this function open and read file,split and return some word as list from txt file
def text_list(text):
    with open(text, 'r') as reader:
        line = reader.readlines()[-1]
    line_list = line.split(",")
    return line_list[:5]


print(text_list(text='sample2.txt'))
