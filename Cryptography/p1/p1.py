#!/usr/bin/env python3

import matplotlib.pyplot as plt
import string
import argparse

letter2num = dict(zip(string.ascii_uppercase, range(0, 26)))
num2letter = {v: k for k, v in letter2num.items()}


def prepare_text(input_txt: str) -> str:
    return ''.join([c.upper() for c in input_txt if c.isalpha()])


def encrypt(plain_txt: str, cypher_key: int) -> str:
    # convert to only uppercase english letters
    processed_txt = prepare_text(plain_txt)
    # convert to numbers
    input_nums = [letter2num[letter] for letter in processed_txt]
    # shift numbers with cypher key
    cypher_nums = [(num + cypher_key) % 26 for num in input_nums]
    # convert back to uppercase english letters
    cypher_text = ''.join([num2letter[num] for num in cypher_nums])
    print(f'cypher text: {cypher_text}')
    return cypher_text


def decrypt(cypher_txt: str, cypher_key: int) -> str:
    # convert to numbers
    cypher_nums = [letter2num[letter.upper()] for letter in cypher_txt]
    # shift numbers with cypher key
    text_nums = [(num - cypher_key) % 26 for num in cypher_nums]
    # convert back to english letters to get original message
    plain_txt = ''.join([num2letter[num] for num in text_nums])
    print(f'plain text: {plain_txt}')
    return plain_txt

def get_letter_freq(text: str) -> str:
    # convert to only uppercase english letters
    plain_text = prepare_text(text)
    # create map that contains all letters & the times repeated in the text, start all at 0
    letter_freq = dict(zip(string.ascii_uppercase, [0]*len(string.ascii_uppercase)))
    # iterate over the text
    for letter in plain_text:
        # add 1 to the frequencies map
        letter_freq[letter] += 1
    print(letter_freq)
    return letter_freq

def generate_bar_plot(letter_freq: map):
    letters = letter_freq.keys()
    frequency = letter_freq.values()
    # create bar plot
    plt.figure(figsize = (20, 10))
    bars = plt.bar(letters, frequency, color ='gray', width = 0.5)
    plt.xlabel("Letters (A-Z)")
    plt.ylabel("No. of times in text")
    plt.title("Frequency of Letters in Text")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + 1, yval)

    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='encrypt or decrypt using the Caesar cypher!')
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_a = subparsers.add_parser('encrypt', help='encrypt help')
    parser_a.add_argument('--message', type=str, required=True, help='message to encrypt/decrypt')
    parser_a.add_argument('--cypher-key', type=int, required=True, help='Caesar cypher key to encrypt/decrypt')
    parser_a.set_defaults(func=encrypt)
    parser_b = subparsers.add_parser('decrypt', help='decrypt help')
    parser_b.add_argument('--message', type=str, required=True, help='message to encrypt/decrypt')
    parser_b.add_argument('--cypher-key', type=int, required=True, help='Caesar cypher key to encrypt/decrypt')
    parser_b.set_defaults(func=decrypt)

    args = parser.parse_args()
    args.func(args.message, args.cypher_key)
