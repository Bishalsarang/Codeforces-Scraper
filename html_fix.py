import pdfkit
import requests
import re
import bs4


def remove_tags(html, val, element_type):
    """
        Removes unwanted tags like sidebar, leaderboard, menus
    """

    def remove_by_id(soup, id_value, tag="div"):
        """"
            Removes html tag by id
        """
        if soup.find(tag, id=id_value) is not None:
            soup.find(tag, id=id_value).decompose()
        return soup

    def remove_by_class(soup, class_value, tag="div"):
        """
            Removes html tag by class
        """
        for div in soup.find_all(tag, {"class": class_value}):
            div.decompose()
        return soup

    soup = bs4.BeautifulSoup(html, "html.parser")
    if element_type == "id":
        return str(remove_by_id(soup, id_value=val))
    if element_type == "class":
        return str(remove_by_class(soup, class_value=val))


def fix_broken_links(LINK):
    html = requests.get(LINK, stream=True).content

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

    # Decode html bytes to string using UTF-8
    html = html.decode(encoding="utf-8")

    tags_to_remove = [("id", "sidebar"),
                      ("class", "roundbox menu-box"),
                      ("id", "footer"),
                      ("class", "second-level-menu"),
                      ]

    for element_type, element in tags_to_remove:
        html = remove_tags(html, val=element, element_type=element_type)

    return html
