# -*- coding:gbk -*- 
# 从matplotlib引入函数pyplot
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16 , 25]
plt.plot(squares, linewidth=5)
plt.title("Sequares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Sequares of Value", fontsize=15)
plt.tick_params(axis="both", labelsize=20)
plt.show()

