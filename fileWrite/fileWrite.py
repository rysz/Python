#r = read
#w = write mode (will overwrite if already exists)
#a = append 

#read the entire file
with open("fileRead.txt", "r") as my_file_read:
    with open("fileWrite.txt", "w") as my_file_write:
        for line in my_file_read:
            my_file_write.write(line)