import pyphen
import random

def combine_words(words, num_results=10, lang='en_US'):
  if lang not in pyphen.LANGUAGES:
    print 'Language %s not found!' % lang
    return []

  d = pyphen.Pyphen(lang=lang)

  bags = []

  for word in words:
    parts = d.inserted(word).split('-')
    bags.append(parts)

  for x in range(0, num_results):
    num_samples = random.randint(2, len(bags)-1)
    pick_from = random.sample(bags, num_samples)

    name = ''
    for bag in pick_from:
      name += bag[random.randint(0,len(bag)-1)]

    print name

