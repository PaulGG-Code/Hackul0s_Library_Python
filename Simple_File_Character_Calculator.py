#open file in read mode
file = open("D:\data.txt", "r")

#read the content of file
data = file.read()

#get the length of the data
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)
