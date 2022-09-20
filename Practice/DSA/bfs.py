# breadth first search
# Breadth-first search tells you if there’s a path from A to B.
# • If there’s a path, breadth-irst search will ind the shortest path.
# • If you have a problem like “ind the shortest X,” try modeling your
# problem as a graph, and use breadth-irst search to solve.
# • A directed graph has arrows, and the relationship follows the
# direction of the arrow (rama -> adit means “rama owes adit money”).
# • Undirected graphs don’t have arrows, and the relationship goes both
# ways (ross - rachel means “ross dated rachel and rachel dated ross”).
# • Queues are FIFO (First In, First Out).
# • Stacks are LIFO (Last In, First Out).
# • You need to check people in the order they were added to the search
# list, so the search list needs to be a queue. Otherwise, you won’t get
# the shortest path.
# • Once you check someone, make sure you don’t check them again.
# Otherwise, you might end up in an ininite loop.

from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_mango_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


def is_mango_seller(name):
    if name[-1] == 'm':
        return True
    return False


print(breadth_first_search('you'))
