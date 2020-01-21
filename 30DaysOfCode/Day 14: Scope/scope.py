class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        l = len(a)
        for i in range(0,l):
            for j in range(i+1,l):
                difference = abs(a[i]-a[j])
                self.maximumDifference = max(self.maximumDifference, difference)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
