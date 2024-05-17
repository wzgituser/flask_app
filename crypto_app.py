import os
import requests
from dotenv import load_dotenv
import pprint

load_dotenv()


def main():
    a = requests.get('https://api.coincap.io/v2/assets/').json()
    print(a)


if __name__ == "__main__":
    main()
