# We are going to learn file handling in python?

# opening a file
f = open('file.txt','r')
# print(f)
# text = f.read()
# print(text)
# f.close()

# file opening mode.

# r = read  default mode
# w = write
# a = append
# x = create a file

# Writing data in a file

f.open('file.txt','w')
f.write("Hello World!")
f.close()

