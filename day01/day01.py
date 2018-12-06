
def fibonacci(n):
    a, b = 0, 1
    for num in xrange(0, n):
        a, b = b, a+b
    # loop ends here
    print a

words = ['cat', 'bat', 'rat']
for w in words:
    print w

for i in range(len(words)):
    if i == (len(words) - 1):
        print words[i]
    else:
        print words[i] + ',',

for i in range(-len(words), 0, 1):
    if i == -1:
        print words[i]
    else:
        print words[i] + ',',

i = 0
while i < 10:
    print i,
    i += 1


#fibonacci(10)
