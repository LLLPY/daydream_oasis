---

next: false

---



<BlogInfo id="15"/>

```python
import torch
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])  # 权重(未知参数)的初始值
w.requires_grad = True  # 将它设置为需要计算梯度


def forword(x):
    return w * x


# 计算损失的函数
def loss(x, y):
    return (forword(x) - y) ** 2


print(f'predicted (before training) f(4)={forword(4).item()}')

w_list = []
loss_list = []

for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)
        l.backward()  # 计算loss对w的导数
        print(f'x={x},y={y},grad={w.grad.item()}')  # w.grad.item() w的梯度
        w.data = w.data - 0.01 * w.grad.data  # 更新w的值 w=w-a*梯度
        w.grad.data.zero_()  # 每走一遍都要进行数据清零(否则会进行累加)

        w_list.append(w.data.item())
        loss_list.append(l.data.item())

        print(f'w={w.data.item()},loss={l.data.item()}')
print(f'predicted (after training) f(4)={forword(4).item()}')

plt.plot(w_list, loss_list)
plt.xlabel('w')
plt.ylabel('loss')
plt.title('loss-w')
plt.show()

```



<ActionBox />
