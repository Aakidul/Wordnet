import nltk
from nltk.corpus import wordnet
nltk.download("wordnet")
import os
os.system("clear")
print("""


 _    _ _________________ _   _ _____ _____
| |  | |  _  | ___ |  _  | \ | |  ___|_   _|
| |  | | | | | |_/ | | | |  \| | |__   | |
| |/\| | | | |    /| | | | . ` |  __|  | |
\  /\  \ \_/ | |\ \| |/ /| |\  | |___  | |
 \/  \/ \___/\_| \_|___/ \_| \_\____/  \_/

[ SEARCH THE DEFINITION OF THE THINGS..]
[ JUST ENTER THE THING NAME ]


""")

while True:
    user_input = input("ENTER: ")
    synsets = wordnet.synsets(user_input)

    if synsets:
        syn = synsets[0]
        print("\n")
        print("Definition:", syn.definition())
        print("\n")
        print("Examples:", syn.examples())
    else:
        print("No Definition Found.")
