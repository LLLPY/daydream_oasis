
<BlogInfo title="一个简单的linear regression例子" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=102 category="机器学习" tag_list="[]" create_time="2023.09.21 11:32:48.654267" update_time="2023.09.21 11:32:48.654273" />

^^^^^^^^^
<h2 id="一个简单的linear-regression例子">一个简单的linear regression例子</h2>
<p>还是使用之前的房屋售卖的例子,现在我有一些房屋的大小以及其售价的数据，现在我有一幢大小为1200feet²的房子，我应该以多少价格售卖出去比较合适？</p>
<pre><code class="language-python"># 一些房屋售卖的数据
size_list = [2104,1416,1534,852,3210]
price_list = [400,232,315,178,870]
</code></pre>
<pre><code class="language-python"># 监督学习的流程

# training set ---&gt; learning algorithm ---&gt; get the model(or f) --input a new x to model-&gt; get the &quot;y-hat&quot;(prediction)
# &lt;----------- training -------------&gt;                            &lt;----------------- predicate -----------------------&gt;
</code></pre>
<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimSun' # 设为宋体，正常显示中文
# 1.training set
x_train = np.array(size_list)
y_train = np.array(price_list)

print(f'x_train:{x_train}')
print(f'y_train:{y_train}')
</code></pre>
<pre><code>x_train:[2104 1416 1534  852 3210]
y_train:[400 232 315 178 870]
</code></pre>
<pre><code class="language-python"># 2.看一下数据的分布情况
plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title(&quot;Housing Prices&quot;)
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show()
</code></pre>
<p><img src="../../../media/image/2023/09/21/linear_regression_4_0.65562ab6582f11eea0c5d9fd74d8f392.png" alt="linear_regression_4_0.65562ab6582f11eea0c5d9fd74d8f392.png" /></p>
<pre><code class="language-python"># 3.选择一种算法。这里就选用最简单的算法：linear regression方法，简单并且有用。

# 3.1 如何表示这个model( or f)呢?
# 在选定模型算法为：linear regression后，我们可以非常容易想到我们常用的一次函数：y=ax+b。

# 3.2虽然确定了模型的表达式，但是表达式中的a和b这两个未知的参数如何去确定呢？

def compute_model_with_train(x_train,y_train):
    '''将这个过程看成是训练的过程，通过输入训练集，在&quot;训练&quot;之后，会产出一个model，这样就确定了我们模型表达式中的未知参数a和b'''
  
    a = 0.2314
    b = 1.2
    f = lambda x:a*x + b  
    return f

model = f = compute_model_with_train(x_train,y_train)
</code></pre>
<pre><code class="language-python"># 4.看一下使用我们“训练”出的模型对数据的模拟情况

y_i_list = [f(x) for x in x_train]

# 我们模型的预测值
plt.plot(x_train, y_i_list, c='b',label='拟合曲线')

# 实际值
plt.scatter(x_train, y_train, marker='x', c='r',label='实际值')
plt.scatter(x_train, y_i_list, marker='x', c='b',label='预测值')

# Set the title
plt.title(&quot;Housing Prices&quot;)
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()
</code></pre>
<p><img src="linear_regression_files/linear_regression_6_0.png" alt="png" /><img src="../../../media/image/2023/09/21/linear_regression_6_0.6aadc30c582f11eea0c5d9fd74d8f392.png" alt="linear_regression_6_0.6aadc30c582f11eea0c5d9fd74d8f392.png" /></p>
<pre><code class="language-python"># 5.预测
# 在得到模型后，我们就可以对任意的一个合法的输入进行预测了。
x_i = 1200
y_i = f(x_i)

print(f'当房子的大小为{x_i}feet²时，以 ${y_i:.0f} thousand dollars价格售卖比较合适。')
</code></pre>
<pre><code>当房子的大小为1200feet²时，以 $279 thousand dollars价格售卖比较合适。
</code></pre>

