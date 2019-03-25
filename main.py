import matplotlib.pyplot as plt
import numpy as np
import math
import os

files_paths = {'src/FIFA20.txt'}


def display_plot_per_letter(freq, alphabet):
    # plot.subplot(212)

    plt.figure(figsize=(10, 5))
    plt.bar(x=alphabet, height=freq)
    plt.show()


def calculate_frequency(text_in, alphabet):
    # print(alphabet)
    # print("file_size = ", some_size)
    text = ""
    for x in text_in:
        text += str(x)
    letters_count = 0
    symbols_count = 0
    text = text.lower()
    # print(text)
    freq = np.zeros(len(alphabet), dtype='int')
    for symb in text:
        pos = -1
        try:
            pos = alphabet.index(symb)
        except ValueError:
            pass
        if pos != -1:
            freq[pos] += 1
            letters_count += 1
        symbols_count += 1
    return (freq, letters_count, symbols_count)


def calculate_entropy(freq, letters_count):
    entropy = 0
    for x in freq:
        if x > 0:
            entropy -= x / letters_count * math.log2(x / letters_count)
    return entropy

def compare_file_size(file_size, entropy, letters_count, symbols_count):
    print("entropy = {1},\nletters_count = {2},\ntotal_symbols_count = {3},\nfile size = {0},".
          format(file_size, entropy, letters_count, symbols_count))
    print("predicted_file_size = {0},".format(entropy * letters_count/2))
    # print("average_size(2bytes=1ukr_letter&enter,1bytes=other_symbols) = {0},"
    #       .format(entropy * (letters_count/4 + (symbols_count-letters_count)/8)))

'''def compare_file_size(file_size, entropy, letters_count, symbols_count):
    print("file size = {0}".
          format(file_size, entropy, letters_count, symbols_count))
    print("predicted_file_size = {0},".format(entropy * letters_count/2))
    # print("average_size(2bytes=1ukr_letter&enter,1bytes=other_symbols) = {0},"
    #       .format(entropy * (letters_count/4 + (symbols_count-letters_count)/8)))'''


archive_name = ('original', 'rar', 'zip', '7-zip','PeaZip')
archive_size_Lina = (909, 679, 720, 767, 767)
archive_size_Astana = (1895, 1229 , 1276 , 1302, 1303)
archive_size_FIFA20 = (2768, 1642, 1642, 1705, 1710)
fn = ('Lina', 'Astana', 'FIFA20')
ao = (909, 1895, 2768)
ar = (679, 1229, 1642)
az = (720, 1276, 1642)
a7 = (767, 1302, 1705)
ap = (767, 1303, 1710)


def display_plot_per_archive():

    fig, ax = plt.subplots()
    index = np.arange(3, 10, 3)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index - 2*bar_width, ao, bar_width,
                     alpha=opacity,
                     color='b',
                     label='original')

    rects2 = plt.bar(index - bar_width, ar, bar_width,
                     alpha=opacity,
                     color='g',
                     label='rar')
    rects3 = plt.bar(index, az, bar_width,
                     alpha=opacity,
                     color='r',
                     label='zip')
    rects4 = plt.bar(index + bar_width, a7, bar_width,
                      alpha=opacity,
                      color='y',
                      label='7-zip')
    rects5 = plt.bar(index + 2*bar_width, ap, bar_width,
                      alpha=opacity,
                      color='black',
                      label='peazip')

    plt.xticks(index, fn)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    for path in files_paths:
        print(path)
        alphabet = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')

        file = open(path, "r", encoding='utf-8', errors='ignore')
        entropy_data = calculate_frequency(file.readlines(), alphabet)
        compare_file_size(os.stat(path).st_size, calculate_entropy(entropy_data[0], entropy_data[1]), entropy_data[1],
                          entropy_data[2])
        display_plot_per_letter(entropy_data[0], alphabet)
        display_plot_per_archive()


