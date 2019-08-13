import argparse
import os
import re

import bs4
import requests

import art
import html_fix
import save_as_pdf


def contest_download_mode(BASE_URL, DIR, start_id, end_id):
    # Regex Pattern for contest name
    header_pattern = re.compile(r'<div style="text-align: center; font-size: 1\.8rem; margin-bottom: 0\.5em;"\s*class="caption">(.+)</div>')
    invalid_character = re.compile(r'&|;|-|/|$|<|>|\*|\?|\||"|:|\\')

    for contest_num in range(start_id, end_id + 1):
        get_url = BASE_URL + str(contest_num) + "/problems"

        html = requests.get(get_url, stream=True)
        print("\n")
        print(f"Fetching {get_url}")

        contest_title = "".join(re.findall(header_pattern, html.text))

        # Remove invalid characters
        contest_title = re.sub(invalid_character, "", contest_title)
        print(f"Converting contest {contest_title}")

        file_name = DIR + contest_title + ".pdf"
        print(file_name)
        # If contest id is invalid
        if file_name == DIR + ".pdf":
            print(f"Contest with contest id {contest_num} doesn't exist")
            continue

        if os.path.exists(file_name):
            print(f"Contest {contest_title} already exists")
            continue

        html = html_fix.fix_broken_links(get_url)
        save_as_pdf.write_pdf(DIR, file_name, contest_title, html)


def problem_download_mode(crawl_url, maximum_problems, BASE_URL, DIR):
    print(crawl_url, maximum_problems)
    DOMAIN = "https://codeforces.com"

    invalid_character = re.compile(r'&|;|-|/|$|<|>|\*|\?|\||"|:|\\')
    # Get all links inside div
    html = requests.get(crawl_url, stream=True).content.decode(encoding="utf-8")
    soup = bs4.BeautifulSoup(html, "html.parser")
    data = soup.find_all("table", {"class": "problems"})
    downloaded = 0
    link_pattern = r"/problemset/problem/\d+/\w"

    for div in data:
        links = div.findAll('a', {"href": re.compile(link_pattern)})
        removed_duplicated_link = [DOMAIN + a["href"] for i, a in enumerate(links) if i % 2 == 0]

        for a in removed_duplicated_link:
            if downloaded == maximum_problems:
                print("Download Complete. Downloaded {} problems ".format(downloaded))
                return
            downloaded += 1
            print("\n")
            print("Fetching {}".format(a))
            print(DIR)
            problem_soup = bs4.BeautifulSoup(requests.get(a, stream=True).content.decode(encoding="utf-8"), "html.parser")
            problem_title = problem_soup.find_all("div", {"class": "title"})[0].text

            # Remove invalid characters
            problem_title = re.sub(invalid_character, "", problem_title)

            print("Converting problem {}".format(problem_title[2:]))

            problem_title = str(downloaded) + ". " + problem_title[2:]
            filename = DIR + problem_title + ".pdf"
            if os.path.exists(filename):
                print(f"Problem {problem_title} already exists")
                continue

            problem_html = html_fix.fix_broken_links(a)
            save_as_pdf.write_pdf(DIR, filename, problem_title, problem_html)


def main():
    arg = argparse.ArgumentParser()
    # Options to specify mode i.e contest download mode or problem download mode
    arg.add_argument("-m", "--mode", required=True, help="Specify the mode contests or problems")

    # Options for contest download mode
    arg.add_argument("-l", "--lower", required=False, help="specify lower contest ID")
    arg.add_argument("-u", "--upper", required=False, help="specify upper contest ID")

    # Options for problem download mode
    arg.add_argument("-t", "--tag", required=False, help="Specify problem tags")
    arg.add_argument("-o", "--orderby", required=False, help="Specify order by rating or solved")
    arg.add_argument("-n", "--number", required=False, help="Specify how many problems")
    arg.add_argument("-asc", required=False, help="specify how to order by ascending or descending")

    args = vars(arg.parse_args())

    mode = args["mode"]

    BASE_URL = "https://codeforces.com/contest/"
    DIR = "Downloaded PDFs/"

    start, end = 1, 1

    # Contest Download
    if mode[0].upper() == "C":
        BASE_URL = "https://codeforces.com/contest/"
        DIR = "Downloaded PDFs/Contests/"
        if not os.path.exists(DIR):
            os.makedirs(DIR)
        if args["lower"] is not None:
            start, end = int(args["lower"]), int(args["upper"])
        contest_download_mode(BASE_URL, DIR, start, end)

    # Problem Download
    elif mode[0].upper() == "P":
        BASE_URL = "https://codeforces.com/problemset?"
        DIR = "Downloaded PDFs/Tags/"
        if not os.path.exists(DIR):
            os.makedirs(DIR)

        maximum_problems = 10

        add_tag, add_orderby, add_asc, add_and = [""] * 4
        if args["number"] is not None:
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
        problem_download_mode(crawl_url, maximum_problems, BASE_URL, DIR)


if __name__ == "__main__":
    main()
