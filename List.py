#!/usr/bin/env python

"""
 Maak een functie die data in een lijst stopt.
 Er worden steeds 20 items in de lijst gestoken, het gemiddelde print je af.
 Zorg dat je de loop kan onderbreken met een door jou gekozen symbool.
 """

# import
import random

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"

def List():

 while True:
    randomlist = random.sample(range(0, 50), 20)                                 #To make a list with this conditions
    print(randomlist)

    listValues = randomlist
    listSum = sum(listValues)

    listLength = len(listValues)
    listAverage = listSum / listLength                                           #To calculate the average

    print(listAverage)
    print("Press enter for a new list or 'm' to quit.")                          #To give the user a choice what to do

    if input() == 'm':                                                           #Press m to break the loop
      break

if __name__ == '__main__':  # code to execute if called from command-line
    List()
