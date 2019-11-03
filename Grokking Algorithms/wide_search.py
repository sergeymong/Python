from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def wide_search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, 'is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def main():
    graph = {
        "you": ["alice", "bob", "claire", "khim"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }
    wide_search(graph, 'you')


if __name__ == '__main__':
    main()
