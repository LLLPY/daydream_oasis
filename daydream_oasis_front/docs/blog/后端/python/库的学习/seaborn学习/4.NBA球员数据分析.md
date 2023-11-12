---

next: false

---



<BlogInfo id="677"/>

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('nba_2017_nba_players_with_salary.csv')
print(data.head())

#相关性 求任意两组数据之间的相关性
corr=data.corr()
print(corr.head())

#绘制相关性的热力图


plt.figure(figsize=(50,50))
sns.heatmap(corr,square=True,linewidths=0.1,annot=True)
plt.savefig('NBA球员数据分析之相关性.png')
plt.show()


print(data.columns.values)
#获取球员的效率排行榜
rpm_list=data.loc[:,['PLAYER','AGE','SALARY_MILLIONS','RPM']].sort_values(by='RPM',ascending=False)
print(rpm_list.head(10))

#获取球员的薪资排行榜
rpm_list=data.loc[:,['PLAYER','AGE','SALARY_MILLIONS','RPM']].sort_values(by='SALARY_MILLIONS',ascending=False)
print(rpm_list.head(10))


#获取球员的年龄 薪水 效率值的分布情况

#年龄
plt.figure(figsize=(100,50))
sns.set_theme(style='darkgrid')
sns.displot(data['AGE'],kde=True,kind='hist',height=100)
plt.show()
print(data['AGE'])
# age_min=data['AGE'].min()
# age_max=data['AGE'].max()
# age_bins=np.linspace(age_min,age_max,30)
# plt.xticks(age_bins)
# plt.ylabel('AGE')


#薪水
plt.subplot(3,1,2)
sns.displot(data['SALARY_MILLIONS'],kde=True)
salary_min=data['SALARY_MILLIONS'].min()
salary_max=data['SALARY_MILLIONS'].max()
salary_bins=np.linspace(salary_min,salary_max,30)
plt.xticks(salary_bins)
plt.ylabel('SALARY_MILLIONS')
#效率
plt.subplot(3,1,3)
sns.displot(data['RPM'],kde=True)
rpm_min=data['RPM'].min()
rpm_max=data['RPM'].max()
rpm_bins=np.linspace(rpm_min,rpm_max,30)
plt.xticks(rpm_bins)
plt.ylabel('RPM')


#查看各个变量之间的相关性
# sns.pairplot(data)
plt.show()

```



<ActionBox />
