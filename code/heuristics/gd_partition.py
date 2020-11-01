class GdPartition:
    def __init__(self, ar):
        self.array = ar
        self.p = [[], [], [], []]

    def p_sum(self):
        return [sum(self.p[0]), sum(self.p[1]), sum(self.p[2]), sum(self.p[3])]

    def partition(self):
        for n in sorted(self.array, reverse=True):
            psum = self.p_sum()
            i_min = psum.index(min(psum))
            self.p[i_min].append(n)
