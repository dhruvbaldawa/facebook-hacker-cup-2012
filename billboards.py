"""
We are starting preparations for Hacker Cup 2013 really early. Our first step is to prepare billboards to advertise the contest. We have text for hundreds of billboards, but we need your help to design them.

The billboards are of different sizes, but are all rectangular. The billboard widths and heights are all integers. We will supply you with the size in inches and the text we want printed. We want you to tell us how large we can print the text, such that it fits on the billboard without splitting any words across lines. Since this is to attract hackers like yourself, we will use a monospace font, meaning that all characters are of the same width (e.g.. 'l' and 'm' take up the same horizontal space, as do space characters). The characters in our font are of equal width and height, and there will be no additional spacing between adjacent characters or adjacent rows.

Let's say we want to print the text "Facebook Hacker Cup 2013" on a 350x100" billboard. If we use a font size of 33" per character, then we can print "Facebook" on the first line, "Hacker Cup" on the second and "2013" on the third. The widest of the three lines is "Hacker Cup", which is 330" wide. There are three lines, so the total height is 99". We cannot go any larger.

Input
The first line of the input file contains a single integer T: the number of test cases. T lines follow, each representing a single test case in the form "W H S". W and H are the width and height in inches of the available space. S is the text to be written.

Output
Output T lines, one for each test case. For each case, output "Case #t: s", where t is the test case number (starting from 1) and s is the maximum font size, in inches per character, we can use. The size must be an integral number of inches. If the text does not fit when printed at a size of 1", then output 0.

Constraints
1 <= T <= 20
1 <= W, H <= 1000
The text will contain only lower-case letters a-z, upper-case letters A-Z, digits 0-9 and the space character
The text will not start or end with the space character, and will never contain two adjacent space characters
The text in each case contains at most 1000 characters
"""
import sys
import re
def parse_file():
    lines = open(sys.argv[1]).read()
    for line in lines.splitlines():
        yield line
    
if __name__ == '__main__':
    index = -1
    expr = re.compile(r'[A-Za-z0-9 ]')
    for line in parse_file():
        if index == -1:
            T = int(line)
            assert T >= 1 and T <= 20
            index += 1
            continue
        
        assert expr.match(line)
        assert len(line) >= 1 and len(line) <= 1000
        
        fragments = line.split()
        w,h,s = fragments[0], fragments[1], fragments[2:]
        
        # Process
        w = int(w)
        h = int(h)
        #font_width = w/len(s[0]
        #max_font = font_width
        sizes = []
        for f_width in range(1, w):
            l = []
            line_width = w/f_width
            space_left = line_width
            for word in s:
                if f_width * len(s) > space_left:
                    l.append(word)
                    space_left = line_width - (len(s) * f_width)
                else:
                    try:
                        e = l.pop() + " " + word
                        l.append(e)
                        space_left = space_left - ((len(s) + 1) * f_width)
                    except:
                        l.append(word)
                        space_left = space_left - (len(s) * f_width)
                
            max_w = len(max(l, key=len)) * f_width
            max_h = len(l) * f_width
            if max_w <= w and max_h <= h:
                sizes.append(f_width)
        
        index += 1
        print "Case #%s: %s" % (index, max(sizes))
    pass
