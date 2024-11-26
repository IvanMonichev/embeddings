import re

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


def check_words_in_model(model):
    words = ['веб-страница_NOUN', 'веб_NOUN', 'день_NOUN', 'ночь_NOUN', 'человек_NOUN', 'семантика_NOUN',
             'биткоин_NOUN', 'сибирь_PROPN']

    for word in words:
        # есть ли слово в модели?
        if word in model:
            print(word)
            # смотрим на вектор слова (его размерность 300, смотрим на первые 10 чисел)
            print(model[word][:10])
            # выдаем 10 ближайших соседей слова:
            for word, sim in model.most_similar(positive=[word], topn=10):
                # слово + коэффициент косинусной близости
                print(word, ': ', sim)
            print('\n')
        else:
            # Увы!
            print('Увы, слова "%s" нет в модели!' % word)


def download_nltk_resource(resource_name, download_dir):
    """
    Загружает указанный ресурс NLTK, устраняя проблемы с SSL-сертификатами.

    :param download_dir: Директория для загрузки ресурса
    :param resource_name: str, Имя ресурса для загрузки (например, 'punkt', 'stopwords').
    """
    try:
        # Попытка загрузки ресурса
        nltk.download(resource_name, download_dir=download_dir)
        print(f"Ресурс '{resource_name}' успешно загружен.")
    except Exception as e:
        print(f"Ошибка при загрузке ресурса '{resource_name}': {e}")


def review_to_wordlist(review, remove_stopwords=False):
    # убираем ссылки вне тегов
    review = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", " ", review)
    # достаем сам текст
    review_text = BeautifulSoup(review, "lxml").get_text()
    # оставляем только буквенные символы
    review_text = re.sub("[^a-zA-Z]", " ", review_text)
    # приводим к нижнему регистру и разбиваем на слова по символу пробела
    words = review_text.lower().split()
    if remove_stopwords:
        # убираем стоп-слова
        stops = stopwords.words("english")
        words = [w for w in words if not w in stops]

    return (words)


def review_to_sentences(review, tokenizer, remove_stopwords=False):
    raw_sentences = tokenizer.tokenize(review.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append(review_to_wordlist(raw_sentence, remove_stopwords))
    return sentences


def clean_and_tokenize(data):
    print("Parsing sentences from training set...")
    tokenizer = nltk.data.load('./content/data/tokenizers/punkt/english.pickle')
    sentences = []
    for review in data["review"]:
        sentences += review_to_sentences(review, tokenizer)

    return sentences
