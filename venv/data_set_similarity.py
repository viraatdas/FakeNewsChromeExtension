# -*- coding: utf-8 -*-

import re, math
from collections import Counter

WORD = re.compile(r'\w+')
cosineValues = []
similarSentenceIndices=[]
body1 = 'California Gov. Jerry Brown on Friday said his state will launch its own satellite in a bid to combat climate change, following up on a promise he made after the election of President Trump. “We’re going to launch our own satellite — our own damn satellite to figure out where the pollution is and how we’re going to end it,” Brown told the audience at the Global Climate Action Summit in San Francisco. "We’re going to launch our own satellite — our own damn satellite to figure out where the pollution is and how we’re going to end it." - California Gov. Jerry Brown. The Golden State will work with San Francisco-based Planet Labs to launch a satellite that would track climate-change-causing pollutants. The company has already launched 150 satellites, Brown said. “In California, with science under attack, in fact we’re under attack by a lot of people, including Donald Trump, but the climate threat still keeps growing,” Brown added. “So, we want to know, what the hell is going on all over the world, all the time?” PELOSI RENEWS OBAMAS WAR ON COAL, BACKS GROUP LOOKING TO SHUT DOWN COAL PLANTS The outgoing governor, who will leave at the end of the year and will be replaced by Democrat Lt. Gov. Gavin Newsom or Republican businessman John Cox, didn’t divulge any how much it will cost the state to undergo a space-related project that is generally done by the federal government. Marc Lotter, former special assistant to President Trump, discusses how The Washington Post said that President Trump is "complicit" for Hurricane Florence because of his views on climate change. Brown’s office told the Washington Post that government scientists and staff will work on the project, but no money from the state’s coffers will be spent toward the development of the satellite. A number of donors have stepped up to fund the experiment, including San Francisco investment banker Richard Lawrence and the Jeremy and Hannelore Grantham Environmental Trust. HARRISON FORD URGES VOTERS TO STOP GIVING POWER TO PEOPLE WHO DONT BELIEVE IN SCIENCE The intentionally worded announcement came nearly two years after the governor threatened the Trump administration that California will launch its own satellite. If Trump turns off the satellites, California will launch its own damn satellite, Brown said back in 2016, before lamenting the Governor Moonbeam” nickname the media gave him for previously considering similar plans. I remember back in 1978 I proposed a Landsat satellite for California. They called me Governor Moonbeam because of that, Brown said. Over the last two years, Brown clashed with the Trump administration on multiple fronts, including immigration and environmental rules. Trump’s decision to pull out the Paris climate agreement in June 2017 particularly infuriated the California governor.'
body2 = 'Gov. Moonbeam is finally sending California into space. Jerry Brown closed his climate summit in San Francisco on Friday with a dramatic announcement: California will launch its own satellite into orbit to track and monitor the formation of pollutants that cause climate change. With science still under attack and the climate threat growing, we’re launching our own damn satellite, Brown said in prepared remarks. This groundbreaking initiative will help governments, businesses and landowners pinpoint — and stop — destructive emissions with unprecedented precision, on a scale that’s never been done before. After decades of being unable to shake the moniker Gov. Moonbeam — which columnist Mike Royko branded Brown in 1976 — the governor has come to embrace it in a big way. Brown suggested around that time that California should launch its own satellite for emergency communications. At the time, the governor was in his 30s and full of ideas for the state that critics dismissed as flaky. Some were put into law and established California as a pioneer on various policy fronts, others were put on the shelf. The governors Global Climate Action Summit — and the Trump administrations reluctance to pursue robust climate research – opened the door wide open for the governor to pull the satellite vision out of the archives. The state will develop the satellite with the San Francisco-based Earth-imaging firm Planet Labs, a company founded by former NASA scientists in 2010. The state may ultimately launch multiple satellites into space, according to the governor’s office. The California Air Resources Board is in the process of developing the monitoring technology used by the satellite. No date has been set for the launch; the process is expected to take several years. Officials at the air board discussed the possibility of the satellite at their meeting in July, when they expressed concern that the Trump administration had mothballed its plans to use the innovative technology to monitor pollutants from above. The state officials said at the time that they hoped to launch within a few years. Robbie Schingler, co-founder of Planet Labs, said the project will inform how advanced satellite technology can enhance our ability to measure, monitor, and ultimately, mitigate the impacts of climate change. The state hopes to put the satellite to use in pinpointing the sources of climate pollutants, which could enable it to refine its regulatory approach and better understand how to mitigate warming. Data from the satellite would be made available to the public through a partnership with the Environmental Defense Fund. Browns announcement came in quickly delivered remarks at the close of the three-day gathering and received a standing ovation from many in the audience. Two activists who stood up on their seats saying Brown is "not a climate leader" were carried out of the auditorium by security.'

def getSimilar(cosineValues):
     indexQuantity = 5;
     a = []
     similarIndices = []

     for i in cosineValues:
          for j in i:
               a.append(j)

     for i in range(0,indexQuantity):
          if (max(a)>0.5):
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
