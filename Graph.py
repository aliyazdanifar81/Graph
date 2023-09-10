import networkx as nx
import matplotlib.pyplot as plt

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
        self.__nodes = list()
        self.__create_graph()

    # User function
    def bfs(self, org=None, des=None):
        res, counter = [], 0
        if org is None:
            my_queue = [self.__nodes[0]]
        else:
            if org in self.__nodes:
                my_queue = [org]
            else:
                raise Exception("Origin was NOT found")
        if des is None:
            for key in my_queue:
                for val in self.__graph[key]:
                    if val[0] not in my_queue:
                        my_queue.append(val[0])
                res.append(my_queue[counter])
                counter += 1
            return res
        else:
            if des not in self.__nodes:
                raise Exception("Destination was NOT found")
            temp_dict, flag, res = {org: [None, 0]}, 0, []
            # temp_dict (format) = [nearest connected node, distance from origin]
            for key in my_queue:
                for val in self.__graph[key]:
                    if val[0] not in my_queue:
                        my_queue.append(val[0])
                        temp_dict[val[0]] = [key, temp_dict[key][1] + 1]
                    if val[0] == des:
                        flag, res = 1, [val[0]]
                        break
                else:
                    counter += 1
                    continue
                break

            if flag:
                while des != org:
                    res.append(temp_dict[des][0])
                    des = temp_dict[des][0]
            return res[::-1]

    # Private functions
    def __create_graph(self):
        with open(self.__filename, 'r') as file:
            for data in file:
                data = data.split()
                if data[0] not in self.__graph.keys():
                    self.__graph[data[0]] = []
                if data[1] not in self.__graph.keys():
                    self.__graph[data[1]] = []
                self.__graph[data[0]].append([data[1], data[2]])
            self.__nodes = list(self.__graph.keys())

    # Operator overloading
    def show(
            self):  # GUI design for his sector | resource for how to use "Networkx" -->
        # https://towardsdatascience.com/plotting-network-graphs-using-python-bc62f0d93b3f
        edge_labels = {}
        options = {
            'node_color': 'yellow',  # color of node
            'node_size': 1000,  # size of node
            'width': 1,  # line width of edges
            'arrowstyle': '-|>',  # array style for directed graph
            'arrowsize': 18,  # size of arrow
            'edge_color': 'blue',  # edge color
        }
        temp_graph = nx.DiGraph(directed=True)
        temp_graph.add_nodes_from(self.__nodes)
        for v in self.__nodes:
            for u in self.__graph[v]:
                temp_graph.add_edge(v, u[0])
                edge_labels[(v, u[0])] = u[1]
        # set layout
        pos = nx.circular_layout(temp_graph)
        # draw graph
        nx.draw(temp_graph, pos, with_labels=True, **options)
        nx.draw_networkx_edge_labels(temp_graph, pos, edge_labels, font_color='red', font_size=15)
        plt.show()


a = Graph("test.txt")
print(a.bfs())
a.show()
