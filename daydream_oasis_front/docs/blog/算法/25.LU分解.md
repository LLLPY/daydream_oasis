---

next: false

---



<BlogInfo id="1148"/>

```python
import numpy as np
import fractions

np.set_printoptions(formatter={'all': lambda x: str(fractions.Fraction(x).limit_denominator())})


def LU_decompose(A):
    n = len(A)
    L = np.zeros(shape=(n, n))

    for base in range(n - 1):
        for i in range(base + 1, n):
            L[i, base] = A[i, base] / A[base, base]
            A[i] = A[i] - L[i, base] * A[base]
    for i in range(n):  # range(n) 范围：[0，n-1]
        L[i, i] = 1
    U = np.array(A)
    print("L:")
    print(L)
    print("U:")
    print(U)


if __name__ == '__main__':
    A = np.array([[5., -4., 1., 0],
                  [-4., 6., -4., 1],
                  [1., -4., 6., -4],
                  [0, 1, -4, 5]
                  ])
    LU_decompose(A)

```



<ActionBox />
