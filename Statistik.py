import codecs
import random
import sys

import matplotlib.pyplot as plt
import numpy
import time

import operator


def listTest():
    arguments = sys.argv
    print str(arguments) + ' ' + str(len(arguments))
    list = [2, 3, 4, 5, 6, 7, 8, 9, ]
    print list
    list.append(10)
    print list
    del list[0]
    print list
    print "min is " + str(numpy.min(list))
    for i in range(0, 1000):
        list.append(random.randint(0, 1000))
    list.sort()
    plt.plot(list)
    plt.show()


# listTest()

ticks = time.time()
print "start programm at " + time.asctime(time.localtime(ticks))
f = codecs.open("res/source.txt", "r", "utf-8")
content = f.readlines()
allText = reduce(lambda x, y: x + y, content, "")
print allText
words = allText.split()

wordWithCount = {}
for word in words:
    if word in wordWithCount:
        count = wordWithCount[word]
        wordWithCount[word] += 1
    else:
        wordWithCount[word] = 1

wordWithCountSorted = sorted(wordWithCount.items(), key=operator.itemgetter(1), reverse=True)
for word in wordWithCountSorted:
    print word[0] + " " + str(word[1])

o = codecs.open("out/output.txt", "w+", "utf-8")
o.write("hello")
o.close()

print "calc time " + str((time.time() - ticks) * 1000) + " ms"
print "End"
