import matplotlib.pyplot as plt

labels = 'Нет назначения', 'Internet', 'Анализ', 'Ввод данных', 'Дизайн', 'Документация', 'М-медиа', 'Программирование'

z = [1360, 1326, 2700, 4850, 3730, 1040, 740, 20800]
fig, ax = plt.subplots()
ax.pie(z, labels=labels, autopct='%1.1f%%')
plt.title('Затраты')
plt.show()
print(sum(z))

t = [680, 168, 120, 2400, 440, 200, 240, 2480]
fig, ax = plt.subplots()
ax.pie(t, labels=labels, autopct='%1.1f%%')
plt.title('Трудозатраты')
plt.show()
print(sum(t), sum(t) / 24, sum(t) / 24 / 7)