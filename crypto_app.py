import os
import requests
from dotenv import load_dotenv
import pprint

load_dotenv()

id_data = []


def get_list():
    a = requests.get('https://api.coincap.io/v2/assets/').json()
    # print(a)

    for i in a:
        for i in a["data"]:
            id_data.append(i["id"])
            # print(i["id"])
    # print(id_data)
    return id_data


def get_chosen_one(xx):
    c = requests.get(f'https://api.coincap.io/v2/rates/{xx}').json()
    for i in c:
        d = c["data"]
    return d


if __name__ == "__main__":
    b = input("Get cyrypto rate, type Y/N:")
    if b == "Y":
        get_list()
    elif b == "N":
        print("see you soon")
    else:
        print("choice the right character - Y/N")
    print(
        f'Names of the main crypto curencies: \n {id_data} \n -------type the crypto name to get data--------')
    test = input(f'type the crypto name :')
    for i in id_data:
        if i == test:
            print(i == test)
            # print(get_chosen_one(test))
