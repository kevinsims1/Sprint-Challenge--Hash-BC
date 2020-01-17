#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


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
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        if ticket.source == "NONE":
            route[0] = ticket.destination

    index = 0
    current = 0

    while True:
        current = route[index]
        next_ = hash_table_retrieve(hashtable, current)
        index += 1
        route[index] = next_
        if next_ == "NONE":
            break

    return route
