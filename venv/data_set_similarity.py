# -*- coding: utf-8 -*-

import re, math
from collections import Counter

WORD = re.compile(r'\w+')
cosineValues = []
similarSentenceIndices=[]

body1 = ''
body2 = ''

def getSimilar(cosineValues):
     indexQuantity = 5;
     a = []
     similarIndices = []

     for i in cosineValues:
          for j in i:
               a.append(j)

     for i in range(0,indexQuantity):
          similarIndices.append(index_2d(cosineValues, max(a)))
          a.remove(max(a))

     return similarIndices

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def calculateCosineValues(text1,text2):
     tempList = []
     #temp1,temp2
     for i, a in enumerate(sentences1):
          temp1 = text_to_vector(a)
          for j, b in enumerate(sentences2):
               temp2 = text_to_vector(b)
               tempList.append(get_cosine(temp1, temp2))
          cosineValues.append(tempList)
          tempList = []

def toSentence(text):
     i = 0
     check = True
     sentences = []
     output_sentences = []
     while text.find('.') != -1:
          sentences.append(text[0: text.find('.')])
          text = text[text.find('.') + 1: len(text)]
          i += 1

     i = 0
     while check == True:
          if (i + 1) < len(sentences) - 1:
               output_sentences.append(sentences[i] + sentences[i + 1])
          elif (i + 1) == len(sentences) - 1:
               output_sentences.append(sentences[i] + sentences[i + 1])
               check = False
          else:
               output_sentences.append(sentences[i])
               check = False
          i += 2
     return output_sentences


sentences1 = toSentence(body1)
sentences2 = toSentence(body2)

print sentences1
print sentences2

calculateCosineValues(sentences1, sentences2)

print 'Cosine:', cosineValues

similarSentenceIndices = getSimilar(cosineValues)
print similarSentenceIndices