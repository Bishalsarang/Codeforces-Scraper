import pdfkit
import os
import platform
import requests
import re

"""
TODO 
1. Handle Cases if contest doesn't exist
2. Downloading editorials
"""



print("  _____          _       __                            _____            _            _   ")
print(" / ____|        | |     / _|                          / ____|          | |          | |  ")
print("| |     ___   __| | ___| |_ ___  _ __ ___ ___        | |     ___  _ __ | |_ ___  ___| |_ ")
print("| |    / _ \ / _` |/ _ \  _/ _ \| '__/ __/ _ \       | |    / _ \| '_ \| __/ _ \/ __| __|")
print("| |___| (_) | (_| |  __/ || (_) | | | (_|  __/       | |___| (_) | | | | ||  __/\__ \ |_ ")
print(" \_____\___/ \__,_|\___|_| \___/|_|  \___\___|        \_____\___/|_| |_|\__\___||___/\__|")

print("                            _____                                      ")
print("                           / ____|                                     ")
print("                          | (___   ___ _ __ __ _ _ __  _ __   ___ _ __ ")
print("                           \___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|")
print("                           ____) | (__| | | (_| | |_) | |_) |  __/ |   ")
print("                          |_____/ \___|_|  \__,_| .__/| .__/ \___|_|   ")
print("                                                | |   | |              ")
print("                                                |_|   |_|                   ")
print("                                                            Author: Bishal Sarangkoti(sarangbishal.github.io)")

print("\nThe starting and ending contest number separated by space")

def isLinux():
    return platform.system() == "Linux"

start, end = 1, 1
try:
    start, end = map(int, input().split())
except Exception as e:
    print("Please supply two lower and upper id for contests")
    exit()
if start > end:
    start, end = end, start

if not os.path.exists("Downloaded PDFs"):
    os.makedirs("Downloaded PDFs")

BASE_URL = "https://codeforces.com/contest/"
DIR = "Downloaded PDFs/"

#Regex Pattern for contest name
header_pattern =  re.compile(r'<div style="text-align: center; font-size: 1\.8rem; margin-bottom: 0\.5em;"\s*class="caption">(.+)</div>')

invalid_character = re.compile(r'&|;|-|/|$|<|>|\*|\?|\||"|:|\\')
for contest_num in range(start, end + 1):
    get_url = BASE_URL + str(contest_num) + "/problems"

   

    html = requests.get(BASE_URL + str(contest_num) + "/problems")
    print("\n\n")
    print(get_url)
    not_found_pattern = r'< div class ="message" > No such contest < / div >'
    if re.match(not_found_pattern, html.text):
        continue
    contest_title = "".join(re.findall(header_pattern, html.text))

    #Remove invalid characters
    contest_title = re.sub(invalid_character,"", contest_title)
    print("Converting contest {}".format(contest_title))
    file_name = DIR + contest_title + ".pdf"

    if os.path.exists(file_name):
        print("Contest {} already exists".format(contest_title))
        continue
    if isLinux():
        pdfkit.from_url(get_url, file_name)
    else:
        #Path to wkhtmltopdf
        path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)
        pdfkit.from_url(get_url, file_name, configuration = config)
