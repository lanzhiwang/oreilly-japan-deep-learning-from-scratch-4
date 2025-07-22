import numpy as np

# naive implementation
np.random.seed(0)  # 固定随机数种子
rewards = []


"""
>>> import numpy as np
>>> np.random.seed(0)
>>> np.random.rand()
0.5488135039273248
>>> np.random.rand()
0.7151893663724195
>>> np.random.rand()
0.6027633760716439
>>> 
"""
for n in range(1, 11):
    reward = np.random.rand()  # 生成一个 0 到 1 之间的随机数
    rewards.append(reward)
    Q = sum(rewards) / n
    print(Q)

print("---")

# incremental implementation
np.random.seed(0)
Q = 0

for n in range(1, 11):
    reward = np.random.rand()
    Q = Q + (reward - Q) / n
    print(Q)

"""
$ python avg.py 
0.5488135039273248
0.6320014351498722
0.6222554154571294
0.6029123573420713
0.567060845741438
0.5801997236289743
0.5598265075766483
0.6013198192273272
0.6415801460355164
0.6157662833145425
---
0.5488135039273248
0.6320014351498722
0.6222554154571294
0.6029123573420713
0.567060845741438
0.5801997236289743
0.5598265075766483
0.6013198192273272
0.6415801460355164
0.6157662833145425
$ 
"""
