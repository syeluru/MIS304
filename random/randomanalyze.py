def check(name_of_file, list_of_words):
    infile = open(name_of_file, 'r')
    text = []
    for line in infile:
        line = line.rstrip('\n')
        text.append(line.split())

    for i in range(len(text)):
        for j in range(len(text[i])):
            for k in range(len(list_of_words)):
                if list_of_words[k] == text[i][j]:
                    return False

    return (True)

def main():
    yes = check("random.txt", ['yo', 'true'])
    print (yes)
main()
