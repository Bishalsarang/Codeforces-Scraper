import pdfkit
import os
import requests
import re

"""
TODO 
1. Handle Cases if contest doesn't exist
2. Downloading editorials
"""

print("The starting and ending contest number separated by space")
start, end = map(int, input().split())

if not os.path.exists("Downloaded PDFs"):
    os.makedirs("Downloaded PDFs")

BASE_URL = "https://codeforces.com/contest/"
DIR = "Downloaded PDFs/"

#Regex Pattern for contest name
header_pattern =  re.compile(r'<div style="text-align: center; font-size: 1\.8rem; margin-bottom: 0\.5em;"\s*class="caption">(.+)</div>')

for contest_num in range(start, end + 1):
    get_url = BASE_URL + str(contest_num) + "/problems"

    #Path to wkhtmltopdf
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)

    html = requests.get(BASE_URL + str(contest_num) + "/problems")
    print(get_url)
    not_found_pattern = r'< div class ="message" > No such contest < / div >'
    if re.match(not_found_pattern, html.text):
        continue
    contest_title = "".join(re.findall(header_pattern, html.text))
    print("Converting contest{}".format(contest_title))
    file_name = DIR + contest_title + ".pdf"
    if os.path.exists(file_name):
        print("Contest {} already exists".format(contest_title))
        continue
    pdfkit.from_url(get_url, file_name, configuration = config)