# 梯度下降推导





## 线性回归

$$ h_\theta(x) = \theta_0 + \theta_1x_1 + \cdots + \theta_nx_n = \sum_{i=0}^n\theta_ix_i = \theta^Tx $$

## 损失函数(最小二乘)

$$ J(\theta) = \frac{1}{2m}\sum_{i=1}^m(h_\theta(x^{(i)} - y^{(i)}))^2 $$

## 梯度下降概念

$$ \theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}J(\theta)  $$

则 $J(\theta)$ 梯度为

$$ \nabla J(\theta) = 
\begin{bmatrix}
\frac{\partial J(\theta)}{\partial\theta_0} \\
\frac{\partial J(\theta)}{\partial\theta_1} \\
\frac{\partial J(\theta)}{\partial\theta_2} \\
\vdots                              \\ 
\frac{\partial J(\theta)}{\partial\theta_n} \\
\end{bmatrix}
$$

$$
\frac{\partial J(\theta)}{\partial\theta_j} 
= \frac{\partial}{\partial\theta_j}\left(\frac{1}{2m}\sum_{i=1}^m\left(h_{\theta}\left(x^{(i)}\right) - y^{(i)}\right)^2\right) 
= \frac{1}{m}\sum_{i=1}^m\left(h_{\theta}\left(x^{(i)}\right) - y^{(i)}\right)x_j^{(i)}
$$

利用梯度下降法，我们很容易实现对应的迭代解法。

$$ \theta_j := \theta_j - \alpha \frac{\partial}{\partial\theta_j}J(\theta) $$

## 代码推导过程

```python
loss = np.dot(X, theta) - Y
gradient = np.dot(X.T, loss) / m
theta -= alpha * gradient
```

$$
LOSS = X \cdot \theta - Y
=
\begin{bmatrix}
x_{1} \cdot \theta \\
x_{2} \cdot \theta \\
\vdots \\
x_{m} \cdot \theta \\
\end{bmatrix}
-
\begin{bmatrix}
y_0 \\
y_1 \\
\vdots \\
y_m \\
\end{bmatrix}
= 
\begin{bmatrix}
x_{10} & x_{11} & x_{12} & \cdots & x_{1n} \\
x_{20} & x_{21} & x_{22} & \cdots & x_{2n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
x_{m0} & x_{m1} & x_{m2} & \cdots & x_{mn} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
\theta_0 \\
\theta_1 \\
\vdots \\
\theta_n \\
\end{bmatrix}
-
\begin{bmatrix}
y_0 \\
y_1 \\
\vdots \\
y_m \\
\end{bmatrix}
=
\begin{bmatrix}
loss_0 \\
loss_1 \\
\vdots \\
loss_m \\
\end{bmatrix}
$$

$$
GRADIENT =
\begin{bmatrix}
\frac{\partial}{\partial\theta_0}J(\theta) \\
\frac{\partial}{\partial\theta_1}J(\theta) \\
\vdots \\
\frac{\partial}{\partial\theta_n}J(\theta) \\
\end{bmatrix}
=
\begin{bmatrix}
\sum_{i=1}^m(h_\theta(x_i) - y_i)x_{i0} \\
\sum_{i=1}^m(h_\theta(x_i) - y_i)x_{i1} \\
\vdots \\
\sum_{i=1}^m(h_\theta(x_i) - y_i)x_{in} \\
\end{bmatrix} 
=
\begin{bmatrix}
\sum_{i=1}^mloss_ix_{i0} \\
\sum_{i=1}^mloss_ix_{i1} \\
\vdots \\
\sum_{i=1}^mloss_ix_{in} \\
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
x_{10} & x_{20} & \cdots & x_{m0} \\
x_{11} & x_{21} & \cdots & x_{m1} \\
\vdots \\
x_{1n} & x_{2n} & \cdots & x_{mn} \\
\end{bmatrix} 
\cdot
\begin{bmatrix}
loss_1 \\
loss_2 \\
\vdots \\
loss_m \\
\end{bmatrix} 
= X^T \cdot LOSS
$$

## 完整代码

梯度下降实现

```python
def gd(X, Y, alpha=0.01, epsilon=1e-6):
    m, n = np.shape(X)
    theta = np.ones(n)
    sse2 = 0
    Xt = np.transpose(X)
    while True:
        hypothesis = np.dot(X, theta)
        loss = hypothesis - Y

        sse = np.dot(loss.T, loss) / (2 * m)
        if abs(sse2 - sse) < epsilon:
            break
        else:
            sse2 = sse

        gradient = np.dot(Xt, loss) / m
        theta -= alpha * gradient
    return theta
```

测试代码

```python
X = [(1, 1.), (1, 2.), (1, 3.), (1, 4.), (1, 5.), (1, 6.), (1, 7.), (1, 8.), (1, 9.)]
Y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]
alpha, epsilon = 0.05, 1e-8

b, a = gd(X, Y, alpha, epsilon)

print('{0} * x + {1} = 0'.format(a, b))

x = np.array(X)
plt.plot(x, Y, 'o', label='Original data', markersize=5)
plt.plot(x, a * x + b, 'r', label='Fitted line')
plt.show()
```

## 启动Notebook

```sh
jupyter notebook
```

## 梯度下降

梯度下降的典型实现方式

```python
import numpy as np

def bgd(x, y, alpha=0.01, epsilon=1e-8):
    m = len(x)
    _x = np.column_stack((np.ones(m), x))
    m, n = np.shape(_x)
    theta, sse2 = np.ones(n), 0
    xt = _x.T
    while True:
        loss = np.dot(_x, theta) - y
        sse = np.dot(loss.T, loss) / (2 * m)
        if abs(sse - sse2) < epsilon:
            break
        else:
            sse2 = sse

        gradient = np.dot(xt, loss) / m
        theta -= alpha * gradient
    return theta
```