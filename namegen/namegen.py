import pyphen

def combine_words(words, lang='en_US'):
  if lang not in pyphen.LANGUAGES:
    print 'Language %s not found!' % lang
    return []

  d = pyphen.Pyphen(lang=lang)

  for word in words:
    parts = d.inserted(word).split('-')
    print parts

