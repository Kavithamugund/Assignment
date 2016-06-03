#!/usr/bin/python
import json

from bottle import  route, run
from collections import defaultdict


def load_dictionary():
    saved_dict = []
    dictionary = file('/usr/share/dict/american-english')
    for line in dictionary:
        saved_dict.append(line.strip())
    return saved_dict


def sort_string(input_str):
    return ''.join(sorted(input_str))

 
@route('/process_string/<input_strings>')
def process_string(input_strings):
    input_strings = [i.strip() for i in input_strings.split(',')]
    known_strings = load_dictionary()
    known_dict = defaultdict(list)
    for known_string in known_strings:
         known_dict[sort_string(known_string)].append(known_string)
         
    for input_string in input_strings:
        sorted_string = sort_string(input_string)
        if sorted_string in known_dict:
         # print "Possible Words for Scrambled Word %s = %s" % (input_string, known_dict[sorted_string])
          #anagrams=','.join(anagram)
          return "Possible anagrams for %s = %s" % (input_string,known_dict[sorted_string])

          #return anagrams
        else:
            return "No matches found for word %s" % (input_string) 
##    return "Possible anagrams for %s = %s" % (input_string,known_dict[sorted_string])

if __name__ == '__main__':
    run(host='0.0.0.0', port=8085, debug=True)
