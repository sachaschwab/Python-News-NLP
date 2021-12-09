# Python-News-NLP

NLP engine and clustering of same-event news articles. Any ideas and feedback are warmly welcome.

## Structure
.<br>

| Path | Comment |
| --- | --- |
|-- python-news-nlp/| Python project |


    # <br>
 |-- data/              # Sample data (see below)<br>
 |-- docs/<br>
 |-----notebook.ipynp   # Walk through the code<br>

## Quick outline
<ul style="line-height: 1.5; font-size:12pt">
  <li>Preprocessing raw news articles data. Columns: 'title' | 'body_text' | 'date' (%Y-%m-%d)</li>
  <li>NLP keyword extraction based on TF-IDF weights (top n keywords)</li>
  <li>NLP sentiment analysis</li>
  <li>NLP named entity extraction</li>
</ul>

## Requirements
<ul style="line-height: 1.5; font-size:12pt">
  <li>Python 3.7</li>
  <li>git</li>
  <li>Jupyter Notebook IDE if you want to get a walk through the text and general Data Science-style comments</li>
</ul>

## Dependencies
<ul style="line-height: 1.5; font-size:12pt">
  <li>Pandas</li>
  <li>NLTK (pip install -U nltk)</li>
</ul>

## Limitations
<ul style="line-height: 1.5; font-size:12pt">
  <li>Text processing (stemming, stopwords etc.) currently limited to English</li>
</ul>

## Demo data
Folder /data contains a random subset (400 items) of the Kaggle "All the news" dataset. Full dataset available here: https://www.kaggle.com/snapcrack/all-the-news