import urllib.request  # библиотека для скачивания данных

import gensim  # библиотека для загрузки и использования моделй w2v
import pandas
from gensim.models import word2vec  # непосредственно методы w2v

from utils import check_words_in_model, download_nltk_resource, clean_and_tokenize

MODEL_PATH = './model/model.bin'


def similarity(word1, word2, model):
    print(model.similarity(word1, word2))


def load_model(model_path):
    return gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)


if __name__ == '__main__':
    # model_ru = load_model(MODEL_PATH)
    # check_words_in_model(model_ru)
    # similarity('человек_NOUN', 'обезьяна_NOUN', model_ru)

    data = pandas.read_csv("./content/data/unlabeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
    download_nltk_resource('punkt', './content/data')
    sentences = clean_and_tokenize(data)

    print(sentences)