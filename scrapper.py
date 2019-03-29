import argparse
import os
import requests
import re
import save_as_pdf
import  art



def contest_download_mode():
    # Regex Pattern for contest name
    header_pattern = re.compile(
        r'<div style="text-align: center; font-size: 1\.8rem; margin-bottom: 0\.5em;"\s*class="caption">(.+)</div>')
    invalid_character = re.compile(r'&|;|-|/|$|<|>|\*|\?|\||"|:|\\')

    for contest_num in range(start, end + 1):
        get_url = BASE_URL + str(contest_num) + "/problems"

        html = requests.get(get_url)
        print("\n")
        print("Fetching {}".format(get_url))

        contest_title = "".join(re.findall(header_pattern, html.text))

        # Remove invalid characters
        contest_title = re.sub(invalid_character, "", contest_title)
        print("Converting contest {}".format(contest_title))

        file_name = DIR + contest_title + ".pdf"

        # If contest id is invalid
        if file_name == DIR + ".pdf":
            print("Contest with contest id {} doesn't exist".format(contest_num))
            continue

        if os.path.exists(file_name):
            print("Contest {} already exists".format(contest_title))
            continue

        save_as_pdf.write(DIR, file_name, contest_title, get_url)


def problem_download_mode(crawl_url, maximum_problems):
    print(crawl_url, maximum_problems)
    #save_as_pdf.write(DIR, file_name, contest_title, crawl_url)

arg = argparse.ArgumentParser()

# Options to specify mode i.e contest download mode or problem download mode
arg.add_argument("-m", "--mode", required=True, help="Specify the mode contests or problems")


# Options for contest download mode
arg.add_argument("-l", "--lower", required=False, help = "specify lower contest ID")
arg.add_argument("-u", "--upper", required=False, help="specify upper contest ID")

# Options for problem download mode
arg.add_argument("-t", "--tag", required=False, help = "Specify problem tags")
arg.add_argument("-o", "--orderby", required=False, help = "Specify order by rating or solved")
arg.add_argument("-n", "--number", required=False, help = "Specify how many problems")
arg.add_argument("-asc", required=False, help = "specify how to order by ascending or descending")



"""

Options:
order=BY_SOLVED_DESC -> Done
order=BY_SOLVED_ASC -> Done
order=BY_RATING_DESC -> Done
order=BY_RATING_ASC -> Done
order=BY_SOLVED_DESC&tags=greedy-> Done
order=BY_RATING_ASC&tags=greedy -> Done
order=BY_RATING_ASC&tags=greedy -> Done
tags=1100-1100 -> Done -> Done
tags=geometry -> Done
"""


args = vars(arg.parse_args())

mode = args["mode"]

BASE_URL = "https://codeforces.com/contest/"
DIR = "Downloaded PDFs/"
start, end = 1, 1
if mode[0].upper() == "C":
    BASE_URL = "https://codeforces.com/contest/"
    DIR = "Downloaded PDFs/"
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    if args["lower"] is not None:
        start, end = int(args["lower"]), int(args["upper"])
    contest_download_mode()

elif mode[0].upper() == "P":
    BASE_URL = "https://codeforces.com/problemset?"
    DIR = "Downloaded PDFs/Tags/"
    if not os.path.exists(DIR):
        os.makedirs(DIR)

    maximum_problems = 10

    add_tag, add_orderby, add_asc, add_and = [""] * 4
    if args["number"] is not  None:
        maximum_problems = int(args["number"])
    if args["tag"] is not None:
        add_tag = "tags=" + args["tag"]
    if args["orderby"] is not None:
        add_orderby = "order=BY_" + args["orderby"].upper()
    if args["asc"] is not None:
        if args["asc"][0].upper() == "F":
            add_asc = "_DESC"
        elif args["asc"][0].upper() == "T":
            add_asc = "_ASC"
    if add_orderby + add_asc != "":
        add_and = "&"
    crawl_url = BASE_URL + add_orderby + add_asc + add_and + add_tag
    crawl_url = re.sub("\s", "+", crawl_url)
    problem_download_mode(crawl_url, maximum_problems)

