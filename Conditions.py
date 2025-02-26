# check for vinegere cipher conditions
def fequenyofwords(text):
    text = text.lower()
    text = text.split()
    freq = {}
    for word in text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
