
from urllib.request import urlopen
import json

def E(X):
    '''
    :param X: [(xi, pi), ...]
    :return: int expected value of random variable X
    '''
    return sum([e[0] * e[1] for e in X])

def Var(X):
    '''
    :param X: [(xi, pi), ...]
    :return: int variance of random variable X
    '''
    return E([(e[0]**2, e[1]) for e in X]) - (E(X))**2


url = 'https://api.blockchain.info/charts/market-price?timespan=1year&format=json'

http_file = urlopen(url)
lines = http_file.readlines()
s = [str(line, encoding = 'utf-8') for line in lines]
t =''
for line in s:
    t += line
s = json.loads(t)
values = s.get('values')
X = []
P = [0.1550018235964546, 0.20615242538328463, 0.27418272575976854, 0.36466302526049216]
for i in range(1, len(values)):
    e2, e1 = values[i], values[i-1]
    dzeta = e2.get('y')/e1.get('y')
    quarter = int(i//91.25)
    X.append((dzeta-1, P[quarter]/91.25))
print(E(X))  # revenue per day
k = (E(X)) * 30  # revenue per month
def kbn(month_sum):
    return month_sum/k
print(1/k)
