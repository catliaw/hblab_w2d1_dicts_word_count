#!/usr/bin/python
from sys import argv
script, filename = argv

# OUR PSEUDOCODE
# Open text file
# create empty dictionary
# loop over the text file line by line
# split each line into a list separated by space
# count words
# if space, continue
# else count words

def get_word_count(file_name):
    """Function counts number of times a word appears in a file

    Takes file name argument on the command line following the script name

    """
    
    my_file = open(file_name)
    word_count = {}

    for line in my_file:
        stripped_line = line.rstrip()
        line_list = stripped_line.split(' ')

        for word in line_list:
            word_count[word] = word_count.get(word, 0) + 1

    for word_in_count, count in word_count.iteritems():
        print "{} {}".format(word_in_count, count)

    my_file.close()
    # return word_count

get_word_count(filename)
# print "\n******************************\n"
# get_word_count("twain.txt")