#! python3
# 9_mclip.py - A multi-clipboard program

TEXT = {'agree':"""Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell':"""Would you consider making this a monthly donation?"""}
import sys, pyperclip

try:
    print(sys.argv[0])
    print(sys.argv[1:])
except:
    print('deu não')

if len(sys.argv) < 2:
    print('Usage: python 6_mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)