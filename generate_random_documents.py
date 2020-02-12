#!/usr/bin/env python3

"""
Script:	random_documents.py
Date:	2018-09-30

Platform: MacOS

Description:
Creates a random text (language like) document.
With no parameters, it outputs to screen
With a file specified, it will output to file

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Developer'

import random
import optparse


def main(gen_type, length, file_path):
    """
    Generate content based on type and length and optionally save
    :param gen_type: (string) words, sentences, paragraphs, or documents
    :param length: (int) Length of the type
    :param file_path: (string) Optional save file
    :return: (void)
    """
    if gen_type == 'words':
        if length == 0:
            length = random.randint(0, 25)
        contents = generate_word(length, length)
    elif gen_type == 'sentences':
        contents = generate_sentence(length)
    elif gen_type == 'paragraphs':
        contents = generate_paragraph(length)
    else:
        contents = generate_document(length)

    if file_path is None:
        print(contents)
    else:
        try:
            with open(file_path, 'w+') as save_file:
                save_file.write(contents)
        except Exception as err:
            print('Error saving file\n{}'.format(err))


def generate_word(min_length=3, max_length=15, capital=False):
    """
    Generate a word in a typical word structure
    :param min_length: (int) Minimum length
    :param max_length: (int) Maximum length
    :param capital: (bool) Capitilise
    :return: (string) word
    """
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    consonants_double = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'qu', 'sc',
                         'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
    consonants_triple = ['sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_double = ['aa', 'ae', 'ai', 'ao', 'au', 'ay', 'ea', 'ee', 'ei', 'eo', 'eu', 'ey', 'ia', 'ie',
                     'io', 'iu', 'oa', 'oe', 'oi', 'oo', 'ou', 'oy', 'ua', 'ue', 'ui', 'uo', 'uy']

    consonants_count = len(consonants) - 1
    consonants_double_count = len(consonants_double) - 1
    consonants_triple_count = len(consonants_triple) - 1
    vowels_count = len(vowels) - 1
    vowels_double_count = len(vowels_double) - 1

    length = random.randint(min_length, max_length)
    word = ''
    if length == 1:
        letter_type = 0
    else:
        letter_type = random.randint(0, 1)
    for index in range(100):
        if letter_type:
            if length > 3 and random.randint(0, 35) == 0:
                letter_index = random.randint(0, consonants_triple_count)
                letter = consonants_triple[letter_index]
                length -= 3
            elif length > 2 and random.randint(0, 20) == 0:
                letter_index = random.randint(0, consonants_double_count)
                letter = consonants_double[letter_index]
                length -= 2
            else:
                letter_index = random.randint(0, consonants_count)
                letter = consonants[letter_index]
                length -= 1
            letter_type = 0
        else:
            if length >= 2 and random.randint(0, 10) == 0:
                letter_index = random.randint(0, vowels_double_count)
                letter = vowels_double[letter_index]
                length -= 2
            else:
                letter_index = random.randint(0, vowels_count)
                letter = vowels[letter_index]
                length -= 1
            letter_type = 1
        word += letter

        if length <= 0:
            break

    if capital:
        word = word.title()

    return word


def generate_sentence(words=0):
    """
    Generate a sentence using the generate_words function
    :param words: (int) Word count, 0=Random, 3-20
    :return: (string) Sentence
    """
    punctuation = ['.', '.', '.', '.', '.', '.', '!', '?']
    quoted = False

    if words == 0:
        words = random.randint(3, 20)

    sentence = ''
    for i in range(words):
        if i == 0:
            sentence += generate_word(1, 10, capital=True)
        else:
            # Chance of punctuation
            if i != words and random.randint(0, 100) == 0:
                sentence += '\'s'

            if random.randint(0, 10) == 0:
                sentence += ','
            elif random.randint(0, 100) == 0:
                sentence += ';'
            elif random.randint(0, 200) == 0:
                sentence += ':'

            # Space words or Hyphenate
            if random.randint(0, 200) == 0:
                sentence += '-'
            else:
                sentence += ' '

            # Chance of quote
            if random.randint(0, 100) == 0:
                quoted = True
                sentence += '"'
            sentence += generate_word()

            # Close quotes out within x words
            if quoted and random.randint(0, 8) == 0:
                quoted = False
                sentence += '"'

    # Make sure quotes end
    if quoted:
        sentence += '"'

    return sentence + punctuation[random.randint(0, len(punctuation) - 1)] + ' '


def generate_paragraph(sentences=0):
    """
    Generate a paragraph using the generate_sentence function
    :param sentences: (int) Sentences, 0=Random, 5-20
    :return: (string) Paragraph
    """
    if sentences == 0:
        sentences = random.randint(5, 20)

    paragraph = ''
    for i in range(sentences):
        if i == 0:
            paragraph += generate_sentence()
        else:
            paragraph += generate_sentence()

    return paragraph + '\n\n'


def generate_document(paragraphs=0):
    """
    Generate a document using the generate_paragraph function
    :param paragraphs: (int) Paragraphs, 0=Random, 5-25
    :return:
    """
    if paragraphs == 0:
        paragraphs = random.randint(5, 25)

    document = ''
    for i in range(paragraphs):
        if i == 0:
            document += generate_paragraph()
        else:
            document += generate_paragraph()

    return document


if __name__ == '__main__':
    parser = optparse.OptionParser('%prog [options]\nGenerate random language like content', version='%prog 1.0')

    parser.add_option('-t', '--type',
                      action='store', dest='type', default='documents',
                      choices=['words', 'sentences', 'paragraphs', 'documents'],
                      help='The type of content to be generate. IE words, sentences, paragraphs, or documents')

    parser.add_option('-l', '--length',
                      action='store', dest='length', default=0, type=int,
                      help='How many words, sentences, paragraphs, or documents')

    parser.add_option('-f', '--file',
                      action='store', dest='file', default=None,
                      help='File to save the contents into')

    options, args = parser.parse_args()

    main(options.type, options.length, options.file)
