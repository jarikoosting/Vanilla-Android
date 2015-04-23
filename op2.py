#!/usr/bin/python
import nltk
from nltk.corpus import brown
from nltk.tag import UnigramTagger

# Exercise 2A
print(len(brown.tagged_words(categories='mystery'))) #57169
print(len(brown.tagged_sents(categories='mystery'))) #3886

# Exercise 2B
print(brown.tagged_words(categories='mystery')[99]) # I, PPSS
print(brown.tagged_words(categories='mystery')[100]) # Suddenly, RB

# Exercise 2C
