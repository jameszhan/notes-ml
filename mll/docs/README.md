#### 文档中心



#### 线性回归
$$ h_\theta(x) = \theta_0 + \theta_1x_1 + \cdots + \theta_nx_n = \sum_{i=0}^n\theta_ix_i = \theta^Tx $$

#### 损失函数(最小二乘)
$$ J(\theta) = \frac{1}{2}\sum_{i=1}^m(h_\theta(x^{(i)} - y^{(i)}))^2 $$

#### 梯度下降
$$ \theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}J(\theta)  $$

$$ \frac{\partial}{\partial\theta_j}J(\theta) = \frac{\partial}{\partial\theta_j}(\frac{1}{2}\sum_{i=1}^m(h_\theta(x^{(i)} - y^{(i)}))^2) $$
$$ = 2 * \frac{1}{2}\sum_{i=1}^m(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} $$
$$ = \sum_{i=1}^m(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} $$


$$ \frac{\partial Q}{\partial a} = 2 \sum_{i=1}^n \left[x_i(a x_i + b - y_i) \right] $$

