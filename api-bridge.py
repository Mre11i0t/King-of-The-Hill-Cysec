#!/usr/bin/env python3
import requests
import os
import sys
def main():
    token = "<your-ctfd-admin-token>"
    # Get users with content type json header
    r = requests.get(f"https://koth.isfcrclub.tech/api/v1/users", headers={"Authorization": f"Token {token}", "Content-Type": "application/json"})
    users = r.json()["data"]
    print(users)
    # map  username to user id in a dictionary
    user_ids = {user["name"]: user["id"] for user in users}
    # Get IP from env variable KOTHSERVER
    ip = os.environ["KOTHSERVER"]
    r = requests.get(f"http://{ip}:9999")
    username = r.text
    print(username)
    # Strip the username of whitespace and \n
    username = username.strip()
    # check if empty
    if username:
        # check if username is in the dictionary
        if username in user_ids:
            # award the user
            award(user_ids[username])
            print(f"Awarded {username}")
        else:
            print(f"{username} is not a valid user")
    else:
        print("No King yet")

def award(user_id):
     token = "<your-ctfd-admin-token>"
    # Create API Session
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})
    r = s.post(
        f"https://koth.isfcrclub.tech/api/v1/awards",
        json={"name":"King","value":"10","icon":"crown","user_id":user_id},
    )
    # Log the response in /tmp/award.log
    with open("./award.log", "a") as f:
        f.write(f"{r.json()}\n")

if __name__ == "__main__":
    main()
