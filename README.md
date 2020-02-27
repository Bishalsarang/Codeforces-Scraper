
# Codeforce-Scrapper
A simple scrapper made in python for the purpose of downloading codeforce contests and problems as pdf <br>
It allows downloading problem based on contest id, rating, difficulty adn tags
[Sample PDF](https://drive.google.com/file/d/1dWMhj5KySMQNa9gSAJBG_vX2Svm2985Z/view?usp=sharing) for CF Beta Round 13

You  can download pdfs from all codeforces contest currently upto Codeforces Round #542 from [here](https://drive.google.com/open?id=1bvspBHcORvqBGyXzhD5TR1HHlOORMCK6)


### Requirements:
1. [wkhtmltopdf](https://wkhtmltopdf.org/)
2. pdfkit
3. requests
4. bs4


### Install Dependencies:
```
pip install requests
pip install pdfkit
pip install wkhtmltopdf
pip install bs4
```
### Usage:
1. Show help 
```
python scrapper.py -h
```
2. Download contest problem from certain contest id 300 upto contest id 302 <br>
View help to know what switch -m, -l and -c are
```
python scrapper.py -m contest -l 300 -u 302
```
3. Download  problems with rating 1200-1300 order by solved
```
python scrapper.py -m p  -t 1200-1300 -o solved 
```
4. Download problems with tag dp
```
python scrapper.py -m p -t dp
```
5. Download problems with tag dp and binary search ordered by solved<br>
<i>Note:</i> Enclose tags inside quotes if it is more than 1 word
```
python scrapper.py -m p -t dp -o solved
python scrapper.py -m p -t "binary search" -o solved
```
6. Download all problems with tag dp ordered by rating
```
python scrapper.py -m p -t dp -o rating
```
7. Download all problems with tag dp ordered by solved in ascending order <br>
Change to -asc False to download in descending order 
```
python scrapper.py -m p -t dp -o solved -asc True
```
8. Download maximum of 10 problems with tag dp ordered by solved in ascending order 
```
python scrapper.py -m p -t dp -o solved -asc True -n 10
```
9. Download maximum of 10 problems with any tag ordered by solved in ascending order 
```
python scrapper.py -m p  -o solved -asc True -n 10
```
10. Download maximum of 10 problems with any tag ordered by rating in ascending order 
```
python scrapper.py -m p  -o rating -asc True -n 10
```

#### Note: Combine switches similarly as per your convenience to download problems based on your query


### Note for Windows Users:
Download wkhtmltopdf executable from [here](https://wkhtmltopdf.org/) and set the path path of executable in scrapper.py file accordingly
by updating <em>path_wkhtmlpdf</em> to path of <strong>wkhtmltopdf.exe</strong>

![Config](https://github.com/sarangbishal/Codeforce-Contests-Scrapper/blob/master/config.JPG)


### Updates:
1. Feature to download contest based on contest ID
2. Feature to download problemset base on ratings, tags (In progress)

### Screenshots

![Screenshots](https://github.com/Bishalsarang/Codeforces-Scrapper/blob/master/sc.JPG)

<hr>

![Screenshots](https://github.com/Bishalsarang/Codeforces-Scrapper/blob/master/linux.JPG)
<hr>


![Screenshots](https://github.com/Bishalsarang/Codeforces-Scrapper/blob/master/Capture.JPG)
