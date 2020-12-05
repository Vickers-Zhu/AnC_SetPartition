from methods import fitness


class ExPartition:
    def __init__(self, ar):
        self.array = ar
        sum_tg = sum(self.array)
        self.targets = [int(sum_tg/4), int(sum_tg/4), int(sum_tg/4), int(sum_tg/4)]
        self.p = [[], [], [], []]
        self.p_his = []
        self.fit = 10

    def partition(self):
        self.partition_cur(0)

    def partition_cur(self, i):
        temp = []
        for p in self.p:
            tp = p[:]
            temp.append(tp)
        self.p_his.append(temp)
        if i < len(self.array):
            value = self.array[i]
            for k in range(0, 4):
                if self.targets[k] >= value:
                    self.targets[k] -= value
                    self.p[k].append(value)
                    if self.partition_cur(i + 1):
                        break
                    else:
                        self.targets[k] += value
                        self.p[k].remove(value)
        return sum(self.targets) == 0
