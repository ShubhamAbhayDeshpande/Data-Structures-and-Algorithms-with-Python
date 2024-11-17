"""
This file contains basic imlementation of graph with constructors and other related methods.

Graph will be entirely implemented using the adjacency list method. Adjacency list will be implemented
entirely using dictionary and methods related to dictionary. 

"""


# Create a class with the name 'Graph'
class Graph:
    def __init__(self):
        """
        Constructor has only one attribute adj_lst which is an empty dictionary.
        This dictionary will contain the adjacency list in the future.

        """
        self.adj_lst = {}

    def add_vertex(self, vertex: any):
        """
        This method will add vertex with value 'vertex' to the adjacency list dictionary.

        The vertex will be assigned to an empty list. This list will contain all the vertices which
        share an edge with this vertex.

        """
        if vertex not in self.adj_lst.keys():
            self.adj_lst[vertex] = []
            return True
        # If the vertex already present in graph, return False.
        return False

    def add_edge(self, v1: any, v2: any):
        """
        This method will add an edge between vertex v1 and vertex v2.

        To add an edge, both vertices should exist in the list and the values of v1 and v2 should be diffferent.
        A vertex cannot have an edge with itself.

        """
        if v1 in self.adj_lst.keys() and v2 in self.adj_lst.keys() and v1 != v2:
            self.adj_lst[v1].append(v2)
            self.adj_lst[v2].append(v1)
            return True
        raise ValueError("Enter valid values for 'v1' and 'v2'.")

    def remove_edge(self, v1: any, v2: any):
        """
        This method will remove an edge between vertices v1 and v2.

        To remove an edge, two vertices should be present in the keys of adj_lst and the values of v1 and v2
        should be unique.

        The edge case in this case is:
        1. When the vertex is incerted in the graph but does not have an edge with any of the other vertices.

        In the above case, an error message should be raised (try and except block in the code).

        """
        if v1 in self.adj_lst.keys() and v2 in self.adj_lst.keys() and v1 != v2:
            try:
                self.adj_lst[v1].remove(v2)
                self.adj_lst[v2].remove(v1)
                return True
            except ValueError:
                raise ValueError("v1 and v2 do not have an edge between them.")

        raise ValueError("Enter valid values for 'v1' and 'v2'.")

    def remove_vertex(self, v: any):
        """
        This method will remove the vertex 'v' from the graph.

        To implement this method, we will call 'remove_edge()' method to remove all the connections
        between vertex 'v' and other vertices.

        After that we can remove 'v' from the dictionary self.adj_lst.

        """
        # Removing all the edges betwen vertex 'v' and all other vertices.
        # Need to check if the 'v' is present in the vertex
        if v in self.adj_lst.keys():
            for keys in self.adj_lst.keys():
                if keys != v:
                    self.remove_edge(keys, v)
            # Delete vertex 'v' from self.adj_lst dictionary
            del self.adj_lst[v]
            return True
        raise ValueError("Check the value of the vertex. Vertex not present in graph.")

    def print_vertex(self):
        for ver in self.adj_lst:
            print(f"vertex : {ver}", self.adj_lst[ver])


if __name__ == "__main__":
    my_graph = Graph()

    # Make vertices
    my_graph.add_vertex(1)
    my_graph.add_vertex(2)
    my_graph.add_vertex(3)
    my_graph.add_vertex(4)

    # Add edges between vertices
    my_graph.add_edge(1, 2)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(1, 4)
    my_graph.add_edge(3, 4)
    my_graph.add_edge(2, 4)
    print("Graph before removing vertex 4:")
    my_graph.print_vertex()

    # Removing vertex
    my_graph.remove_vertex(4)
    print("Graph after removing vertex 4:")
    my_graph.print_vertex()
