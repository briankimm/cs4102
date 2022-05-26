# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID:byk6q
# Collaborators:jw2zph
# Sources: Introduction to Algorithms, Cormen
#################################

class Supply:
    def __init__(self):
        return
    def numberOfNodes(self, file_data):
        nodes = file_data[0].split()
        return int(nodes[0])
    def numberOfPossibleLinks(self, file_data):
        possibleLinks = file_data[0].split()
        return int(possibleLinks[1])
    def nameAndType(self, file_data): # initiate vertice id at 0
        x = self.numberOfNodes(file_data) + 1
        nAndT = file_data[1:x]
        temp = {}
        for i in nAndT:
            place_holder = i.split()
            temp.update({place_holder[0]: place_holder[1]})
        nAndT= temp
        return nAndT
    def connections(self, file_data):
        x = self.numberOfNodes(file_data) + 1
        y = self.numberOfPossibleLinks(file_data)
        connect = file_data[x:x + y]
        temp = []
        for i in connect:
            separate = i.split()
            temp.append((separate[0], separate[1], separate[2]))
        return temp
    def association(self, file_data):
        nodes = file_data[1:self.numberOfNodes(file_data) + 1]
        counter = 1
        index = []
        storesToDistCenter = {}
        for i in nodes:
            if 'dist-center' in i:
                index.append(counter)
            counter+=1
        index.append(len(nodes))
        for a in range(len(index) - 1):
            values = []
            key = file_data[index[a]]
            temp = key.split()
            key = temp[0]
            difference = index[a + 1] - index[a]
            count = index[a] + 1
            for i in range(difference):
                temp1 = file_data[count].split()
                x = temp1[1]
                if(x=='store'):
                    values.append(temp1[0])
                count+=1
                storesToDistCenter.update({key: values})
        return storesToDistCenter
    def sortByWeight(self, file_data):
        temp = sorted(file_data, key = lambda x:x[2]) #https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
        return temp
    def validConnection(self, file_data):
        nameType = self.nameAndType(file_data)
        sortedConnect = self.sortByWeight(self.connections(file_data))
        distCenterToStore = self.association(file_data)
        valid = []
        counter = 0
        possibleLinks = self.numberOfPossibleLinks(file_data) - 1
        for i in sortedConnect:

            start = nameType.get(i[0])

            end = nameType.get(i[1])

            if (start == 'port') and ((end == 'rail-hub') or(end == 'dist-center')):
                valid.append(i)
                counter+=1
            elif (start == 'rail-hub') and ((end == 'rail-hub') or (end == 'dist-center') or (end == 'port')):
                valid.append(i)
                counter+=1
            elif (start == 'dist-center') and ( ((end == 'store') and ((i[1] in distCenterToStore.get(i[0]))))):
                valid.append(i)
                counter+=1
            elif (start == 'dist-center') and ((end == 'rail-hub') or (end == 'port')):
                valid.append(i)
                counter += 1
            elif ((start == 'store') and (end == 'dist-center')) and (i[0] in distCenterToStore.get(i[1])):
                valid.append(i)
                counter+=1
            elif ((start == "store") and (end == "store")):
                valid.append(i)
                counter+=1
            else:
                possibleLinks -= 1
        return valid
    def find(self, parent, a):  # checks to see if the vertices' ID is the same. a and b are dictionary values
        if parent.get(a) == a:
            return a
        else:
            return self.find(parent, parent.get(a))
    def union(self, parent, a, b):
        parent.update({b: parent.get(a)})
    def kruskals(self, file_data):
        disjointsets = {}
        nT = self.nameAndType(file_data)
        keys = list(nT.keys())
        for i in range(len(nT)):
            disjointsets.update({keys[i]: keys[i]})
        edgeWeightSum = 0
        valid = self.validConnection(file_data)
        for i in valid:
            x = self.find(disjointsets, i[0])
            y = self.find(disjointsets, i[1])
            checker = (x == y)
            if checker == False:
                self.union(disjointsets, x, y)
                edgeWeightSum += int(i[2])
        return edgeWeightSum
    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        edgeWeightSum = self.kruskals(file_data)

        # your function to compute the result should be called here

        return edgeWeightSum