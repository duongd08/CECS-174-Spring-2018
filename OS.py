import os

print(os.name) # gives the name of the operating system dependent module imported

print() 

print(os.getlogin()) # gets the name of the user name log in

print()

print(os.getpid()) # gets the current process id

print()

print(os.getppid()) # gets the parent's process id

print()

print(os.getcwd()) # gets the current working directory

print()

print(os.listdir())# gets all the current files in the code's directory

print()

# try catch exception

try:

    filename = "Students.cpp"
    f = open(filename, "rU")
    text = f.read()
    f.close()


except IOError:
    print("Problem reading: " + filename)


