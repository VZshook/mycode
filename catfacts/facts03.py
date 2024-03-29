#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
## print the value assocaited with text"
    for catfact in r.json()["all"]:
        print(catfact.get("text"))  # the .get() method returns NONE if key not found
    
    if r.status_code == 200:
        print('Success!')
    elif r.status_code == 404:
        print('Not Found.')
main()
