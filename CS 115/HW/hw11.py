''' "I pledge my honor that I have abided by the Stevens Honor System" - Jonathan Joshua'''
# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:
            print("You did it, you really won against me!?!?")
            print("That ain't no problem!!! BEST 2 OUT OF 3, YOU WON'T :)")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            print("HAHAHAHA in your face punitive human.")
            print("I see no other GOD up here other than MEEE...")
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    while True:
        num_piles = int(input("How many piles are we playing with? "))
        if num_piles > 0:
            break
        print("Please give a valid number")     
    piles = [0] * num_piles
    for var in range(len(piles)):
        while True:
            ans = int(input("How many  are in pile " + str(var) + "? "))
            if ans >= 0:
                break
            print("Please give a valid number")
        piles[var] = ans

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    var = 0
    while var < len(piles):
        print("pile " + str(var) + " = " + str(piles[var]))
        var += 1


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles
    while (True):
        chosen = int(input("Which pile? "))
        if chosen in range(num_piles) and piles[chosen] > 0:
            return chosen


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    chosen = int(input("How many coins? "))
    while chosen not in (map(lambda x: x +1, range(piles[pnum]))):
        chosen = int(input("Amount invalid!! Give another one. "))
    return chosen


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles
    n = 0
    for pile in piles:
        n = n ^ pile
    return n


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles
    n = game_nim_sum()
    for pile in range(num_piles):
        if (piles[pile] ^ n < piles[pile]):
            return (pile, piles[pile] - (piles[pile] ^ game_nim_sum()))
    for pile in range(num_piles):
        if (piles[pile] > 0):
            return (pile, 1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles
    greatest_play = opt_play()
    piles[greatest_play[0]] = piles[greatest_play[0]] - greatest_play[1]
    print("My turn ... prepare to be dazzled!!!")
    print("I take away " + str(greatest_play[1]) + " from the pile " + str(greatest_play[0]))
    


#   start playing automatically
if __name__ == "__main__" : play_nim()
