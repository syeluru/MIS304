# Program to compute average number of words per sentence

def main():
    # Define variables
    num_sentences = 0
    total_words = 0
    average_words = 0.0
    word_list = []

    try:
        # Open file for input
        infile = open("textwordcount.txt", 'r')

        # Read data from the input file
        # into a list of lines
        # #ach element in sentence_list is a line
        sentence_list = infile.readlines()

        num_sentences = len(sentence_list)

        for sentence in sentence_list:
            word_list = sentence.split()
            total_words += len(word_list)

        # Calculate average words
        average_words = total_words/num_sentences

        # Display output
        print ("Average number of words per sentence: %s" % average_words)

        # Close input file
        infile.close()
    except IOError:
        print ("Error opening the file")

main()
