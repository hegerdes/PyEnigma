#!/usr/bin/env python3
import roman
import argparse
import sys
import logging
from typing import List, Tuple
from lib.rotor import Rotor, ReverseRotor
from lib.plugboard import Plugboard

logger = logging.getLogger("hegerdes::pyenigma")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rotorTransit = {
    1: 16,
    2: 4,
    3: 21,
    4: 99,
    5: 25
}


class Enigma:
    def __init__(self, RotorNumbers: List[str] = [], RotorPos: List[int] = [], ReverseRotorNum: str = 'B', PlugSet: List[Tuple] = []):
        self.rotors = []
        self.plugsSet = False
        ReverseRotorNum.upper()
        if (len(RotorNumbers) != 3):
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

        if (len(RotorPos) != 3):
            self.PosErr()

        for i in range(3):
            if (RotorPos[i] > 25 or RotorPos[i] < 0):
                self.PosErr()
            self.rotors[i].setPos(RotorPos[i])

        if (not (ReverseRotorNum == 'A' or ReverseRotorNum == 'B' or ReverseRotorNum == 'C')):
            self.RevErr()

        self.reverse = ReverseRotor(ReverseRotorNum)

        if (len(PlugSet) == 0):
            self.plugsSet = False
            PlugSet = []
            for i in ALPHABET:
                PlugSet.append((i, i))
        else:
            self.plugsSet = True
        self.Plugs = Plugboard(PlugSet)

        logger.debug('The config for this Enigma is:')
        for i in self.rotors:
            logger.debug(i)
        if (self.plugsSet):
            logger.debug('Following plugs are set:')
            logger.debug(self.Plugs)
        else:
            logger.debug('No plugs are set')

    def moveRotos(self):
        self.rotors[0].setPos(self.rotors[0].RotorPos + 1)
        if (self.rotors[0].RotorPos == rotorTransit[self.rotors[0].RotorNum]):
            self.rotors[1].setPos(self.rotors[1].RotorPos + 1)
            if (self.rotors[1].RotorPos == rotorTransit[self.rotors[1].RotorNum]):
                self.rotors[2].setPos(self.rotors[2].RotorPos + 1)
                if (self.rotors[2].RotorPos == rotorTransit[self.rotors[2].RotorNum]):
                    pass

        for i in self.rotors:
            if (i.RotorPos == 26):
                i.setPos(0)

    def crypt(self, inString: str) -> str:
        outStr = ''
        inString = inString.replace(' ', '').lower()
        for i in inString:
            current = ALPHABET.index(i)

            current = self.Plugs.run(current)
            # logger.info(self.inText(current))

            for rot in self.rotors:
                current = rot.run(current, True)

            current = self.reverse.run(current)

            self.rotors.reverse()
            for rot in self.rotors:
                current = rot.run(current, False)
            self.rotors.reverse()

            current = self.Plugs.run(current)
            # logger.info(self.inText(current))

            self.moveRotos()
            outStr = outStr + self.inText(current)
        return outStr

    def inText(self, index):
        return (ALPHABET[index])

    def setPlugs(self, Plugs):
        self.Plugs.setPlugs(Plugs)

    def randomPlugs(self, plug_amount=26):
        return self.Plugs.randomPlugs(plug_amount)

    def RotorErr(self):
        logger.error('Err1')
        exit(1)

    def PosErr(self):
        logger.error('Err2')
        exit(1)

    def RevErr(self):
        logger.error('Err3')
        exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PyEnigma',
        description='Fun CLI-Project that implements the Enigma, used in WW2 in, software.',
        epilog='Author: hegerdes')

    parser.add_argument('-i', '--input', default="")
    parser.add_argument('-v', '--verbose',
                        action='store_true')

    args = parser.parse_args()

    input_text = args.input
    if (args.verbose):
        logger.setLevel(logging.DEBUG)
    if (len(input_text) <= 0):
        input_text = input("Provide a strimg to encrypt/decrypt: ")

    en1 = Enigma(['IV', 'II', 'III'], [0, 0, 0], 'B')
    cyther = en1.crypt(input_text)
    logger.info('Encryped: {}'.format(cyther))

    en2 = Enigma(['IV', 'II', 'III'], [0, 0, 0], 'B')
    dcyther = en2.crypt(cyther)
    logger.info('Decryped: {}'.format(dcyther))
