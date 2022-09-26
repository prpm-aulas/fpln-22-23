import os
import re

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def import_words(text, words_counter):
    words_list = re.findall(r'\w+', text)
    for word in words_list:
        if word not in words_counter:
            words_counter[word] = 1
            continue
        
        words_counter[word] += 1
    
    return words_counter


def makeImage(text):
    alice_mask = np.array(Image.open("fpessoa-mask.png"))

    wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
    # generate word cloud
    wc.generate_from_frequencies(text)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


words_counter = {}
path = "poemas/"
for poema_file in os.listdir(path):
    poema_path = os.path.join(path, poema_file)
    with open(poema_path, 'r') as f:
        t = f.read()
        words_counter = import_words(t, words_counter)

words_counter = dict(sorted(words_counter.items(), key=lambda item: item[1], reverse=True))

makeImage(words_counter)
