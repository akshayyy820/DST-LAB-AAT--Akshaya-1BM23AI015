#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    
    st = []
    
    
    m_b = {')': '(', ']': '[', '}': '{'}
    
    
    for i in s:
        if i in '({[':
            
            st.append(i)
        elif i in ')}]':
            
            if st and st[-1] == m_b[i]:
                
                st.pop()
            else:
                
                return "NO"
    
    
    return "YES" if not st else "NO"              
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
