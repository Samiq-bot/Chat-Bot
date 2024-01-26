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
        response = json.loads(z)
        print(response['cnt'])
        
if __name__ == "__main__":
    main()
