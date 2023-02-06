
import random

# Набор массива длиною введенной пользователем случайными целыми числами.
a = []
[a.append(random.randint(1, 10)) for i in range(1, int(input()) + 1)]

