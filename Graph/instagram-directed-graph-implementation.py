#Instagram use of graph : A instagram followerlist of users is a directed type of graph.


class Users: #users class to initiate each each user with some details
    def __init__(self,uid,name,email):
        self.uid = uid
        self.name = name
        self.email = email
    
    def getUserDetails(self):
        return f'{self.uid} | {self.name} | {self.email}'

class Instagram: #directed graph structure class 
    def __init__(self):
        self.users = {}
 
    def followUsers(self,user1,user2):  #creating edges between the two users using adjacency list
        if user1 in self.users:
            self.users[user1].append(user2)
        else:
            self.users[user1] = [user2]

        if user2 not in self.users:
            self.users[user2] = []


    def showFollowerList(self): #display all the vertices and edges
        keys = self.users.keys()

        for key in keys:
            print(key.getUserDetails())
            print("Follower List: ")
            followerlist = self.users[key]
            if len(followerlist)==0:
                print("No Followers")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            else:
                for follower in followerlist:
                    print(follower.getUserDetails())
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            


if __name__ == '__main__':
    graph = Instagram()
    user1 = Users(1,"john","john@example.com")
    user2 = Users(2,"jennie","jennie@example.com")
    user3 = Users(3,"fionna","fionna@example.com")
    user4 = Users(4,"dave","dave@example.com")
    user5 = Users(5,"kia","kia@example.com")
    user6 = Users(6,"leo","leo@example.com")

    graph.followUsers(user1,user2)
    graph.followUsers(user1,user3)
    graph.followUsers(user2,user4)
    graph.followUsers(user3,user4)
    graph.followUsers(user3,user5)
    graph.followUsers(user4,user5)
    graph.followUsers(user5,user6)

    graph.showFollowerList()
