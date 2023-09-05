"""
input file format:
node1(origin) node2(destination) weight
-----------------------------------------
i use hash table(Dictionary) for implementing graph
"""


class Graph:
    def __init__(self, filename: str):
        self.__filename = filename
        self.__graph = dict()
        self.__create_graph()

    # Private functions
    def __create_graph(self):
        with open(self.__filename, 'r') as file:
            for data in file:
                data = data.split()
                if data[0] not in self.__graph.keys():
                    self.__graph[data[0]] = []
                self.__graph[data[0]].append([data[1], data[2]])


a = Graph("test.txt")
