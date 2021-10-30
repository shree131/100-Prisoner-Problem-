import sys
import random

## List representing prisoners
prisoners = list(range(0, 100))

## List representing drawers
drawers = list(range(0, 100))

## Randomly assign each prisoner to each drawer
random.shuffle(drawers)

def chooseDrawers(p, found, n): 
    c = 0
    found = False
    choice = p 


    while c < n and (found == False): ## Exit loop as soon as prisoner finds his number

        print("Drawer #", choice, "'s value (", drawers[choice], ") =?", p)

        ## If drawer matches his number
        if drawers[choice] == p: 
            found = True

            
        else:
            choice = drawers[choice] ## Use value of current drawer to look for next drawer no.
        
        
        print(found, "\n")

        c += 1
        
    ## Return if prisoner found his number in the given no. of boxes
    return found
    

def givenMethod():
    p = 0
    successFlag = True
    
    ## All prisoners choose 50 drawers
    while p < 10 and successFlag: ## The trail ends if a single prisoner can't find his number in 50 tries
        
        print("Prisoner #", p, "\n")

        ## Call chooseDrawers()
        successFlag = chooseDrawers(p, successFlag, 50) 

        print("-------------------------------------")

        p += 1 ## Move to next prisoner

    ## return if the trail was successful
    return successFlag
        

def main():
    success = 0;

    n = 101

    for i in range(1, n):
        print("Trail #", i, ": \n\n")

        if givenMethod():
            print("Trail #", i, "successful")
            success += 1 ## Add up no. of successes for all trials
        else:
            print("Trail #", i, "unsuccessful")
        print("\n")

    ## Calculate success rate
    successRate = (success/n) * 100
    
    print("No. of successes in ", n-1, " trials: ", success)
    print("Success rate: ", successRate, "%")


## Call main method
main()

    
