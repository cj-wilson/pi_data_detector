import random
import re
import helper as h
import csv
import string

# helper for flattening a list
def flatten(x):
    if isinstance(x, list):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

# helper for removing and replacing punctuation
def stem(s):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    out = regex.sub(' PUNCT ', s)
    return out

# helper to change the label for PUNCT tokens to 'punct'
def update_label(val, label):
    out = []
    for v, l in zip(val, label):
        if v == 'PUNCT':
            l = 'punct'
        out.append(l)
    return out


# setup stuff
n = 0
l = []
outfile = "../data/fake_data.csv"

# basic string
for i in range(0,10000):
    # string to list
    words = h.words()

    # create same size list of words
    label = ["word"] * len(words)

    # generate a fake
    y = h.gen_fake()
    # cleaning punct
    # may look into adding a new label for punct
    y['value'] = stem(y['value'])

    y_val = re.split("\\s+", y['value'])
    newlabel = [y['label']] * len(y_val)

    newlabel = update_label(y_val, newlabel)

    # insert into word
    idx = random.choice(range(0, len(words)))
    words[idx] = y_val 
    label[idx] = newlabel

    words = flatten(words)
    label = flatten(label)
    sentence = [n] * len(words)

    l.append([sentence, words, label])
    n = n + 1

# write out to file
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["sentence", "word", "label"])
    for item in l:
        # transpose the lists before writing out
        item_tx = list(map(list, zip(*item)))
        
        # loop over items in tx list
        for i in range(len(item_tx)):
            writer.writerow(item_tx[i])

