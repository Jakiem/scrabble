from collections import Counter


def scrabble(string, word):
    w = Counter(word.lower())
    s = Counter(string.lower())
    count = 0
    for i in word:
        if s[i] >= w[i]:
            count += 1
    if count >= len(word):
        return True
    return False
  



scrabble('begsdhhtsexoult', 'hexlet')
scrabble('rkqodlw', 'world')
scrabble('begsdhhtsexoult', 'hexlet')
scrabble('katas', 'steak')
scrabble('scriptjava', 'javascript')
scrabble('scriptingjava', 'javascript')
scrabble('scriptjavest', 'javascript')
scrabble('', 'hexlet')
scrabble('scriptingjava', 'JavaScript')