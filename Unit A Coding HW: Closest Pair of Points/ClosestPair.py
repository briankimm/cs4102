import math
import sys
# CS4102 Spring 2022 - Unit A Programming
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
# Your Computing ID: byk6q
# Collaborators: my6jdq
# Sources: Introduction to Algorithms, Cormen
#################################

class ClosestPair:
    def __init__(self):
        return
    def convert(self, file_data):
        converted = []
        for i in file_data:
            temp = i.split()
            converted.append((float(temp[0]), float(temp[1])))
        return converted
    def sortX(self, file_data):
        sortedXList = self.convert(file_data)
        return sorted(sortedXList)
    def runwayPoints(self, file_data, delta, med):
        pointsInRunway = []
        for i in file_data:
            if i[0] >= med - delta and i[0] <= med or i[0] <= med + delta and i[0] >= med:
                pointsInRunway.append(i)
        return pointsInRunway
    def getMedian(self, a):
        median = len(a)//2
        if(len(a) % 2 != 0):
            median = a[median][0]
        else:
            median = (a[median][0] + a[median - 1][0]) / 2
        return median
    def distance(self,point1, point2):
        return math.sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2))
    def bruteForce(self, subList):
        smallestMin = sys.float_info.max
        secondSmallestMin = sys.float_info.max
        for i in range(len(subList)-1):
            for j in range(i + 1, len(subList)):
                if(self.distance(subList[i], subList[j]) < smallestMin):
                    secondSmallestMin = smallestMin
                    smallestMin = self.distance(subList[i],subList[j])
                elif(self.distance(subList[i], subList[j])<secondSmallestMin):
                    secondSmallestMin = self.distance(subList[i], subList[j])
        return (smallestMin, secondSmallestMin)
    def findMins(self, subList):
        if(len(subList)<=3):
            return self.bruteForce(subList)
        median = self.getMedian(subList)
        mid = len(subList) // 2
        sublistLeft = subList[:mid]
        sublistRight = subList[mid:]
        distanceLeft = self.findMins(sublistLeft) # combine these two is the second smallest and smallest of each subList
        distanceRight = self.findMins(sublistRight)
        xMins = [distanceLeft[0], distanceLeft[1],distanceRight[0],distanceRight[1]]
        sortedXMins = sorted(xMins)
        twoSmallestDistances = [sortedXMins[0], sortedXMins[1]]
        minLeft = min(distanceLeft[0], distanceLeft[1])
        minRight = min(distanceRight[0], distanceRight[1])
        runwayDistance = max(minLeft, minRight)
        runway = self.runwayPoints(subList, runwayDistance, median)
       # sorted by y-coordinate
        sortedRunwayPoints = sorted(runway, key=lambda i: i[-1])#https://pythonguides.com/python-sort-list-of-tuples/#:~:text=To%20sort%20the%20list%20of%20tuples%20by%20descending%20order%20we,of%20the%20sort()%20method.
        for i in sortedRunwayPoints:
            counter = 1
            while counter < 8 and sortedRunwayPoints.index(i) + counter < len(sortedRunwayPoints):
                temp = [i, sortedRunwayPoints[counter+sortedRunwayPoints.index(i)]]
                yMin = self.distance(temp[0], temp[1])
                if(yMin < twoSmallestDistances[0] and yMin != 0 ):
                    twoSmallestDistances[1] = twoSmallestDistances[0]
                    twoSmallestDistances[0] = yMin
                elif(yMin < twoSmallestDistances[1] and yMin != twoSmallestDistances[0] and yMin !=0):
                    twoSmallestDistances[1] = yMin
                counter+=1
        return twoSmallestDistances






    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1
    def compute(self, file_data):
        twoSmallestDistances = self.findMins(self.sortX(file_data))
        closest = twoSmallestDistances[0]
        secondClosest = twoSmallestDistances[1]
        return [closest, secondClosest]
