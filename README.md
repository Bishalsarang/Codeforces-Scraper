
# Codeforce-Contests-Scrapper
A simple scrapper made in python for the purpose of downloading codeforce contests as pdf <br>
[Sample PDF](https://drive.google.com/file/d/1dWMhj5KySMQNa9gSAJBG_vX2Svm2985Z/view?usp=sharing) for CF Beta Round 13

You  can download pdfs from all codeforces contest currently upto Codeforces Round #542 from [here](https://drive.google.com/open?id=1bvspBHcORvqBGyXzhD5TR1HHlOORMCK6)


Requirements:
1. [wkhtmltopdf](https://wkhtmltopdf.org/)
2. pdfkit
3. requests

Install Dependencies:
```
pip install requests
pip install pdfkit
pip install wkhtmltopdf
```
Usage:
```
python scrapper.py
```

Note for Windows Users:
Download wkhtmltopdf executable from [here](https://wkhtmltopdf.org/) and set the path path of executable in scrapper.py file accordingly
by updating <em>path_wkhtmlpdf</em> to path of <strong>wkhtmltopdf.exe</strong>

![Config](https://github.com/sarangbishal/Codeforce-Contests-Scrapper/blob/master/config.JPG)

Screenshots

![Screenshots](https://github.com/sarangbishal/Codeforce-Contests-Scrapper/blob/master/sc.JPG)

<hr>

![Screenshots](https://github.com/sarangbishal/Codeforce-Contests-Scrapper/blob/master/linux.JPG)
<hr>


![Screenshots](https://github.com/sarangbishal/Codeforce-Contests-Scrapper/blob/master/Capture.JPG)
