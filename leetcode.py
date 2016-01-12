'''
Created on Jan 7, 2016

@author: huguogang
'''
import unittest

class LeetCode(unittest.TestCase):
    def maxDepth(self, root):
        """
        :type root: treenode
        :rtype: int
        """
        if(root is None): 
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        answer = triangle[-1] # start at the bottom row
        size = len(triangle)
        
        for rowIndex in range(size - 2, -1, -1): # from second to last row to top
            for colIndex in range(rowIndex + 1):
                answer[colIndex] = min(answer[colIndex], answer[colIndex + 1]) + triangle[rowIndex][colIndex]
        
        return answer[0]
        
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numberOfNonZeroes = 0 # count of number of non-zero numbers so far during scan
        for scanIndex in range(0, len(nums)):
            if(nums[scanIndex] != 0):
                if(scanIndex != numberOfNonZeroes):
                    nums[numberOfNonZeroes] = nums[scanIndex]
                    nums[scanIndex] = 0
                numberOfNonZeroes += 1
                
    def testIsAnagram(self):
        def isAnagram(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            def buildLookup(s):
                lookup = {}
                for c in s:
                    if c in lookup:
                        lookup[c] += 1
                    else:
                        lookup[c] = 1
                return lookup
            sLookup = buildLookup(s)
            tLookup = buildLookup(t)
            print sLookup
            print tLookup
            return sLookup == tLookup
        print isAnagram(self, "a", "b")
        
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n != 0 and n & (n - 1) == 0
    
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [0] * n
        for stepSize in range(1, n):
            for changes in range(stepSize - 1, n, stepSize):
                bulbs[changes] ^= 1
        return reduce(lambda count, bulb: count + bulb, bulbs)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()