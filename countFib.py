class Counter(object):
    def __init__(self):
        self._number = 0
    def increment(self):
        self._number += 1
    def __str__(self):
        return str(self._number)
def fib(n, counter):
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n - 2, counter)
problemSize = 2
print ("%12s%15s" % ("Problem Size", "Calls"))
for count in range(5):
    counter = Counter()
    fib(problemSize, counter)
    print ("%12d%15s" % (problemSize, counter))
    problemSize *= 2

