
import requests

#Domain you will scan
domain = "URL_YOU_{CHANGE}_WANNA_SCAN"

#read from a file
file = open("directory-list-2.3-medium.txt")

#read all the file
content = file.read()

#split by new lines
subdomains = content.splitlines()

for subdomain in subdomains:

        #URL construction
        url = f"http://{domain}.{subdomain}"
        try:

                #If error then the subdomain does not exist
                requests.get(url)

        except requests.ConnectionError:

                #if no subdomain, pass
                #print nothing
                pass

        else:
                #if found print it
                print("[+] Subdomain Found: ", url)
