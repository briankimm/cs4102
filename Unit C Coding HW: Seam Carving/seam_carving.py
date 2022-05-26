import math
# CS4102 Spring 2022 -- Unit C Programming
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
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
class SeamCarving:
    def __init__(self):
        self.seam_builder = []
        return
    def length(self, file_data):#x
        return len(file_data[0])
    def width(self, file_data):#y
        return len(file_data)
    def difference(self, pixel1, pixel2):#takes in the pixel itself ([0,0,0])
        return math.sqrt((pixel2[0] - pixel1[0])**2 + (pixel2[1] - pixel1[1])**2 + (pixel2[2] - pixel1[2])**2)
    def weight(self,image):
        y = self.width(image)
        x = self.length(image)
        seam_builder = []
        for i in range(y):
            seam_builder.append([])
        for i in reversed(range(y)):
            for j in range(x):
                total_energy = 0
                counter = 0
                if(i!= 0):#checks to see if there is a pixel to the north of it
                    total_energy += self.difference(image[i][j], image[i-1][j])
                    counter+=1
                    if(j!=x-1):#northeast
                        total_energy += self.difference(image[i][j], image[i -1][j +1])
                        counter += 1
                if(j!=x-1):#east
                    total_energy += self.difference(image[i][j], image[i][j+1])
                    counter+=1
                    if(i!=y-1):#southeast
                        total_energy += self.difference(image[i][j], image[i+1][j+1])
                        counter+=1
                if(i!=y-1):#south
                    total_energy+= self.difference(image[i][j], image[i+1][j])
                    counter +=1
                    if(j!=0):#southeast
                        total_energy+=self.difference(image[i][j], image[i+1][j-1])
                        counter+=1
                if(j!=0):#west
                    total_energy+=self.difference(image[i][j], image[i][j-1])
                    counter += 1
                    if(i!=0):#northwest
                        total_energy += self.difference(image[i][j], image[i-1][j-1])
                        counter+=1
                average_energy = total_energy / counter
                if(i!=y-1):#checks to see if bottom row
                    if(j!=0 and j!=x-1):#checks to see if it is in between the edges
                        seam_builder[i].append(average_energy + min(seam_builder[i+1][j+1], seam_builder[i+1][j], seam_builder[i+1][j-1]))
                    elif(j == (x-1)):#right edge
                        seam_builder[i].append(average_energy + min(seam_builder[i+1][j], seam_builder[i+1][j-1]))
                    elif(j==0):#leftedge
                        seam_builder[i].append(average_energy + min(seam_builder[i+1][j+1], seam_builder[i+1][j]))
                else:
                    seam_builder[i].append(average_energy)
        self.seam_builder = seam_builder
        # return seam_builder
    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        self.weight(image)
        energy = self.seam_builder
        return min(energy[0])

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        image = self.seam_builder
        min_value = min(image[0])
        index = []
        x_coordinates = []
        for i in range(len(image[0])):
            if(min_value == image[0][i]):
                index.append(i)
        min_index = int(index[0])
        x_coordinates.append(min_index)
        counter = 1
        while(counter < len(image)):
            connection = []
            if(min_index !=0 and min_index!=len(image[0])-1):
                min_value = min(image[counter][min_index -1], image[counter][min_index], image[counter][min_index+1])
                for i in range(-1,2):
                    if min_value == image[counter][min_index + i]:
                        connection.append(min_index + i)
                min_index = int(connection[0])
                counter+=1
                x_coordinates.append(min_index)
            elif(min_index == 0):
                min_value = min(image[counter][min_index], image[counter][min_index+1])
                for i in range(0,2):
                    if min_value == image[counter][min_index + i]:
                        connection.append(min_index + i)
                min_index = int(connection[0])
                counter+=1
                x_coordinates.append(min_index)
            elif(min_index == len(image[0])-1):
                min_value = min(image[counter][min_index -1], image[counter][min_index])
                for i in range(-1,1):
                    if min_value == image[counter][min_index + i]:
                        connection.append(min_index + i)
                min_index = int(connection[0])
                counter+=1
                x_coordinates.append(min_index)
        return x_coordinates


