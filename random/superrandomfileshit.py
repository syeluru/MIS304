def main():
    infile = open('betterrrandom.txt', 'r')
    a = []
    b = infile.readline()
    print (b)
    #a.append(line.strip('\n'))
    print (a)

    outfile = open("writelines.txt", 'w')
    list = ['absc', 'dfasd', 'adfasdfas asdfasdf asd']
    for i in range(len(list)):
        outfile.write(list[i] + '\n')

main()
