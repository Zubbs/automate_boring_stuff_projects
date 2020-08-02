import random, time, copy

#first create cells

indexCells = []

width = 30 
height = 10
import random, time, copy

#first create cells

indexCells = []

width = 30 
height = 10

for x in range(width):
    col = []
    for y in range(height):
        if random.randint(0,1) == 0:
            col.append('0')
        else:
            col.append('*')
    
    indexCells.append(col)



#Main program

while True:

    print('\n \n')

    nextcell = copy.deepcopy(indexCells)

    for y in range(height):
        for x in range(width):
            print(nextcell[x][y], end = '')
        print()   #to give a space after every row



    for x in range(width):
        for y in range(height):
            leftcord = (x-1) % width 
            rightcord = (x+1) % width
            upcord = (y-1) % height
            downcord = (y+1) % height

        
            num_of_live_neighbours = 0

            #check each neigbour

            if nextcell[leftcord][upcord] == '*':
                num_of_live_neighbours += 1
            if nextcell[x][upcord] == '*':
                num_of_live_neighbours += 1
            if nextcell[rightcord][upcord] == '*':
                num_of_live_neighbours += 1
            if nextcell[leftcord][y] == '*':
                num_of_live_neighbours += 1
            if nextcell[rightcord][y] == '*':
                num_of_live_neighbours += 1
            if nextcell[leftcord][downcord] == '*':
                num_of_live_neighbours += 1
            if nextcell[x][downcord] == '*':
                num_of_live_neighbours += 1
            if nextcell[rightcord][downcord] == '*':
                num_of_live_neighbours += 1
            

            #checking game of life

            if nextcell[x][y] == '*' and (num_of_live_neighbours == 3 or num_of_live_neighbours == 2):
                indexCells[x][y] = '*'


            elif nextcell[x][y] == '0' and num_of_live_neighbours == 3:
                indexCells[x][y] = '*'

            else:
                indexCells[x][y] = '0'
            

    time.sleep(1)


          

