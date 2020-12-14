import itertools
import sys
from collections import Counter

test_array = [3, 2, 2, 4]
# test_array = [6,10,7,3,4,10,4,4,3]

class ExPartition:
    def __init__(self, ar):
        self.array = ar
        self.p = ""

    def Rest_List(self, whole_list, li1):
        return list((Counter(whole_list) - Counter(li1)).elements())

    def Diff_Sum(self, li1, li2):
        return sum(li1) - sum(li2)

    def partitions(self, n, k):
        for c in itertools.combinations(range(n+k-1), k-1):
            yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]

    def partition(self):
        length = len(self.array)
        print("length of the array is :", length)
        result =[sys.maxsize, []]
        if length < 5:
            i = 0
            for item in self.array:
                result[1].append([item])
                i = i + 1
            while i < 4:
                result[1].append([])
                i = i + 1
            max1 = max(sum(result[1][0]), sum(result[1][1]), sum(result[1][2]), sum(result[1][3]))
            min1 = min(sum(result[1][0]), sum(result[1][1]), sum(result[1][2]), sum(result[1][3]))
            result[0] = max1 - min1
        else:
            parts = list(self.partitions(len(self.array), 4))
            for c in parts:
                c = list(c)# b1, b2, b3, b4 = c #(1, 0, 0, 5)
                c = tuple([i for i in c if i!=0] )#c(1,5)
                if len(c) == 4:#(1, 1, 1, 2)
                    b1, b2, b3, b4 = c
                    for part1 in itertools.combinations(self.array, b1): #[0] [1] [2] [3] [4]
                        part1_s=sum(list(part1))
                        res1 = self.Rest_List(self.array, part1)
                        for part2 in itertools.combinations(res1, b2): #[1], [2], [3], [4]
                            part2_s=sum(list(part2))
                            res2 = self.Rest_List(res1, part2)
                            for part3 in itertools.combinations(res2, b3): #[2], [3], [4]
                                part3_s=sum(list(part3))
                                res3 = self.Rest_List(res2, part3)
                                for part4 in itertools.combinations(res3, b4): #[3], [4]
                                    part4_s=sum(list(part4))
                                    max1 = max(part1_s, part2_s, part3_s, part4_s)
                                    min1 = min(part1_s, part2_s, part3_s, part4_s)
                                    cur_res = max1 - min1
                                    cur_per = [list(part1), list(part2), list(part3), list(part4)]
                                    cur_res_min, cur_res_per = result[0], result[1]
                                    if cur_res_min > cur_res:
                                        result[0] = cur_res
                                        result[1] = cur_per
        self.p = result[1]
        print(result)
#
#
# a = ExPartition(test_array)
# a.partition()
