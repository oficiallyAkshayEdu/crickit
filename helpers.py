from imports import *

#### Checks the probability of an event happening
def probability(event):
    if event <= random.random():
        return True
    else:
        return False