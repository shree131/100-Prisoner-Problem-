import sys
import random

## List representing prisoners
prisoners = list(range(1, 11))

## List representing drawers
drawers = list(range(1, 11))

## Randomly assign each prisoner to each drawer
random.shuffle(drawers)




def chooseDrawers(p, found, n):

    ## Represents choices
    c = 1
    found = False

    list1 = []

    
    while c <= n and (found == False): ## Prisoner doesn't open any more drawers if he finds his number
        
        ## Choose a random drawer
        choice = random.choice(drawers)

        ## Check if prisoner found his number
        if choice == p:
            found = True

        ## Make sure prisoner chose a drawer that he hasn't picked before
        if choice in list1:
            ## Discard the choice and let him pick again
            n += 1

        else:
            list1.append(choice)
            print("Choice: ", choice, "=? ", p)
            print(found, "\n")
            
                
        c += 1
    return found


## The 100 Prisoner Problem Simulation
def prisonerProblem():
 

    p = 1
    flag = True

    ## All prisoner chooses 50 drawers
    while p <= len(prisoners) and flag:

        print("Prisoner #", p, "\n")
        flag = chooseDrawers(p, flag, 5)

            
        ## Clear the prisoner's choices
        ## list2.clear()
        print("------------------------------------")
        
        ## Move to the next prisoner
        p += 1

    ## Return if successful or not
    return flag       


                
def main():

    success = 0;

    n = 101

    ## Run prisoner problem X10 Mil.
    for i in range(1, n):
        print("Trail #", i, "\n\n")
        if prisonerProblem():
            success += 1
        print("\n")    
    successRate = (success / n) * 100
    
    print("No. of successes in ", n-1, " trials: ", success)
    print("Success rate: ", successRate, "%")



main()







    
