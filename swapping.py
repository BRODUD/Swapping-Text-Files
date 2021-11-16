def swapFileData() :
    file_1=input('Enter File Path: ')
    file_2=input('Enter Second File Path: ')
    with open(file_1, 'r') as a:
        data_a=a.read()
    with open(file_2, 'r') as b:
        data_b=b.read()
    with open(file_1, 'w') as a:
        a.write(data_b)
    with open(file_2, 'w') as b:
        b.write(data_a)
    print("Data A: ",data_a)
    print("Data B: ",data_b)

# File A - D:\Documents\school\jr\PRIVATE\swapping file\sample1.txt
# File B - D:\Documents\school\jr\PRIVATE\swapping file\sample2.txt

swapFileData()