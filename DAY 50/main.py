# Other methods of file handling.

# readline() method
# The readline() method in Python reads a line from a file. It returns a string containing the text from the line, and the file pointer is left pointing to the next line.

f = open('file.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


# writelines() method
# The writelines() method in Python writes a list of lines to a file. It does not automatically append a newline character to the end of each line, so you need to include the newline character in each string.

f = open('file2.txt','w')
lines = ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()