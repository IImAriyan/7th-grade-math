import random
import time


class Mathematics :
    def __init__(self):
        self.calculates = {}
        self.calculates['getting_two_numbers_together'] = []
        self.calculates['getting_three_numbers_together'] = []
        self.calculates['get_all_two_numbers_mods'] = []
        self.calculates['get_all_three_numbers_mods'] = []


    def randomNumber(self,min:int,max:int):
        return random.randint(min,max)



    """
    guess strategy
    """


    def get_all_two_numbers_mods(self,total:int):
        while len(self.calculates['get_all_two_numbers_mods']) < total + 1:
            mode = []
            guess = self.randomNumber(min=0,max=total)
            guess2 = self.randomNumber(min=0,max=total)
            if not [guess,guess2] in self.calculates['get_all_two_numbers_mods'] and (guess + guess2) == total:
                mode.append(guess)
                mode.append(guess2)
                self.calculates['get_all_two_numbers_mods'].append(mode)

        calculated = self.calculates['get_all_two_numbers_mods']
        self.calculates['get_all_two_numbers_mods'] = []
        return len(calculated)



    def get_all_three_numbers_mods(self,total:int) :
        count = 0
        for a in range(total + 1):
            for b in range(total + 1 - a):
                c = total - a - b
                if c >= 0 :
                    count += 1
        return count




    def getting_two_numbers_together(self,lap= 1,total = 0):
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
            print("There are not so many modes")

        i = 0

        for items in self.calculates['getting_two_numbers_together']:
            i = i + 1
            print(f" [ {i}: {items[0]} + {items[1]} = {items[0] + items[1]} ]")

        self.calculates['getting_two_numbers_together'] = []
        print(f"{i} modes")

    def getting_three_numbers_together(self,lap = 1,total = 0):
        compeleted = 0
        while lap > compeleted:
            while len(self.calculates['getting_three_numbers_together']) < lap:
                their_sum = self.randomNumber(0, total);
                compeleted = compeleted + 1;
                guess = self.randomNumber(0, total - their_sum);
                guess2 = self.randomNumber(0, total - their_sum);
                mode = []
                if (guess + their_sum + guess2) == total and not [guess, their_sum, guess2] in self.calculates['getting_three_numbers_together']:
                    mode.append(guess)
                    mode.append(their_sum)
                    mode.append(guess2)
                    self.calculates['getting_three_numbers_together'].append(mode)


        i = 0

        for items in self.calculates['getting_three_numbers_together']:
            i = i + 1
            print(f" [ {i}: {items[0]} + {items[1]} + {items[2]} = {items[0] + items[1] + items[2]} ]")

        self.calculates['getting_three_numbers_together'] = []
        print(f"{i} modes")


math = Mathematics()



print(math.get_all_three_numbers_mods(50))






