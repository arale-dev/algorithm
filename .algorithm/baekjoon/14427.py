A_num = int(input())
A_arr = [[i+1,j] for (i,j) in enumerate(list(map(int, input().split())))]
A_min = min(A_arr, key=lambda x : x[1])

test_num = int(input())
for _ in range(test_num):
    ins = list(map(int, input().split()))
    if ins[0] == 1:
        A_arr[ins[1]-1][1] = ins[2]
        if ins[1] != A_min[0]:
            if A_min[1] >= ins[2] and A_min[0] >= ins[1]:
                A_min = [ins[1], ins[2]]
        else:
            A_min = min(A_arr, key=lambda x : x[1])
    else:
        print(A_min[0])

class Node:
    def __init__(self, index, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
        self.index = index

class Tree:
    def __init__(self, A_arr):
        self.root = None
        self.left = None
        self.right = None
        self.value = value
        self.index = index