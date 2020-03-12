import os
import roman
from Rotor import Rotor, ReverseRotor
from Plugboard import Plugboard

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
plugs = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h'), ('i', 'j'), ('k', 'l'),
         ('m', 'n'), ('o', 'p'), ('q', 'r'), ('s', 't'), ('u', 'v'), ('w', 'x'), ('y', 'z')]

rotorTransit = {
    1: 17,
    2: 5,
    3: 21,
    4: 10,
    5: 26
}


class Enigma:

    def __init__(self, RotorNumbers = [], RotorPos = [], Plugboard = []):
        self.rotors = []
        if(len(RotorNumbers) != 3): self.RotorErr()
        usedRotors = []
        for i in RotorNumbers:
            num = None
            if str == type(i):
                num = roman.fromRoman(i.upper())
            else:
                num = int(i)
            if not num in usedRotors:
                usedRotors.append(num)
                self.rotors.append(Rotor(num))
            else: self.RotorErr()

        if(len(RotorPos) != 3): self.PosErr()
        for i in range(3):
            if(RotorPos[i] > 25 or RotorPos[i] < 0): self.PosErr()
            self.rotors[i].setPos(RotorPos[i])

        for i in self.rotors:
            print(i)




    def RotorErr(self):
      print('Err')
      exit(1)

    def PosErr(self):
      print('Err')
      exit(1)

if __name__ == '__main__':

    en = Enigma(['III', 'I', 'II'], [1,2,3])


    rotor1 = Rotor(1, 0)
    rotor2 = Rotor(2, 0)
    rotor3 = Rotor(3, 0)
    board = Plugboard(plugs)

    endRotor = ReverseRotor('B')

    def moveRotos():
        rotor1.setPos(rotor1.RotorPos + 1)
        if(rotor1.RotorPos == 26):
            rotor1.setPos(0)
            rotor2.setPos(rotor2.RotorPos + 1)
            if(rotor2.RotorPos == 26):
                rotor2.setPos(0)
                rotor3.setPos(rotor2.RotorPos + 1)
                if(rotor3.RotorPos == 26):
                    rotor3.setPos(0)

    def inText(index):
        return(alphabet[index])

    while(True):
        command = input('One Char please\n')
        command = command.rstrip("\n").lower()

        for i in command:
            current = alphabet.index(i)

            current = board.run(current)
            print(inText(current))

            current = rotor1.run(current, True)
            print(inText(current))
            current = rotor2.run(current, True)
            print(inText(current))
            current = rotor3.run(current, True)
            print(inText(current))
            current = endRotor.run(current)
            print(inText(current))
            current = rotor3.run(current, False)
            print(inText(current))
            current = rotor2.run(current, False)
            print(inText(current))
            current = rotor1.run(current, False)

            print(inText(current))
            current = board.run(current)

            print(inText(current), end='')
            moveRotos()

        print()
