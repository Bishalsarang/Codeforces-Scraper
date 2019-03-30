import pdfkit
import requests
import re
import  bs4


def remove_tags(html, val):
    soup = bs4.BeautifulSoup(html, "html.parser")
    if val == "sidebar":
        if soup.find('div', id="sidebar") is not None:
            soup.find('div', id="sidebar").decompose()
    elif val == "roundbox menu-box":
        for div in soup.find_all("div", {"class": "roundbox menu-box"}):
            div.decompose()
    elif val == "second-level-menu":
        for div in soup.find_all("div", {"class": "second-level-menu"}):
            div.decompose()
    elif val == "footer":
        if soup.find('div', id="footer") is not None:
            soup.find('div', id="footer").decompose()
    return str(soup)

def fix_broken_links(LINK):
    html = requests.get(LINK, stream = True).content

    to_replace = [b'href="//',
                  b'src="//',
                  br'\/scripts\/(\w+)\/en\/codeforces-options.js"',
                  b"href='//",
                  b'src = "//',
                  br'src="/predownloaded/',
                  ]

    replace_with = [b'href="https://',
                    b'src="https://',
                    br"https://codeforces.com/scripts/\1/en/codeforces-options.js",
                    b"href='https://",
                    b'src = "https://',
                    br'src="https://codeforces.com/predownloaded/'
                    ]


    # Fix css and js
    # Take css and js from cf server
    for i in range(len(to_replace)):
        html = re.sub(to_replace[i], replace_with[i], html)


    # with open("arko.html", "wb") as f:
    #    f.write(html)

    # Decode html bytes to string using UTF-8
    html = html.decode(encoding="utf-8")

    tags_to_remove = ["sidebar",
                      "roundbox menu-box",
                      "footer",
                      "second-level-menu",
                      ]

    for element in tags_to_remove:
        html = remove_tags(html, val=element)

    return  html

