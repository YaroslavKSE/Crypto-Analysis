import matplotlib.pyplot as plt

encrypted_file = open("e.txt.", "r")

encrypted_Text = encrypted_file.read()

frequency_dict = {}


def calculate_frequency():
    for element in encrypted_Text:
        if element.isalpha():
            if element.lower() not in frequency_dict:
                frequency_dict[element.lower()] = 1
            else:
                frequency_dict[element.lower()] += 1


def find_top_frequency():
    list_of_values = []
    while len(list_of_values) != 3:
        max_value = max(frequency_dict.values())
        list_of_values.append(max_value)
        for key, value in frequency_dict.items():
            if value == max_value:
                frequency_dict.pop(key)
                break
    return list_of_values


def draw_polygon():
    frequencies = list(frequency_dict.values())
    plt.plot(frequencies)
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Frequency polygon")
    plt.show()


calculate_frequency()
find_top_frequency()
draw_polygon()


