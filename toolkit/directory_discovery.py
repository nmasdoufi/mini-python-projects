import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("DIRECTORY DISCOVERY")
print(ascii_banner)

print("-"*50)
target_url = input("[*] Enter Target's IP : ")
word_list = input("[*] Enter The Wordlist's Path : ")

def request(url) :
    try:
        return requests.get("http://"+ url)
    except requests.exceptions.ConnectionError:
        pass

print("-"*50)
file = open(word_list, 'r')
for line in file:
    directory = line.strip()
    full_url = target_url + '/' + directory
    response = request(full_url)

    if response:
        print("[*] Discovered Directory at : " + full_url)
print("-"*50)  
file.close()      