from collections import deque
class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
    def person_is_seller(self, target_name):
        return self.name == target_name and self.profession == "mango seller"
people = [
        Person("alice", "programmer"),
        Person("bob", "shop seller"),
        Person("claire", "driver"),
        Person("anuj", ""),
        Person("peggy", "banker"),
        Person("thom", "driver"),
        Person("jonny", " seller")
    ]
graph = {
    'You': [people[0].name, people[1].name, people[2].name],
    people[1].name : [people[3].name, people[4].name],
    people[0].name : [people[4].name],
    people[2].name : [people[5].name, people[6].name],
    people[3].name : [],
    people[4].name : [],
    people[5].name : [],
    people[6].name : [],
}

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            person_obj = None
            for p in people:
                if p.name == person:
                    person_obj = p
                    break
            if person_obj and person_obj.person_is_seller(person):
                print(person + ' is mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False



if not search('You'):
    print('Nobody is mango seller')