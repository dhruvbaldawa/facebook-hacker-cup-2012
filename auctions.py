"""
ALPHABET SOUP
You have encountered a new fancy online auction that offers lots of products. You are only interested in their price and weight. We shall say that product A is strictly preferred over product B if A costs less than B and is not heavier (they may be of equal weight) or if A weighs less and is not more expensive (they can have equal price).

We shall call a product A a bargain if there is no product B such that B is better than A. Similarly, we shall call a product C a terrible deal if there exists no product D such that C is better than D. Note that according to our definitions, the same product may be both a bargain and a terrible deal! Only wacky auctioneers sell such products though.

One day you wonder how many terrible deals and bargains are offered. The number of products, N, is too large for your human-sized brain though. Fortunately, you discovered that the auction manager is terribly lazy and decided to sell the products based on a very simple pseudo-random number generator.

If product i has price Pi and weight Wi, then the following holds for product i+1:

Pi = ((A*Pi-1 + B) mod M) + 1 (for all i = 2..N)
Wi = ((C*Wi-1 + D) mod K) + 1 (for all i = 2..N)
You carefully calculated the parameters for the generator (P1, W1, M, K, A, B, C and D). Now you want to calculate the number of terrible deals and bargains on the site.

Input
The first line of the input file contains a single integer T: the number of test cases. T lines follow, each representing a single test case with 9 space-separated integers: N, P1, W1, M, K, A, B, C and D.

Output
Output T lines, one for each test case. For each case, output "Case #t: a b", where t is the test case number (starting from 1), a is the number of terrible deals and b is the number of bargains.

Constraints
1 <= T <= 20
1 <= N <= 1018
1 <= M, K <= 107
1 <= P1 <= M
1 <= W_1 <= K
0 <= A,B,C,D <= 109
"""
import sys
def preference(P, W, i, j):
    if (P[i] < P[j] and W[i] <= W[j]) or (P[i] <= P[j] and W[i] < W[j]):
        return i
    else:
        return j

def parse_file():
    lines = open(sys.argv[1]).read()
    for line in lines.splitlines():
        yield line
    
if __name__ == '__main__':
    index = -1

    for line in parse_file():
        if index == -1:
            T = int(line)
            assert T > 1 and T <= 20
            index += 1
            continue
        
        #Process
        N, P1, W1, M, K, A, B, C, D = (int(x) for x in line.split())
        P = [P1]
        W = [W1]
        for i in range(1, N):
            P.append(((A*P[i-1] + B) % M) + 1)
            W.append(((C*W[i-1] + D) % K) + 1)
        
        bargain = 0
        t_deal = 0
        
        #print P, W
        for i in range(N):
            preferred = 0
            n_preferred = 0
            for j in range(N):
                if i == j:
                    continue
                
                if preference(P,W,i,j) == i and preference(P,W,j,i) == i:
                    preferred += 1
                elif preference(P,W,i,j) == j and preference(P,W,j,i) == j:
                    n_preferred += 1
                else:
                    #print i,j
                    preferred += 1
                    n_preferred += 1        
            
            if preferred == N-1:
                #print "Bargain: ",i
                bargain += 1
            
            if n_preferred == N-1:
                #print "Terrible Deal: ",i
                t_deal += 1
                
        #Process END
        index += 1
        print "Case #%s: %s %s" % (index, t_deal, bargain)
    pass
