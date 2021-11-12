
#! python3
import webbrowser, sys, pyperclip, requests



if(len(sys.argv)>1):
    # Get address from command line
    address = ''.join(sys.argv[1:])
else:
    # Get address from the clipboard
    address = pyperclip.paste()
print(address)

downloaded_website = requests.get('https://facebook.com')

downloaded_website.raise_for_status()

print(downloaded_website.status_code)
print(downloaded_website)

# at page 279 in the pdf in collections in chrome

