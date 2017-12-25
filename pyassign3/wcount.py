"""wcount.py: count words from an Internet file.

__author__ = "Ai Yuyang"
__pkuid__  = "1700011721"
__email__  = "aiyuyang@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

def wcount(lines, topn = 10):
    temp = ''
    for line in lines:
        line = line.decode('gbk','ignore')
        line = ''.join([ch for ch in line.lower() if ord(ch) == 32 or (ord(ch) > 96 and ord(ch) < 123)])
        temp += line + ' '
    wordlist = temp.split()
    result = []
    allword = set({})
    for word in wordlist:
        allword.add(word)
    for word in allword:
        n = 0
        for word0 in wordlist:
            if word0 == word:
                n += 1
        result.append((n, word))
    result.sort(reverse = True)
    for (times, word) in result:
        if result.index((times, word)) < topn:
            print(word, str(times).rjust(15 - len(word)))
            
pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as lines:
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
   
            
    
