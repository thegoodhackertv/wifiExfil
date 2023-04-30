# wifiExfil

Exfiltrate all saved Wi-Fi passwords from a Windows PC.

## Requirements

1. On your Windows machine install Python from https://www.python.org/downloads/

2. Install pyinstaller, run `pip install pyinstaller` from cmd

3. Create a webhook from one of the following sites:
- https://requestinspector.com
- https://beeceptor.com
- https://webhook.site

## Instructions (Windows Only)
1. Download repo as ZIP

2. Run builder
```bash
python3 build.py <webhook_url>
```
Executable will be placed inside the `dist` folder

## Disclaimer
Usage of these scripts for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

## Support
[<img width=300 alt="patreon" src="https://i0.wp.com/thegoodhackertv.com/wp-content/uploads/2020/11/patreon.png">](https://www.patreon.com/thegoodhacker)
[<img width=250 alt="buymeacoffe" src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png">](https://www.buymeacoffee.com/thegoodhacker)
