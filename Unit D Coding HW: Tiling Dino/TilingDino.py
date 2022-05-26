import networkx as nx
# CS4102 Spring 2022 -- Unit D Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: byk6q
# Collaborators: my6jdq
# Sources: Introduction to Algorithms, Cormen
#################################
class TilingDino:
    def __init__(self):
        return
    def color(self, xcoordinate, ycoordinate):
        if (int(xcoordinate) + int(ycoordinate)) %2 == 0:
            return "blue"
        else:
            return "red"
    def length(self, lines):
        return len(lines[0])
    def width(self, lines):
        return len(lines)
    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        colors = []
        edges = []
        source = []
        sink = []
        x = self.length(lines)
        y = self.width(lines)
        for i in range(y):
            for j in range(x):
                if(lines[i][j] == "#"):
                    colors.append((j,i,self.color(j,i)))
        for i in colors:
            if (i[0] != x -1) and (i[1] != y -1):
                valid = [item for item in colors if ((item[0] == i[0] + 1 and item[1] == i[1]) or (item[0] == i[0] and item[1] == i[1] + 1)) and (item[2]!=i[2])]
                for j in valid:
                    if j[2] == "blue":
                        edges.append((i,j))
                    else:
                        edges.append((j,i))
            elif(i[0] == x-1):
                valid = [item for item in colors if ((item[0] == i[0]) and (item[1] == i[1] + 1)) and (item[2]!=i[2])]
                for j in valid:
                    if j[2] == "blue":
                        edges.append((i,j))
                    else:
                        edges.append((j,i))
            elif(i[1] == y-1):
                valid = [item for item in colors if (item[0] == i[0] + 1and item[1] == i[1]) and (item[2]!=i[2])]
                for j in valid:
                    if j[2] == "blue":
                        edges.append((i,j))
                    else:
                        edges.append((j,i))
        G = nx.DiGraph()
        for i in edges:
            if i[0][2] == "red" and (("source", i[0])) not in source:
                source.append(("source",i[0]))
            if i[1][2] == "blue"and ((i[1], "sink")) not in sink:
                sink.append((i[1], "sink"))
        edges = source + edges + sink
        for i in edges:
            G.add_edge(i[0], i[1], capacity = 1.0)
        m = nx.maximum_flow(G, edges[0][0], edges[len(edges)-1][1])
        flow = m[1]
        counter = 0
        domino = []
        for a, b in flow.items():#https://www.programiz.com/python-programming/nested-dictionary
            if a[2] == "blue":
                break
            if a ==  source[counter][1]:
                for key in b:
                    if b[key] == 1.0:
                        domino.append((source[counter][1], key))
                counter+=1
        answer = []
        if len(colors) != len(domino)*2:
            return ["impossible"]
        else:
            for i in domino:
                answer.append(str(i[0][0]) + " " + str(i[0][1]) + " " + str(i[1][0]) + " " + str(i[1][1]))
            return answer
