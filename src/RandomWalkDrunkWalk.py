import matplotlib.pyplot as plt
import random

def random_walk(length):
    x,y = 0,0
    walkx,walky = [x],[y]
    for i in xrange(length):
        new = random.randint(1,2)
        if new == 1:
            x -= 1
        elif new == 2:
            x += 1
        y +=1
        walkx.append(x)
        walky.append(y)
    return [walkx,walky]
def random_walk_2020(length):
    x,y = 0,0
    walkx,walky = [x],[y]
    for i in xrange(length):
        new = random.randint(1,2)
        if new == 1:
            if x == -20:
                x = 20
            else:
                x -= 1
        elif new == 2:
            if x == 20:
                x = -20
            else:
                x += 1
        y +=1
        walkx.append(x)
        walky.append(y)
    return [walkx,walky]

def main():
    number_of_iteration =500
    walk_coordinates = random_walk(number_of_iteration)
    plt.plot(walk_coordinates[0],walk_coordinates[1],'-o', label= 'Random walk')
    plt.axis([min(walk_coordinates[0])-10,max(walk_coordinates[0])+10,0,number_of_iteration+10])
    plt.grid(True)
    plt.show()
    
    walk_coordinates_2020 = random_walk_2020(number_of_iteration)
    plt.plot(walk_coordinates_2020[0],walk_coordinates_2020[1],'-o', label= 'Random walk')
    plt.axis([-20,+20,0,number_of_iteration+10])
    plt.grid(True)
    plt.show()
    
if __name__ == '__main__':
    main()
