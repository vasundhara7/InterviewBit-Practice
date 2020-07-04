# A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

# Input Format
# First argument is an integer array A containing arrival time of booking.
# Second argument is an integer array B containing departure time of booking.
# Third argument is an integer C denoting the count of rooms.

# Output Format
# Return True if there are enough rooms for N bookings else return False.
# Return 0/1 for C programs.

# Example Input
# Input 1:

#  A = [1, 3, 5]
#  B = [2, 6, 8]
#  C = 1

# Example Output
# Output 1:

#  0

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        li=[]
        i=0
        j=0
        arrive.sort()
        depart.sort()
        while j<len(depart) and i<len(arrive):
            if arrive[i]<depart[j]:
                li.append(str(arrive[i])+'a')
                i+=1
            elif arrive[i]>=depart[j]:
                li.append(str(depart[j])+'d')
                j+=1
        while i<len(arrive):
            li.append(str(arrive[i])+'a')
            i+=1
        while j<len(depart):
            li.append(str(depart[j])+'d')
            j+=1
            

        count=0
        for i in li:
            if i[-1]=='a':
                count+=1
            else:
                count-=1
            if count>K:
                return 0
        return 1
        
