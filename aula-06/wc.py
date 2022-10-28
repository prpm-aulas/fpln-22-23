from wordcloud import WordCloud

d = {'hello': 3, 'world': 1, 'Olá': 2, 'mundo': 10, 'adeus': 3}

# gerar a nuvem
wc = WordCloud().generate_from_frequencies(d)

# desenhar a nuvem
image = wc.to_image()
image.show()
