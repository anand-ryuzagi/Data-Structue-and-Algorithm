#Facebook use of graph : In facebook friendlist of users is a undirected type of graph.


class Users: #users class to initiate each each user with some details
    def __init__(self,uid,name,email):
        self.uid = uid
        self.name = name
        self.email = email
    
    def getUserDetails(self):
        return f'{self.uid} | {self.name} | {self.email}'

class Facebook: #undirected graph structure class 
    def __init__(self):
        self.users = {}
 
    def connectUsers(self,user1,user2):  #creating edges between the two users using adjacency list
        if user1 not in self.users:
            self.users[user1] = []
        if user2 not in self.users:
            self.users[user2] = []

        
        self.users[user1].append(user2)
        
        self.users[user2].append(user1)

    def showFriendList(self): #display all the vertices and edges
        keys = self.users.keys()

        for key in keys:
            print(key.getUserDetails())
            print("Friend List: ")
            friendlist = self.users[key]
            for friend in friendlist:
                print(friend.getUserDetails())
            
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")


if __name__ == '__main__':
    graph = Facebook()
    user1 = Users(1,"john","john@example.com")
    user2 = Users(2,"jennie","jennie@example.com")
    user3 = Users(3,"fionna","fionna@example.com")
    user4 = Users(4,"dave","dave@example.com")
    user5 = Users(5,"kia","kia@example.com")
    user6 = Users(6,"leo","leo@example.com")

    graph.connectUsers(user1,user2)
    graph.connectUsers(user1,user3)
    graph.connectUsers(user2,user4)
    graph.connectUsers(user3,user4)
    graph.connectUsers(user3,user5)
    graph.connectUsers(user4,user5)
    graph.connectUsers(user5,user6)

    graph.showFriendList()
