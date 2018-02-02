
$$ L(\theta) = \prod_{i=1}^mP(y_i=1|x_i)^{y_i}(1-P(y_i=1|x_i))^{1-y_i} $$

$$ log(L(\theta)) = \sum_{i=1}^m log\left(P(y_i=1|x_i)^{y_i}(1-P(y_i=1|x_i))^{1-y_i}\right) $$

$$ = \sum_{i=1}^m \left(y_ilogP(y_i=1|x_i) + (1 - y_i)log(1 - P(y_i=1|x_i)) \right)$$


$ P(Y=1|x) = \frac{1}{1 + e^{-z}}$ 


其中 $z = \theta^Tx  $


$$ P(y=1|x;\theta) = h_{\theta}(x) $$

$$ P(y=0|x;\theta) = 1 - h_{\theta}(x) $$

$$ P(y|x;\theta) = \left[h_{\theta}(x_i)\right]^{y_i}\left[1 - h_{\theta}(x_i)\right]^{(1 - y_i)} $$

$$ L(\theta) = \prod_{i=1}^m\left[h_{\theta}(x_i)\right]^{y_i}\left[1 - h_{\theta}(x_i)\right]^{(1 - y_i)} $$

#### 逻辑回归损失函数导数

$$ J(\theta) = \frac{1}{m}\sum_{i=1}^m Cost\left(h_{\theta}\left(x^{(i)}\right),y^{(i)}\right) 
= -\frac{1}{m}[\sum_{i=1}^m y^{(i)}\log h_{\theta}\left(x^{(i)}\right) 
+ \left(1 - y^{(i)}\right)\log\left(1 - h_{\theta}\left(x^{(i)}\right)\right)] $$

因为：$ y = \frac{1}{1 + e^{-x}} $, $(1 - y) = \frac{e^{-x}}{1 + e^{-x}} $ 
可知
$ \frac{dy}{dx} = y \cdot (1 - y) = \frac{e^{-x}}{(1 + e^{-x})^2} $，
则有：

$$ \frac{\partial}{\partial\theta_j}J(\theta) = -\frac{1}{m}[\sum_{i=1}^m 
y^{(i)} \frac{h_{\theta}^{'}\left(x^{(i)}\right)}{h_{\theta}\left(x^{(i)}\right)}\cdot x_j^{(i)}
- \left(1 - y^{(i)}\right)\frac{h_{\theta}^{'}\left(x^{(i)}\right)}{1 - h_{\theta}\left(x^{(i)}\right)}\cdot x_j^{(i)}] $$

$$ = -\frac{1}{m}\sum_{i=1}^m \left(y^{(i)}\left(1 - h_{\theta}(x^{(i)})\right) 
- \left(1 - y^{(i)}\right)h_{\theta}(x^{(i)})\right) x_j^{(i)} $$

$$ = -\frac{1}{m}\sum_{i=1}^m \left(y^{(i)} - h_{\theta}(x^{(i)})\right)x_j^{(i)} 
= \frac{1}{m}\sum_{i=1}^m \left(h_{\theta}(x^{(i)}) - y^{(i)}\right)x_j^{(i)} 
$$


#### $\ln x$ 导数的推导


$$ \frac{d}{dx}\ln x 
= \lim_{h \to 0} \frac{\ln(x + h) - \ln(x)}{h} 
= \lim_{h \to 0} \frac{\ln\left(\frac{x + h}{x}\right)}{h} 
= \lim_{h \to 0} \frac{\ln\left(1 + \frac{h}{x}\right)}{h} $$


$$ = \lim_{h \to 0} \frac{\ln(x + h) - \ln(x)}{x \cdot \left(\frac{h}{x}\right)} 
= \frac{1}{x} \cdot \lim_{h \to 0} \frac{\ln\left(1 + \left(\frac{h}{x}\right)\right)}{\frac{h}{x}} 
= \frac{1}{x} \cdot \lim_{h \to 0} \ln\left(1 + \frac{h}{x}\right)^{\frac{x}{h}} $$


因为：

$$ \lim_{u \to 0}\left(1 + u\right)^{\frac{1}{u}} = e $$

则有：

$$ \frac{d}{dx}\ln x 
= \frac{1}{x} \cdot \ln\left(\lim_{\frac{h}{x} \to 0} \left(1 + \frac{h}{x}\right)^{\frac{x}{h}}\right)
= \frac{1}{x} \cdot \ln e
= \frac{1}{x} $$


设$V_n,U_m$分别是$n,m$维的线性空间，如果一个从$V_n$ 到$U_m$的映射T满足

1）对于任意$\vec{a}_1,\vec{a_2} \in V_n$，有$T(\vec{a_1}+\vec{a_2})=T(\vec{a}_1)+T(\vec{a}_2)$

2）对于任一$\vec{a} \in V_n, \lambda \in R$，有$T(\lambda \vec{a})=\lambda T(\vec{a})$

则称映射T为线性映射，又称线性变换。
