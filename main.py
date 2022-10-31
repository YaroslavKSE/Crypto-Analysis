import operator

import matplotlib.pyplot as plt

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

encrypted_file = open("e11.txt.", "r")

encrypted_Text = encrypted_file.read()

relative_frequency = {"a": 8.2, "b": 1.5, "c": 2.8, "d": 4.3, "e": 13, "f": 2.2, "g": 2, "h": 6.1, "i": 7,
                      "j": 0.15, "k": 0.77, "l": 4, "m": 2.4, "n": 6.7, "o": 7.5, "p": 1.8, "q": 0.095, "r": 6,
                      "s": 6.3, "t": 9.1, "u": 2.8, "v": 0.98, "w": 2.4, "x": 0.15, "y": 2, "z": 0.074}


def calculate_frequency(text):
    dictionary = {}
    for element in text:
        if element.isalpha():
            if element.lower() not in dictionary:
                dictionary[element.lower()] = 1
            else:
                dictionary[element.lower()] += 1
    return dictionary


def draw_polygon():
    plt.plot(frequency_dict.keys(), frequency_dict.values())
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Frequency polygon")
    plt.show()


def calculate_relative_frequency(dictionary):
    total = 0
    cipher_relative_freq = {}
    for element in dictionary.values():
        total += element
    for element in dictionary:
        occurrence = dictionary[element]
        pers = occurrence / total * 100
        cipher_relative_freq[element] = pers

    return cipher_relative_freq


def decrypt_cipher():
    key = 1
    brute_list = []
    temporary = ""
    while key != 26:
        for letter in encrypted_Text:
            if letter.isalpha():
                index = letters.index(letter.lower())
                if index - key >= 0:
                    temporary += letters[index - key]
                else:
                    temporary += letters[25 + (index - key % 26)]
        freq = calculate_frequency(temporary)
        rel_freq = calculate_relative_frequency(freq)
        rel_freq = {key: value for key, value in sorted(rel_freq.items())}
        brute_list.append(rel_freq)
        temporary = ""
        key += 1
    return brute_list


def find_key(rel_freq_list):
    differences = []
    for element in rel_freq_list:
        difference_list = list(map(operator.sub, element.values(), relative_freq.values()))
        difference = 0
        for number in difference_list:
            difference += number
        differences.append(difference)
    indexes = []
    while len(indexes) < 3:
        if len(indexes) == 0:
            indexes.append(differences.index(min(differences)) + 1)
        if len(indexes) == 1:
            indexes.append(differences.index(min(differences)) + 2)
        else:
            indexes.append(differences.index(min(differences)) + 3)
    return indexes


frequency_dict = calculate_frequency(encrypted_Text)
frequency_dict = {key: value for key, value in sorted(frequency_dict.items())}
print(frequency_dict)

relative_freq = calculate_relative_frequency(frequency_dict)
print(relative_freq)

brute = decrypt_cipher()
print(brute)

print("Possible keys:", find_key(brute))

draw_polygon()
