# AutoText/AutoType

Two sets of scripts for messing with people. Both are ways of reading out a file either line-by-line or word-by-word into another application. AutoText will automatically send using Messages in the background on Mac. AutoType can be used to send using any messaging application, but you will have to navigate into the window and stay there while it runs.
Setup:

1. Make sure you have a valid Python 3 install with pip package manager!
2. Install the dependencies of the script with `pip install -r requirements.txt`

## LyricSpammer
1. `python3 main.py`

## AutoText

This is a simple script which takes in a text file argument and reads the file line-by-line, sending it through the MacOS Messages app to a friend who is also on Apple Messages. Note that it will only work if you have texted the number previously on Messages.

1. Run the script with `python3 autotext.py <filepath> <phonenumber>`. Make sure the phone number is in a standard format, either with dashes and parentheses or without works.
   1. You can make the script go by line with the arg `--byline`, so `python3 autotype.py --byline <filepath>`.
   2. Defalut time delay between texts is 1 second, you can change it with the arg `-t <desired delay in seconds>`, so `python3 autotype.py -t 5 <filepath>` for a five second delay.
2. Watch the script work!

## AutoType

This is a simple script which takes in a text file argument and reads the file line-by-line, typing it into the current in focus window on your machine (very useful for texting a friend the entire script of The Bee Movie for example).  

1. Run the script with `python3 autotype.py <filepath>`. This will run the script typing out each word in the file on its own with a 3 second delay before starting.

   1. You can make the script go by line instead of word by word with the arg `--byline`, so `python3 autotype.py --byline <filepath>`.
   2. You can also increase the time delay with the arg `-t <int for desired delay in seconds>`, so `python3 autotype.py -t 5 <filepath>` for a five second delay.
2. There will be a 3 second delay for you to navigate to the window and text field you want to type in before it begins. If you want to change this time, simply edit the `time_delay` variable at the top of autotype.py
3. Watch the script work!
