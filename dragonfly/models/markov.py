import markovify
import json


def from_text(lines=[]):
    return markovify.Text(''.join(lines))


def from_json(data={}):
    return markovify.Text.from_json(data) 


def save_file(model, filename):
    with open(filename, 'w') as outfile:
        json.dump(to_json(model), outfile)


def load_file(filename, handler=None):
    try:
        with open(filename) as f:
            return from_json(json.load(f))
    except Exception as e:
        handler(e)
        return None


def to_json(model):
    return model.to_json()


def combine_models(models=[], weights=[]):
    assert(len(models) == len(weights))
    return markovify.combine(models, weights)


def generate_sentences(model, num_sentences=1, max_length=140):
    for _ in range(num_sentences):
        print('\n{}'.format(model.make_short_sentence(max_length)))
