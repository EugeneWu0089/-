import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1) # 保證跑出來數字跟下面一樣

m = 100 # 樣本數
x1 = 50 + 30 * np.random.rand(m, 1) # m*1的array
y = 135 + 0.5 * x1 + 3 * np.random.randn(m, 1) # 後面為隨機誤差

x1[:5] # 當作體重
y[:5] # 當作身高

# -------------畫散佈圖-------------------

plt.figure(figsize=(5,4))
plt.plot(x1,y,"b.")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.savefig('plot_ex1.pdf', dpi=300, bbox_inches='tight')

plt.show()


# ------------使用模型，sklearn:linearRegression()--------------------

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(x1,y).intercept_ # fit為(x1 y)套用到lin_reg裡, intercept取出其截距
lin_reg.fit(x1,y).coef_ # coef為係數



# --------------Predict---------------------------------------

x1_new = np.array([[50],[80]]) # 帶入兩個x 分別為50,80
lin_reg.predict(x1_new)


# --------------Plot the regression model---------------------------------------

plt.figure(figsize=(5,4))

xls = np.linspace(x1.min(),x1.max(),10).reshape(-1,1)
y_pred = lin_reg.predict(xls)

plt.plot(x1, y, "b.")
plt.plot(xls, y_pred, 'r-', linewidth=2, label='$\hat y$')

plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.legend(loc='upper left', fontsize=14)

plt.show()










