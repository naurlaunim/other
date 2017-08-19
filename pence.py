# how many ways can we get 200 pence
nominal = [200, 100, 50, 20, 10, 5, 2, 1]

def pence(n, k):
    if n <= 0 or k > 7:
        return 0;
    if nominal[k] == 1 or n == 1:
        return 1;
    else:
        res = pence(n - nominal[k], k) + pence(n, k + 1)
        if n == nominal[k]:
            return res + 1
        else:
            return res

print(pence(200, 0))
