def write_file(string, filename):
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()

def read_file(filename):
    myfile = open(filename, "r")
    contents = myfile.read()
    myfile.close()
    return contents

def read_file_v2(filename):
    with open(filename, "r") as myfile:
        return myfile.read()

def read_file_v3(filename):
    with open(filename, "r") as f:
        return f.readlines()

def read_file_v4(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

def read_preferences(filename):
    dictionary = {}
    with open(filename, "r") as f:
        for line in f:
            [username, artists] = line.strip().split(":")
            artistList = artists.split(",")
            dictionary[username] = artistList
    return dictionary
              
#write_file("Welcome to CS115\nhello All\nHow are you?", "test.txt")

#print(read_file("test.txt"))

#read_file_v4("test.txt")

