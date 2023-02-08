import random
#1. Given a name of 5 characters long, duplicated that name so that each character is repeated twice.
# Ex: Harry --> HHaarrrryy
def duplicateName(name):

    newName = ""
    for char in name:
        newName = newName + (char*2)

    return newName
    
#2. Given a list of numbers. Shuffle (randomize the list), then print out the first, last and middle number in the random list
def shuffle():
    list = [(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100)),(random.randint(1, 100))]
    length = len(list)
    first = list[0]
    last = list[-1]
    mid = list[length//2]
    return list, first, last, mid                                                                                                                                                                                            
                                                                                                                                                                                                  

                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                             
                                                                                                                                                                                                             
                                                                                                                                                                                                             
                                                                                                                                                                                                             
    

def main():

    #call all of the methods defined
    print(duplicateName(input("Enter a 5-letter name: ")))
    print(shuffle())



if __name__=="__main__":
    main()
