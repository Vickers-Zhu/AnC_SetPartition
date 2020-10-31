class ExPartition:
    def __init__(self, ar):
        self.array = ar
        sum_tg = sum(self.array)
        self.targets = [int(sum_tg/4), int(sum_tg/4), int(sum_tg/4), int(sum_tg/4)]
        self.p = [[], [], [], []]

    def partition(self, i):
        if i < len(self.array):
            value = self.array[i]
            for k in range(0, 4):
                if self.targets[k] >= value:
                    self.targets[k] -= value
                    self.p[k].append(value)
                    if self.partition(i+1):
                        break
                    else:
                        self.targets[k] += value
                        self.p[k].remove(value)
        return sum(self.targets) == 0


