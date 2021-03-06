# NewsRepository 

## About
This project is a simple web application which allows English learners to read English news more effectively

## Features
- Collection of news articles from authoritative sources
- Easy on-demand dictionary feature to look up words and their meaning
- Save cool words for learning
- Save news article for learning
- Test yourself on saved words

## Phases
- [x] News article scraping scripts
- [x] News API

### News scraping
- [x] Create RDS instance to save the news
- [x] Create AWS Lambda scripts to read news and save into RDS database
- [x] Create NewsAPI to serve the news

## Structure
### App 
To be updated

### NewsAPI
Current url: https://articlesfinder.net
```
/about
```
Display information regarding the API
```
/news/all?limit=..&after_id=..
```
Getting all the news
```
/news/byid?id[]=1&id[]=30
```
Getting news by id