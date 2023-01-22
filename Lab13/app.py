from textblob import TextBlob


def hello(name):
    return "Hello {}".format(name)


def extract_sentiment(text):
    text = TextBlob(text)
    if text.sentiment.polarity > 0:
        return True
    else:
        return False


def text_contain_word(word: str, text: str):
    return word in text


def bubbleSort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
