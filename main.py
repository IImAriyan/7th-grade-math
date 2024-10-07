import random


class Mathematics :
    def __init__(self):
        self.calculates = {}
        self.calculates['getting_two_numbers_together'] = []
        self.calculates['getting_three_numbers_together'] = []


    def randomNumber(self,min:int,max:int):
        return random.randint(min,max)



    """
    guess strategy
    """



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


math.getting_three_numbers_together(78,11)
math.getting_two_numbers_together(10,11)

10*7 + 1




