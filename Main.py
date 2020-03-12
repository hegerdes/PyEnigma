import os
import copy
import roman
from Rotor import Rotor, ReverseRotor
from Plugboard import Plugboard

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rotorTransit = {
    1: 16,
    2: 4,
    3: 21,
    4: 99,
    5: 25
}


class Enigma:

    def __init__(self, RotorNumbers=[], RotorPos=[], ReverseRotorNum='B', PlugSet=[]):
        self.rotors = []
        self.plugsSet = False
        ReverseRotorNum.upper()
        if(len(RotorNumbers) != 3):
            self.RotorErr()
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
            else:
                self.RotorErr()

        if(len(RotorPos) != 3):
            self.PosErr()
        for i in range(3):
            if(RotorPos[i] > 25 or RotorPos[i] < 0):
                self.PosErr()
            self.rotors[i].setPos(RotorPos[i])

        if(not (ReverseRotorNum == 'A' or ReverseRotorNum == 'B' or ReverseRotorNum == 'C')):
            self.RevErr()

        self.reverse = ReverseRotor(ReverseRotorNum)

        if(len(PlugSet) == 0):
            self.plugsSet = False
            PlugSet = []
            for i in alphabet:
                PlugSet.append((i, i))
        else:
            self.plugsSet = True
        self.Plugs = Plugboard(PlugSet)

        print('The config for this Enigma is:')
        for i in self.rotors:
            print(i)
        if(self.plugsSet):
            print('Following plugs are set:')
            print(self.Plugs)
        else:
            print('No plugs are set')

    def moveRotos(self):
        self.rotors[0].setPos(self.rotors[0].RotorPos + 1)
        if(self.rotors[0].RotorPos == rotorTransit[self.rotors[0].RotorNum]):
            # print('Switsch1')
            self.rotors[1].setPos(self.rotors[1].RotorPos + 1)
            if(self.rotors[1].RotorPos == rotorTransit[self.rotors[1].RotorNum]):
                # print('Switsch2')
                self.rotors[2].setPos(self.rotors[2].RotorPos + 1)
                if(self.rotors[2].RotorPos == rotorTransit[self.rotors[2].RotorNum]):
                    pass
                    # print('Switsch3')
        for i in self.rotors:
            if(i.RotorPos == 26):
                i.setPos(0)

    def crypt(self, inString):
        outStr = ''
        inString = inString.replace(' ', '').lower()
        for i in inString:
            current = alphabet.index(i)

            current = self.Plugs.run(current)
            # print(self.inText(current))

            for rot in self.rotors:
                current = rot.run(current, True)
                # print(self.inText(current))

            current = self.reverse.run(current)
            # print(self.inText(current))

            self.rotors.reverse()
            for rot in self.rotors:
                current = rot.run(current, False)
                # print(self.inText(current))
            self.rotors.reverse()

            current = self.Plugs.run(current)
            # print(self.inText(current))

            self.moveRotos()
            outStr = outStr + self.inText(current)
        print(outStr)

    def inText(self, index):
        return(alphabet[index])

    def RotorErr(self):
        print('Err1')
        exit(1)

    def PosErr(self):
        print('Err2')
        exit(1)

    def RevErr(self):
        print('Err3')
        exit(1)


if __name__ == '__main__':

    en = Enigma(['IV', 'II', 'III'], [0, 0, 0], 'B')
    en.crypt('Hello das ist ein test')

    en1 = Enigma(['IV', 'II', 'III'], [0, 0, 0], 'B')
    en1.crypt('ruqyjlqvafayhldfam')