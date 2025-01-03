#problem 187 LC

#Repeated DNA Sequences
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        #simple approach is, we use a set() to store 10-character long substrings, which have key value 2 or more
        #then finally return the set() as an array TC: O (n)

        #2 sets
        seen, result = set(), set()

        for L in range(len(s)-9):
            current = s[L:L + 10]
            #if a string is seen already, it would add to result
            if current in seen:
                result.add(current)

            #if not seen , it would be added to seen
            seen.add(current)
        return list(result)

