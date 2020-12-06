#!/usr/bin/env python

"""
 Info about our project comes here.
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"



class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics


    def sing(self):
         for x in self.lyrics:
              print(x)


christmas_song = Song(["It's beginning to look a lot like Christmas", "Everywhere you go",
                       "Take a look at the five and ten, it's glistening once again",
                       "With candy canes and silver lanes that glow", "It's beginning to look a lot like Christmas",
                       "Toys in every store", "But the prettiest sight to see is the holly that will be",
                       "On your own front door", "Sure, it's Christmas once more"])

christmas_song.sing()






