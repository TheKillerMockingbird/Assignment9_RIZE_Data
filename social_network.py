class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            missing = person1_name if person1_name not in self.people else person2_name
            print(f"Friendship not created. {missing} doesn't exist!")
            return
        
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


network = SocialNetwork()

network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")
network.add_person("Alex")

print("People currently in the network:")
print(list(network.people.keys()))
print()

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")
network.add_friendship("Jordan", "Johnny")

print()
print("Final network:")
network.print_network()


# Design Memo - Social Network Graph

# A social network is naturally modeled as a graph. Each person is a vertex, and each friendship is an undirected edge connecting two vertices. Graphs excel at representing relationships that are many-to-many and can contain cycles (friends of friends). Using an adjacency-list representation (a dictionary of people, each holding a list of friends) makes it easy to add new people, add friendships in both directions, and traverse the network.

# A simple list would be a poor fit. With a list of people you would still need a secondary structure to record who is friends with whom, essentially reinventing a graph. Checking whether two people are friends or finding all of someone's friends would require repeated linear searches, which becomes inefficient as the network grows.

# A tree is also unsuitable. Trees are hierarchical and acyclic; social connections are neither. People form mutual friendships and friend-of-friend loops, which trees cannot represent without artificial parent/child constraints that do not exist in real social networks.

# Performance trade-offs appear in the operations we implemented. Adding a person is O(1) average case because of the dictionary. Adding a friendship is also fast (constant time after the existence checks). Printing the entire network, however, is O(V + E): we must visit every person and then walk their friend list. With an adjacency list this is efficient for sparse networks (typical of social graphs), but if the network became extremely dense the friend lists would grow long and printing would slow down. Overall the graph approach gives the best balance of flexibility and reasonable performance for this problem.