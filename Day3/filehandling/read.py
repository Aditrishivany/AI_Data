with open("data.txt","r") as file:
    #print(file.readline().strip())
    #print(file.readline().strip())
    #print(file.readline().strip())
    while True:
        line=file.readline()
        if not line:
            break
            print(line.strip())