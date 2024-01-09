import pandas as pd
import os
from tkinter import *
import json


class Game:
  def __init__(self, console, name, box, rating) -> None:
    self.console = console
    self.name = name
    self.box = box
    self.rating = int(rating)
    pass

  def setConsole(self):
      self.console = input("What console is this for: ")
      return self.console




  def setInfo(self):
    while(True):
      self.console = input("What console is this for: ")
      self.name = input("What is the name of the game: ")
      while(True):
        self.box = input("Is it in a box(Y/N): ")
        self.box = self.box.lower()
        if self.box == 'y' or self.box == 'n':
          break
        else:
          print("Please enter Y or N")
      while(True):
        try:
          self.rating = int(input("Whats your rating (0-5): "))
          if self.rating >= 0 and self.rating < 6:
            break
          else:
            print("Please enter a value between 0 and 5 ")
        except ValueError:
           print("Please enter a value between 0 and 5 ")
      break
    while(True):
          print("(1)Console: " + self.console)
          print("(2)Title: " + self.name)            
          print("(3)In box: " + self.box)
          print("(4)Rating: " + str(self.rating))
          this = input("Is all this info correct(Y/N)? ")
          if this == 'y':
            break
          elif this == 'n':
            while(True):
                    while(True):
                        try:
                          issue = int(input("What is wrong(Enter the number of the item that is wrong): "))
                          break
                        except ValueError:
                            print("Please enter the value of the incorrect item.")
                    if issue == 1:
                      self.console = input("What console is this for: ")
                      break
                    elif issue == 2:
                        self.name = input("What is the name of the game: ")
                        break
                    elif issue == 3:
                        while(True):
                          self.box = input("Is it in a box(Y/N): ")
                          self.box = self.box.lower()
                          if self.box == 'y' or 'n':
                            break
                          else:
                            print("Please enter Y or N")
                        break
                    elif issue == 4:
                            while(True):
                              self.rating = int(input("Whats your rating (0-5): "))
                              if self.rating >= 0 or self.rating < 6:
                                break
                              else:
                                print("Please enter a value between 0 and 5 ")
                            break
                    else:
                      print("Please enter a valid input")
                      continue
          else:
             print("Please enter a valid input")



  
  def showInfo(self):
    print(self.name + " For " + self.console + ", is " + self.box + " box, " + " Rating : " + str(self.rating))

  def addToLibrary(self):
    return{
      'Console' : self.console.capitalize(),
      'Name' : self.name.capitalize(),
      'Box' : self.box.capitalize(),
      'Rating' : self.rating
    }

fullLibrary = []

filename = 'Library.txt'
if os.path.exists(filename):
    print(f"Loaded previous Library file.")
    with open("Library.txt", "r") as fp:
      fullLibrary = json.load(fp)
      df = pd.DataFrame(fullLibrary)
      print(df)
else:
    print(f"No previous Library file found.")



def sortByConsole(list, key):
  n = len(list)
    
  for i in range(n - 1):
      for j in range(0, n - i - 1):
          if list[j][key] > list[j + 1][key]:
              list[j], list[j + 1] = list[j + 1], list[j]


game1 = Game('N/A', 'N/A', 'this', 0)




while(True):
  print("*------------------------------------------------------------------------------------------*")
  print("Would you like to (A)dd a game, (V)iew your games, (R)emove a game,or (S)ave and exit")
  answer = input("")
  answer = answer.lower()
  if answer == "s":
    with open("Library.txt", "w") as fp:
      json.dump(fullLibrary, fp)
    df = pd.DataFrame(fullLibrary)
    df.to_csv('Library.csv')
    print("Done writing dict into .txt and .csv file")
    print("Goodbye")
    break
  elif answer == "a":
    game1.setInfo()
    game1.showInfo()
    fullLibrary.append(game1.addToLibrary())
    sortByConsole(fullLibrary, 'Console')
    continue
  elif answer == "v":
      while(TRUE):
        print("How would you like your games to be sorted?")
        sort = input("By (C)onsole or (N)ame: ")
        sort = sort.lower()
        if sort == 'c':
            sortByConsole(fullLibrary, 'Console')
            break
        elif sort == 'n':
          sortByConsole(fullLibrary, 'Name')
          break
        else:
          print("please enter C or N")
        break
      print("*------------------------------------------------------------------------------------------*")
      df = pd.DataFrame(fullLibrary)
      print(df)
  elif answer == 'r':
    df = pd.DataFrame(fullLibrary)
    print(df)
    while(True):
      try:
        remove = int(input("Enter the number of what game you want removed: "))
        break
      except ValueError:
        print("Please enter the value of the game to be removed.")
    while(True):
      if int(remove) <= int(len(fullLibrary)):
         fullLibrary.pop(remove)
         break
      else:
         print("please enter a valid value for the game you want to remove")
         

  else:
    print("Please Enter a valid input")
    continue

