#r = read
#w = write mode (will overwrite if already exists)
#a = append 

#read the entire file
with open("fileRead.txt", "r") as my_file_all:
    
    my_file_content = my_file_all.read()
    print("my_file_all.read(): \n\n", my_file_content)


#read set number of characters incrementally
with open("fileRead.txt", "r") as my_file_char:
    print()
    print("my_file_char.read(37): ", my_file_char.read(38))
    print("my_file_char.read(54): ", my_file_char.read(55))


#read line within the file
with open("fileRead.txt", "r") as my_file_line:
    print()
    print("my_file_line.readline(): ", my_file_line.readline())
    print("my_file_line.readline(): ", my_file_line.readline())

#loop and iterate through
with open("fileRead.txt", "r") as my_file_loop:
    print()
    i = 0
    for line in my_file_loop:
        print("Iteration", str(i), ":", line)
        i = i + 1