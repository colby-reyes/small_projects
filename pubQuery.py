#! python3
# pubQuery.py
# uses google search to search within pubmed instead of pubmed search bar

import webbrowser as w
import random as r

term = input("Search term:   ")

url = 'https://google.com/search?q=site%3Ancbi.nlm.nih.gov '+term
url2 = 'https://scholar.google.com/scholar?q=site:ncbi.nlm.nih.gov+'+term

site = input("\n(1) Google >> PubMed\n(2) Google Scholar >> PubMed\nWhich site would you like to search?     ")

if site == "1":
    w.open(url)
elif site == "2":
    w.open(url2)
else:
    print("Invalid entry...please restart...")
    
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