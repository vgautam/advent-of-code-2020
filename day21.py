#!/usr/bin/env python3
from collections import Counter
from collections import defaultdict

day=21 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test21'

lines = [l.strip() for l in open(inp_f)] # every line

allergen_word_dict = defaultdict(Counter)
allergen_count = defaultdict(int)
all_words = set()
recipes = []
for l in lines:
    _spl = l.split('(')
    words = _spl[0].strip().split()
    all_words.update(words)
    recipes.append(words)
    if len(_spl) > 1:
        allergens = _spl[1].split(')')[0].split('contains ')[1].split(', ')
        for allergen in allergens:
            allergen_word_dict[allergen].update(words)
            allergen_count[allergen] += 1

final_allergen_word_map = {}
words_accounted_for = set()
sus_words = set()
for allergen in allergen_word_dict:
    counter = allergen_word_dict[allergen]
    candidate_words = {word: counter[word] for word in counter if word not in words_accounted_for}
    unanimous_max = True
    max_count = max([v for k,v in counter.items()])
    max_words = []
    for word in counter:
        if word not in words_accounted_for and counter[word] == max_count:
            if max_words:
                unanimous_max = False
            max_words.append(word)
    if max_count == allergen_count[allergen]:
        if unanimous_max:
            #print('HERE', max_words[0])
            final_allergen_word_map[allergen] = max_words[0] # should i switch up the order?
            words_accounted_for.add(max_words[0])
        else:
            for x in max_words:
                sus_words.add(x)
    else:
        print('problem zone')
        print(allergen, allergen_count[allergen], max_count, max_words, unanimous_max)

print('part 1')
ok_words = all_words - words_accounted_for - sus_words
total = 0
for ingredients in recipes:
    total += sum([1 for word in ingredients if word in ok_words])
print(total)

print('part 2')
words_accounted_for.update(ok_words)

while len(sus_words):
    # lots of duplication from part 1 but i cbf
    sus_words = set()
    for allergen in allergen_word_dict: #sus_words - set(final_allergen_word_map.values()):
        counter = allergen_word_dict[allergen]
        candidate_words = {word: counter[word] for word in counter if word not in words_accounted_for}
        unanimous_max = True
        max_count = max([v for k,v in counter.items()])
        max_words = []
        for word in counter:
            if word not in words_accounted_for:
                if counter[word] == max_count:
                    if max_words:
                        unanimous_max = False
                    max_words.append(word)
        if max_count == allergen_count[allergen]:
            if unanimous_max and max_words:
                final_allergen_word_map[allergen] = max_words[0]
                words_accounted_for.add(max_words[0])
            else:
                for x in max_words:
                    sus_words.add(x)
print(','.join([final_allergen_word_map[k] for k in sorted(final_allergen_word_map)]))
