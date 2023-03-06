from causallearn.graph.GeneralGraph import GeneralGraph
from causallearn.graph.GraphNode import GraphNode
from causallearn.graph.Endpoint import Endpoint
from causallearn.graph.Edge import Edge


def causal_cmd_to_general_graph(path):
    with open(path) as f:
        line = f.readline()
        while "Graph Nodes:" not in line:
            line = f.readline()
        line = f.readline()
        variables: list[str] = line[:-1].split(";")

        nodes = [GraphNode(x) for x in variables]

        G = GeneralGraph(nodes)

        while "Graph Edges:" not in line:
            line = f.readline()
        lines = f.readlines()

        for line in lines:
            edge = line.split()
            if (len(edge) == 0):
                break

            leftNode = edge[1]
            rightNode = edge[3]
            leftEpt = edge[2][0:1]
            rightEpt = edge[2][2:3]

            for i in range(0, len(nodes)):
                if nodes[i].name == leftNode:
                    _l = nodes[i]
                    break

            for i in range(0, len(nodes)):
                if nodes[i].name == rightNode:
                    _r = nodes[i]
                    break

            if leftEpt == "-":
                _le = Endpoint.TAIL
            elif leftEpt == "<":
                _le = Endpoint.ARROW
            elif leftEpt == "o":
                _le = Endpoint.CIRCLE
            else:
                _le = None

            if rightEpt == "-":
                _re = Endpoint.TAIL
            elif rightEpt == ">":
                _re = Endpoint.ARROW
            elif rightEpt == "o":
                _re = Endpoint.CIRCLE
            else:
                _re = None

            if _le == Endpoint.TAIL and _re == Endpoint.ARROW:
                G.add_directed_edge(_l, _r)
            elif _le == Endpoint.ARROW and _re == Endpoint.TAIL:
                G.add_directed_edge(_r, _l)
            # elif _le == Endpoint.TAIL and _re == Endpoint.TAIL:
            #     G.add_undirected_edge(_l, _r)
            else:
                e = Edge(_l, _r, _le, _re)
                G.add_edge(e)

    return G
