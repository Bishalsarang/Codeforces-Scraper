import pdfkit
import platform

# Path to wkhtmltopdf for Windows Machine
path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)

def is_linux():
    """
    Identify the current platform
    :return: True if Linux else False
    """
    return platform.system() == "Linux"

def remove_unwanted(name):
    """
    Function to remove characters from contest like VK Cup 2015  Раунд 3
    https://codeforces.com/contest/541/problems
    """
    # Valid Name in Contest
    pattern = re.compile('[a-z0-9\s\-()[\]\.,\+#]+', re.IGNORECASE)
    for i, elem in enumerate(name):
        if not re.match(pattern, elem):
            return name[: i]
    return name

def write(DIR, file_name, contest_title, get_url):
    if is_linux():
        try:
            pdfkit.from_url(get_url, file_name)
        except:
            file_name = DIR + remove_unwanted(contest_title) + ".pdf"
            pdfkit.from_url(get_url, file_name)
    else:
        try:
            pdfkit.from_url(get_url, file_name, configuration=config)
        except Exception as e:
            file_name = DIR + remove_unwanted(contest_title) + ".pdf"
            pdfkit.from_url(get_url, file_name, configuration=config)