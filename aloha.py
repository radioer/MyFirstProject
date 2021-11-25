import matplotlib.pyplot as plt
import numpy as np
import sympy
from typing import List


p = np.arange(101) / 100
def caculatelimit():
    n = sympy.symbols('n')
    f = (1 - 1/n)**(n)
    return sympy.limit(f, n, sympy.oo)

def caculatefordiffpeople(numofpeople: List[int]) -> List[float]:
    Iter = 100000
    basket = np.random.rand(numofpeople, Iter)
    result = []
    for i in range(len(p)):
        basketball = basket
        basketball = np.where(basketball > 1 - p[i], 1, 0)
        basketball = np.sum(basketball, axis=0)
        basketball = np.where(basketball <= 1, basketball, 0)
        result.append(np.sum(basketball)/Iter)
    return result


limination = []
for i in range(len(p)):
    limination.append(caculatelimit())
plt.plot(p, limination, label='limination:exp(-1)')
mynum = [2, 4, 6, 8, 10, 12]
for i in range(len(mynum)):
    myresult = caculatefordiffpeople(mynum[i])
    print('人数为', mynum[i], '时最大的概率为：', max(myresult))
    print('此时p的值为：', p[myresult.index(max(myresult))])
    plt.plot(p, myresult, label=('number of people =', mynum[i]))
plt.legend()
plt.xlabel('probability')
plt.ylabel('hit frequency')
plt.title('hit frequeccy changing because of probability changing and different people')
plt.show()
