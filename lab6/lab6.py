# Подключение библиотек
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn import datasets
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

X = np.random.randint(0, 100, size=(4, 4))

# Создание полотна для рисования
# fig = plt.figure(figsize=(15, 30))
# fig.patch.set_facecolor('white')

# Загрузка набора данных "Ирисы Фишера"
iris = datasets.load_iris()
#

# plt.figure(figsize=(5,5))

# Реализация иерархической кластеризации при помощи функции linkage
mergingsMin = linkage(X, method='single')
mergingsMax = linkage(X, method='complete')

# Построение дендрограммы. Разными цветами выделены автоматически определенные кластеры
R1 = dendrogram(mergingsMin, orientation='top', leaf_font_size=13)

# Отображение дендрограммы
plt.title("Min")
plt.show()

# Построение дендрограммы. Разными цветами выделены автоматически определенные кластеры
R2 = dendrogram(mergingsMax, orientation='top', leaf_font_size=13)

# Отображение дендрограммы
# plt.figure(figsize=(15,30))
plt.title("Max")
plt.show()

headers = ["X1", "X2", "X3", "X4"]
table = tabulate(X, headers=headers)

print(table)

