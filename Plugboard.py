import random
import os
import copy

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Plugboard:

    def __init__(self, plugs = None):
        self.board = {}
        for i in alphabet:
            self.board[i] = None
        if (plugs):
            self.setPlugs(plugs)
        else:
            self.randomPlugs()


    def randomPlugs(self, plug_amount = 26):
        if(plug_amount%2 != 0):
            print("Need to be an even number of plugs")
            exit(1)

        tmp = copy.deepcopy(alphabet)
        random.shuffle(tmp)

        while (len(tmp) > 26- plug_amount):
            num1 = tmp[random.randint(1, len(tmp)) - 1]
            num2 = tmp[random.randint(1, len(tmp)) - 1]

            if (num1 != num2):
                self.board[num1] = num2
                self.board[num2] = num1
                tmp.remove(num1)
                tmp.remove(num2)

    def setPlugs(self, plugs):
        for i in plugs:
            self.board[i[0]] = i[1]
            self.board[i[1]] = i[0]

    def run(self, inputChar):
        out = alphabet.index(self.board[alphabet[inputChar]])
        if( out != None): return out
        return inputChar