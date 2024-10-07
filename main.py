import random
import time


class Mathematics :
    def __init__(self):
        self.calculates = {}
        self.calculates['getting_two_numbers_together'] = []

    def randomNumber(self,min,max):
        count = 0
        return random.randint(min,max)



    """
    guess strategy
    """
    def getting_two_numbers_together(self,lap = 1,total = 0):
        if (lap) == total + 1 or (lap) < total:
            compeleted = 0
            while lap > compeleted:
                while len(self.calculates['getting_two_numbers_together']) < lap:
                    their_sum = self.randomNumber(0, total);
                    compeleted = compeleted + 1;
                    guess = self.randomNumber(0, total - their_sum);
                    mode = []
                    if (guess + their_sum) == total and not [guess, their_sum] in self.calculates['getting_two_numbers_together']:
                        mode.append(guess)
                        mode.append(their_sum)
                        self.calculates['getting_two_numbers_together'].append(mode)
                    else:
                        pass

        else:
            print("There are not so many modes")

        i = 0
        for items in self.calculates['getting_two_numbers_together']:
            i = i + 1
            print(f"[ {i}: {items[0]} + {items[1]} = {items[0] + items[1]} ]")

        self.calculates['getting_two_numbers_together'] = []
        print(f"{i} modes")








