import numpy as np

rows = 4
cols = 4
a = np.arange(rows*cols).reshape(rows, cols)
print(a)
print(a.sum())
print(a.sum(axis=1))

totalSum = 0
rowSum = np.zeros(rows, dtype=np.int32)

for i in range(rows):
    for j in range(cols):
        rowSum[i] += a[i][j]
    totalSum += rowSum[i]

print(totalSum)
print(rowSum)