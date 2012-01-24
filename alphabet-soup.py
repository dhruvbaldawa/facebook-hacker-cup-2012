"""
ALPHABET SOUP
Alfredo Spaghetti really likes soup, especially when it contains alphabet pasta. Every day he constructs a sentence from letters, places the letters into a bowl of broth and enjoys delicious alphabet soup.

Today, after constructing the sentence, Alfredo remembered that the Facebook Hacker Cup starts today! Thus, he decided to construct the phrase "HACKERCUP". As he already added the letters to the broth, he is stuck with the letters he originally selected. Help Alfredo determine how many times he can place the word "HACKERCUP" side-by-side using the letters in his soup.

Input
The first line of the input file contains a single integer T: the number of test cases. T lines follow, each representing a single test case with a sequence of upper-case letters and spaces: the original sentence Alfredo constructed.

Output
Output T lines, one for each test case. For each case, output "Case #t: n", where t is the test case number (starting from 1) and n is the number of times the word "HACKERCUP" can be placed side-by-side using the letters from the sentence.

Constraints
1 < T < 20
Sentences contain only the upper-case letters A-Z and the space character
Each sentence contains at least one letter, and contains at most 1000 characters, including spaces
"""
from collections import Counter
import sys
import re
def parse_file():
    lines = open(sys.argv[1]).read()
    for line in lines.splitlines():
        yield line
    
if __name__ == '__main__':
    sentence = "HACKERCUP"
    index = -1
    expr = re.compile(r'[A-Z ]')
    for line in parse_file():
        if index == -1:
            T = int(line)
            assert T > 1 and T <= 20
            index += 1
            continue
        
        assert expr.match(line)
        assert len(sentence) >= 1 and len(sentence) <= 1000
        
        c = Counter(line)
        d = Counter(sentence)
        min_ = c[sentence[0]]/d[sentence[0]]
        for letter in sentence:
            if c[letter]/d[letter] < min_:
                min_ = c[letter]
        index += 1
        print "Case #%s: %s" % (index, min_)
    pass
