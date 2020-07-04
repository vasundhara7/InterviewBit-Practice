# Given a list of non negative integers, arrange them such that they form the largest number.

# For example:

# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        new=''
        ext=[]
        
        l=len(str(max(A)))+1
        
        for i in A:
            a=str(i)*l
            ext.append((a[:l],i))
        
        ext=sorted(ext,reverse=True)
        for i in range(len(ext)):
            new+=str(ext[i][1])
        if int(new)==0:
            return 0
        return new
