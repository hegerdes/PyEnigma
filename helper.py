rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'VZBRGITYUPSDNHLXAWMJQOFECK']
reversedRotor = ['EJMZALYXVBWFCRQUONTSPIKHGD', 'YRUHQSLDPXNGOKMIEBFZCWVJAT', 'FVPJIAOYEDRZXWGCTKUQSBNMHL']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for wirering in rotors:
    wirering = wirering.lower()
    print('[', end='')
    for i in range(0,26):
        for j in range(0,26):
            if(wirering[i] == alphabet[j]):
                print('[', end='')
                print(i, end=', ')
                print(j, end='], ')
    print(']')