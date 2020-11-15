# Lyric Spammer

![heroImage](https://github.com/ShaylanDias/LyricSpammer/blob/master/lyricspammer.jpg)

This app provides a GUI which allows you to search for a song, then send the lyrics to a friend line-by-line over text.
Keep in mind that this will only work on a machine running OSX which is logged into Messages.

Shaylan developed the API, web scraping, and Applescript contact searching/texting while David McAllister created most of the GUI.

## Functionality

This uses a Flask API have set up for retrieving song names and images which is hosted on Heroku. It then feeds that information to a local web scraper to get the lyrics.
These lyrics are then sent through the OSX Messages app to the desired Contact/Number using AppleScript. I have to credit https://github.com/adhorrig/azlyrics for providing the majority
of the web scraping code which was then modified to fit our needs.

## Setup:

1. Follow the README in the app directory to use it with our API. If you want to set up your own API follow the instructions in the website README and deploy it to a host of your choice (we used Heroku since it was easy and free).
