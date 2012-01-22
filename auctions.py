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
1 <= N <= 10^18
1 <= M, K <= 10^7
1 <= P1 <= M
1 <= W_1 <= K
0 <= A,B,C,D <= 10^9
"""
import sys
from collections import Counter
import profile
def preference(P, W, i, j):
    if (P[i] < P[j] and W[i] <= W[j]) or (P[i] <= P[j] and W[i] < W[j]):
        return i
    else:
        return j

def gcd(a,b):
  if not b == 0:
     return gcd(b,a%b)
  else:
     return a

def lcm(a,b):
  return a*(b/gcd(a,b))

def get_period(N, P1, W1, M, K, A, B, C, D):
    P = [P1]
    W = [W1]
    r_W = False
    r_P = False
    
    k = max(M,K)
    n = 1
    while n < k:
        P_t = (((A*P[n-1] + B) % M) + 1)
        W_t = (((C*W[n-1] + D) % K) + 1)
        if W_t == W1:
            #print "W_t:",n
            r_W = n
        if P_t == P1:
            #print "P_t:",n
            r_P = n
        if r_W and r_P:
            k = lcm(r_W, r_P)+1 if k < N and N/k != 0 else N
        P.append(P_t)
        W.append(W_t)
        n += 1               
    return P,W,k

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
        P, W, k = get_period(N, P1, W1, M, K, A, B, C, D)
        print "Done. Get Period"
        bargain = 0
        t_deal = 0
        bargain_index = []
        t_deal_index = []
               
        preferred = Counter()
        n_preferred = Counter()
        k = min(N, k)
        for i in xrange(k):
            if i % 100000 == 0:
                print i,"done"
            for j in xrange(i+1,k):
                if preference(P,W,i,j) == i and preference(P,W,j,i) == i:
                    preferred[i] += 1
                    n_preferred[j] += 1
                elif preference(P,W,i,j) == j and preference(P,W,j,i) == j:
                    n_preferred[i] += 1
                    preferred[j] += 1
                else:
                    #print i,j
                    preferred[i] += 1
                    n_preferred[i] += 1
                    preferred[j] += 1
                    n_preferred[j] += 1        
            
            if preferred[i] == k-1:
                #print "Bargain: ",i
                #raw_input("Continue...")
                bargain += 1
                bargain_index.append(i)
            
            if n_preferred[i] == k-1:
                #print "Terrible Deal: ",i
                #raw_input("Continue...")
                t_deal += 1
                t_deal_index.append(i)
        
        if k < N and N/k != 0:
            t_deal *= N/k
            bargain *= N/k
        
        for x in bargain_index:
            if x < N%k:
                bargain += 1
            else:
                break
                
        for x in t_deal_index:
            if x < N%k:
                t_deal += 1
            else:
                break
        
        #print P, W, k, preferred, n_preferred
        #Process END
        index += 1
        print "Case #%s: %s %s" % (index, t_deal, bargain)
    pass
