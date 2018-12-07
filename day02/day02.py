
def testFunc1(a, b):
    print a, b

def testFunc2(a, b = "world"):
    print a, b

testFunc1("hello", "world!")
testFunc2("hello", b = "meghana")
testFunc2("hello")

def testFunc3(firstArg, *argsList, **argsDict):
    print "firstArg is", firstArg
    print "argsList is", argsList
    print "argsDict is", argsDict

def testFunc4(*posArgs):
    print "posArgs are", posArgs

def testFunc5(**kwArgs):
    print "kwArgs are", kwArgs

testFunc4("arg1", "arg2", "arg3")
testFunc5(arg1="arg1Value", arg2="arg2Value", arg3="arg3Value")
newDictionary = {'arg1': 'arg1Value', 'arg2': 'arg2Value'}
testFunc5(**newDictionary)

# this is a regular function
def thisIsARegularFunc(n):
    return n + 2

# prints 4 here
print thisIsARegularFunc(2)

def thisIsAnotherRegularFunc(n):
    return thisIsARegularFunc(n)

# this has lambda func in it
def thisIncludesLambda(n):
    # this is lambda
    return lambda x: x + n # func(x): return x + n

# fn is lambda x: x + 10 ==> func(x): return x + 10
fn = thisIncludesLambda(10)
# this prints 12
fn(2)
