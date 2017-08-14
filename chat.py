import fbchat
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    users = client.fetchAllUsers()
    friend = [user for user in users if user.name == name][0]
    msg = str(input("Message: "))
    sent = client.sendMessage(msg, thread_id=friend.uid, thread_type = 1)
    if sent:
        print("Message sent successfully!")

