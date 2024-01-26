import requests
import json
def get_requests(API):
    x = requests.get(API).text
    return x

def main():
    while True:
        message = input(">>")

        API = f"YOURAPI={message}"
        
        z = get_requests(API)
        nigga = json.loads(z)
        print(nigga['cnt'])
        # print(type(nigga))
        
if __name__ == "__main__":
    main()
