import random
l = [random.choice(range(-50, 50)) for i in range(0, 30)]
print(l)

# def bubble(l):
#     l1 = l
#     l2 = []
#     while l1 != l2:
#         l2 = l1.copy()
#         for i in range(len(l1)-1):
#             print(l1[i], l1[i+1])
#             if l1[i] > l1[i+1]:
#                 l1[i], l1[i+1] = l1[i+1], l1[i]
# bubble(l)
# print(l)

# def insert(l):
#     l1 = l
#     l2 = []
#     while l1 != l2:
#         l2 = l1.copy()
#         for i in range(len(l1)-1):
#             if l1[i] > l1[i+1]:
#                 x = l[i+1]
#                 for j in range(0, i+1):
#                     if l1[j] > x:
#                         l1.insert(j, x)
#                         del l[i + 2]
#                         break
# insert(l)
# print(l)

def choose(l):
    for i in range(len(l)):
        min = l[i]
        id = 0
        for j in range(i, len(l)):
            if l[j] < min:
                id = j
                min = l[j]
        if min < l[i]:
            l.insert(i, min)
            del l[id+1]
choose(l)
print(l)
