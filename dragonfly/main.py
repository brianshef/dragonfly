import argparse
from os import environ
from dragonfly import app

# argparse
_description='''
A Markov Chain generator based on song lyrics.
Also mixes in text from the artist Wikipedia page
in order to give the sentences a better structure.
Adjust the weights using the option to play with the
relative amounts of material used in rendering the final model.
'''
_epilog='''
Best invoked like pipenv run python main.py, OR
pipenv run python main.py --artist "Coheed and Cambria" --wiki "Coheed_and_Cambria" | tee output.txt
'''


def configure():
    parser = argparse.ArgumentParser(description=_description, epilog=_epilog)
    parser.add_argument('--artist', '-a', default="Coheed and Cambria", required=False)
    parser.add_argument('--wiki', '-w', default="Coheed_and_Cambria", required=False)
    parser.add_argument('--songs', '-s', default=10, required=False, type=int)
    parser.add_argument('--number', '-n', default=5, required=False, type=int)
    parser.add_argument('--lyric-weight', '-p', default=1.0, required=False, type=float)
    parser.add_argument('--wiki-weight', '-q', default=0.0, required=False, type=float)
    return parser.parse_args()


def main():
    app.main(
        configure(), 
        environ.get('GENIUS_CLIENT_ACCESS_TOKEN')
    )
    

if __name__ == "__main__":
    main()
