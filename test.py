def artifact(*args, **kwargs):
    text = {}
    for word in args:
        for i in kwargs:
            if i == 'short':
                text[i] = short(kwargs[i], word)
            if i == 'absence':
                text[i] = absence(kwargs[i], word)
            if i == 'up_dig':
                text[i] = up_dig(kwargs[i], word)
    return text


def short(n, word):
    if len(word) <= n:
        return word


def absence(n, word):
    if n not in word:
        return word


def up_dig(n, word):
    if n == 1:
        if not word.islower():
            return word
    if n == 3:
        if not word.isalpha():
            return word


things = [
    "Stone", "object", "box",
    "rock", "Crystal", "Bowl"
]
params = {
    "short": 5,
    "absence": "B",
    "up_dig": 1
}
print(artifact(*things, **params))