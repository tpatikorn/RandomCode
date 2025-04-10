import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from os import path


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(44.0)
    s = int(80.0)
    l = int(float(random_state.randint(60, 100)))

    return "hsl({}, {}%, {}%)".format(h, s, l)


DS_mask = np.array(Image.open(path.join("DS.png")))

keyword = "ai"

with open("text/" + keyword + ".txt", "r", encoding="utf8") as f:
    txt = f.read()
    cloud = WordCloud(width=800, height=240, max_words=200, mask=DS_mask,
                      background_color="#4499DD", color_func=random_color_func,
                      max_font_size=100, min_font_size=10,
                      contour_width=10, contour_color="grey").generate(txt)
    cloud.to_file("wordcloud/"+keyword+".png")
