# JaneStreetOctober
Brute force solution to the jane street puzzle for October 2024

To run do:

python index.py | python map_out.py | python score.py

(Will indicate proper paths to get 2024)
To convert the path to chess notation just stick one of the lists into 'parse.py'

With the benefit of hindsight I should have just used text files to store all the variables instead of piping everything, but my goal for this project was to do things quickly which meant making expedient decisions (like using random.random())

If it takes to long to run:

Change the line in index.py: "if len(previous_moves) > 12:" to a smaller number

Change the multipication of all random.random() to a larger number (like 15)
