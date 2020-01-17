#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        #insert tickets into the HT     #Key            #Value
        hash_table_insert(hashtable, ticket.source, ticket.destination) 
        # ticket didn't come from anywhere so its the start of our route
        if ticket.source == "NONE": 
            route[0] = ticket.destination


    index = 0
    current = 0

    #runs until it hits a destination of None
    while True:
        current = route[index]
        #Retrieve destination and place next to its source
        next_ = hash_table_retrieve(hashtable, current)
        index += 1
        route[index] = next_
        if next_ == "NONE": #we have reached the end
            break

    #returns our list of routes
    return route
