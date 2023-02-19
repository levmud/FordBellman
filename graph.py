INF = 10 ** 10

class Graph:
    # Строка ответа
    s = ""

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # метод, добавляющая ребра в граф u-начало, v-конец, w-вес
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def get_s(self):
        return self.s

    def get_v(self):
        return self.V

    def printPath(self, i, path):
        p = ')'
        while i != -1:
            p += ' '
            p += str(i+1)
            i = path[i]
        p += '( '
        return p[::-1]


    # функция вывода информации о расстояних или о том, что существует отрицательный цикл
    def printArr(self, dist, path):
        self.s = ""
        self.s += "Веришина Расстояние от выбранной\n"
        for i in range(self.V):
            if dist[i] != INF:
                self.s += " " + str(i + 1) + "       " + str(dist[i])
                self.s += self.printPath(i, path)
                self.s += "\n"
            else:
                self.s += " " + str(i + 1) + "       Нет пути"
                self.s += "\n"

    # Основная функция, которая находит кратчайшее расстояние от выбранной вершины
    # до всех остальных вершин с использованием алгоритма Беллмана-Форда.
    # Функция также обнаруживает цикл отрицательного веса
    def BellmanFord(self, src):

        # Инициализируем расстояния от выбранной вершины до всех остальных
        # Расстояния до самой себя делаем равным нулю
        dist = [INF] * self.V
        dist[src] = 0
        path = [-1] * self.V

        for i in range(self.V - 1):
            # Будем производить релакцсацию вдоль кажого ребра
            for u, v, w in self.graph:
                if (dist[u] != INF) and (dist[u] + w < dist[v]):
                    dist[v] = dist[u] + w
                    path[v] = u
        # Проверим наличие циклов с отрицательным весом.
        # Приведенный выше шаг гарантирует кратчайшие расстояния,
        # если график не содержит цикла с отрицательным весом.
        # Если мы получаем более короткий путь, то возникает цикл.
        for u, v, w in self.graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                self.s = "Граф содержит отрицательные циклы"
                return
        self.printArr(dist, path)