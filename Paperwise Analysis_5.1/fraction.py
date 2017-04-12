#!/home/mayank/anaconda/bin/python
import os
import sys
import sklearn
import matplotlib
import pickle

matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity

"""
Input:  Is a file that contains
        '<cited> <citer> <citation context>' information.
        Update that filename in the variable dataFile

Output: Produces tuples
        '<citer1> <citer2> <cited> <cosineSimilarity>'
         stored in outputDataFrame
"""

def get_years():
    year_of = {}
    with open("../Files/years_final.txt", "r") as years_file:
        for line in years_file.readlines():
            line = line.split(":")            
            year_of[int(line[0])] = int(line[1])
    return year_of


def get_titles():
    title_of = {}
    with open("../Files/paper_title", "r") as titles_file:
        for line in titles_file.readlines():
            line = line.split()
            context = ' '.join(line[1:])            
            title_of[int(line[0])] = context
    return title_of

def paper_fields():
    field_of = {}
    with open("../Files/paper_fields", "r") as fields_file:
        for line in fields_file.readlines():
            line = line.split()            
            field_of[int(line[0])] = str(line[1])
    return field_of




top500PapersCitationData = pd.read_pickle('top500PapersData.p')


fraction = [0]*6
year = [0]*6

for i in xrange(1,6):
    fname = 'year%dtop10.p' %(i)
    year[i] = pd.read_pickle(fname)


yearWiseTotal = [0]*6
for i in xrange(1,6):
    yearWiseTotal[i] = len(top500PapersCitationData[top500PapersCitationData['Year Difference'] == i])


for i in xrange(1,6):
    uniqueCiters = year[i]['Citer1'].unique()
    uniqueCiters = uniqueCiters.tolist()
    copiedFraction = 0
    for citer in uniqueCiters:
        totalCount = len(top500PapersCitationData[(top500PapersCitationData['Citer'] == citer)])
        copiedCount = len(year[i][(year[i]['Citer1'] == citer)])
        copiedFraction += copiedCount/totalCount 
    fraction[i] = float(copiedFraction)/len(uniqueCiters)

print fraction
