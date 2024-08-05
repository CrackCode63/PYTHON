import matplotlib.pyplot as plt
# In this matplotlib is a library and pyplot a class of matplotlib.
x = [1,2,3,4]
y = [2,4,6,8]

plt.bar(x,y)

plt.show()

# Here show() fun is used to display the graphs.

# Here are going to design the graphs

c = ["red","green","yellow","blue"]
# We can also use this.
# c = ["r","g","y","b"]
plt.bar(x,y,color= c)
plt.show()

# Here we are going to give the label(title) to the graphs
# In this label we can change the font size of the labels by using fontsize keyword.
plt.xlabel("baby", fontsize = 30)
plt.ylabel("bachha")
plt.title("Matplotlib")
plt.bar(x,y, color= c)
plt.show()
