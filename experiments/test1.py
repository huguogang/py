'''
Created on Jan 6, 2016

@author: huguogang
'''
import unittest
# from test.test_deque import fail


class Test1(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testFunctionName(self):
        def containsSkip (name):
            return ('skip' in name or 'Skip' in name)
        
        allFunctions = dir(unittest)
        
        print 'all functions in unittest'
        print allFunctions
        print
        print 'functions in unittest that contains skip'
        print filter(containsSkip, allFunctions)
        pass

    def testDictionary(self):
        key1 = {
                "a": 1,
                "b": 2
        }
        key2 = {
                "c": 3,
                "d": 4,
                5: "five",
                # tuple can be key, immutable
                (1, 'a'): "tuple as key"
                # list is mutable, cannot be key, runtime error
                # [1, 'a']: "list as key"
        }
        key2["d"] = 5
        key2.pop("c")
        print key2
        key2.pop((1, 'a'));
        # Error, cannot pop keys that does not exist
        # key2.pop("no such key")
        print key2
        # won't run, key is not hashable
        # dictUsingDictKey = {
        #         key1: "key1's value",
        #         key2: "key2's value"
        # }
        # self.fail('test fail')
        print key2["a new key"]
        
    def testTuple(self):
        print '--  Test Tuple'
        print (1, 'a') is (1, 'a') # False
        t = (1, 'a')
        t1 = t
        print t is t1 # True
        # error, tuple is immutable t[1] = 'b'

    def testList(self):
        print '-- test list'
        l = [1, '2', 3]
        
        print l[-1] # index for the last one
        print l[-2] # index for second from the last one
        
        l[1] = "new 1"
        print l[1]
        
        print l[1:30] # extra indices are ignored here
        
        print l[0:0] # nothing
        print l[0:len(l)] # all
        print l[0:-1]
        print l[0:-2]
        print l[0:-5] # nothing
        print l[0:len(l):2]
        
    def testClass(self):
        class InnerClass():
            print 'inner class'
            sharedData = 100
            def method(self):
                """Document string
                line 2
                line 3
                """
                print self

        print '-- test class'
        print InnerClass.method.__doc__
        instance = InnerClass()
        print InnerClass
        print instance
        print instance.method()
        
        def dynamicMethod(self):
            self.instanceData = 1
            print "inside the dynamic method"
            print self
            
        # modify class def
        # does not work InnerClass["method"] = dynamicMethod
        InnerClass.method = dynamicMethod
        newInstance = InnerClass()
        print newInstance.method()

        # add a new method
        InnerClass.newMethod = dynamicMethod
        # notice newInstance was created before the class is modified
        print newInstance.newMethod()
        
        # add new data to instance
        newInstance.newData = 1000
        print newInstance.newData
        
        # this also works
        newInstance.method = "replace existing method with a string"
        print newInstance.method
        
        # shared data is shared among all instances
        print newInstance.sharedData    # 100
        instance.sharedData = 1
        print newInstance.sharedData    # 100
        print instance.sharedData       # 1
        
        InnerClass.sharedData = 1
        print newInstance.sharedData    # 1
        print instance.sharedData       # 1
        
    def testLambda(self):
        print "-- test lambda"
        # (3) is a integer, (3, ) is a Tuple with one element
        pairs = [(1, 'one', 3), (2, 'two'), (3,), (4, 'four')]
        pairs.sort(key=lambda pair: len(pair))
        print pairs
        
    def testMisc(self):
        print "--miscellaneous tests"
        number = 1
        ++number
        print number    # 1
        print ++number  # 1
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()