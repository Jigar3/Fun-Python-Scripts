#  import os
#
# myFile = open( "beautiful-soap-example.py" , 'a')
# myFile.write('Hi')
# import webbrowser
#
# brainy_quote = webbrowser.open('https://www.brainyquote.com/topics/inspirational')
from bs4 import BeautifulSoup
import requests, json, sys, pprint

strOb = "Age Alone Amazing Anger Anniversary Architecture Art Attitude Beauty Best Birthday Brainy Business Car Chance Change Christmas Communication Computers Cool CourageDadDatingDeathDesignDietDreams Easter Education Environmental Equality Experience Failure Faith Family Famous FatherDay Fear Finance Fitness Food Forgiveness Freedom Friendship Funny Future Gardening God Good Government Graduation Great Happiness Health History Home Hope Humor Imagination Independence Inspirational Intelligence Jealousy Knowledge Leadership Learning Life Love Marriage Medical MemorialDay Men Mom Money Morning MothersDay Motivational Movies Moving On Music Nature New YearsParenting Patience Patriotism Peace Pet Poetry Politics Positive Power Relationship Religion Respect Romantic Sad Saint PatricksDay Science Smile Society Space Sports Strength Success Sympathy Teacher Technology Teen Thankful Thanksgiving Time Travel Trust Truth ValentinesDay VeteransDay War Wedding Wisdom Women"

newStr = strOb.lower()
list1 = newStr.split(' ')
pprint.pprint(list1)
print('Enter the Topic: ')

topic = input()

brainy_quote = requests.get('https://www.brainyquote.com/topics/' + topic)

soup = BeautifulSoup(brainy_quote.content, 'html.parser')
filename = topic

quotes = open( str(topic)+'.txt', 'w')
authors = soup.find_all('a', title="view author", )
i=0

for lines in soup.find_all('a', title="view quote"):
    quotes.write('Quote: ' + lines.text + '\n')
    if(i<len(authors)):
        quotes.write('Author: ' + authors[i].text + '\n\n')
    i=i+1
