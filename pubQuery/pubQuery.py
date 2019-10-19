#! python3
# pubQuery.py
# uses google (or search engine of choice) to search within pubmed instead of pubmed search bar

import webbrowser as w
#import random as r
from pqVars import *
from pqFuncs import *


print("_"*60)
print("Search engine is currently set to: {}\nTo change search engine, enter 'X' or just hit 'Enter'".format(searchEngine))
print("_"*60)

term = input("Search term:    ")

if searchEngine == "":
    seSelect = change_search_engine()
    update_var("pqVars.py","searchEngine", seSelect)
elif term == "" or term.upper() == "X":
    seSelect = change_search_engine()
    update_var("pqVars.py","searchEngine", seSelect)
else:
    w.open(urls[searchEngine]+term)


    
    
"""   
## TODO:
    # add GUI input field using tkinter
# importing tkinter 
from tkinter import * 
from tkinter import ttk 
from tkinter.messagebox import askyesno 
  
# creating root 
root = Tk() 
  
# specifying geometry 
root.geometry('200x100') 
  
# This is used to take input from user 
# and show it in Entry Widget. 
# Whatever data that we get from keyboard 
# will be treated as string. 
input_text = StringVar() 
  
entry1 = ttk.Entry(root, textvariable = input_text, justify = CENTER) 
  
# focus_force is used to take focus 
# as soon as application starts 
entry1.focus_force() 
entry1.pack(side = TOP, ipadx = 30, ipady = 6) 
  
save = ttk.Button(root, text = 'Save', command = lambda : askyesno( 
                                'Confirm', 'Do you want to save?')) 
save.pack(side = TOP, pady = 10) 
  
root.mainloop()

"""
"________________________________________"

"""

## TODO:
    # open text/csv file
    with open("file_name") as fhand:
        # do something?

## TODO:
    # gather url's of top x# of citations
    # search for all permutations of 
    stPerm  = r.combo(term)     # ** find or write function
    stPerm = combo(term)
    print("Gathering citations for keyword combination: '{}'".format(stPerm))
    
    
## TODO:
    # filter out duplicate url's
    print("Checking for duplicates...")

## TODO:
    # write to file
    print("Saving results to file '{}'...".format(fhand)
    
## TODO >> finish fn
def combo(search_term):
    words = search_term.split()
    # mix order of words
    
    newST = newOrder.join(" ")
    return newST
    
    
    
## NEXT STEP: gather pdf's when possible
    try:
    except: 
    
## NEXT STEP: 
    # Gather text of abstract along with formatted title and author citation 
    # create visual way to present abstracts with citations (1 page per citation/abstract? list of citations/abstracts?)
"""