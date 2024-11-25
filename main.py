import urllib.request  # библиотека для скачивания данных
import gensim  # библиотека для загрузки и использования моделй w2v
from gensim.models import word2vec  # непосредственно методы w2v

MODEL_PATH = './model/model.bin'


def similarity(word1, word2, model):
    print(model.similarity(word1, word2))

def check_words_in_model(model):
    words = ['веб-страница_NOUN', 'веб_NOUN', 'день_NOUN', 'ночь_NOUN', 'человек_NOUN', 'семантика_NOUN',
             'биткоин_NOUN', 'сибирь_PROPN']

    for word in words:
        # есть ли слово в модели?
        if word in model_ru:
            print(word)
            # смотрим на вектор слова (его размерность 300, смотрим на первые 10 чисел)
            print(model_ru[word][:10])
            # выдаем 10 ближайших соседей слова:
            for word, sim in model_ru.most_similar(positive=[word], topn=10):
                # слово + коэффициент косинусной близости
                print(word, ': ', sim)
            print('\n')
        else:
            # Увы!
            print('Увы, слова "%s" нет в модели!' % word)


def load_model(model_path):
    return gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)


if __name__ == '__main__':
    model_ru = load_model(MODEL_PATH)
    check_words_in_model(model_ru)
    similarity('человек_NOUN', 'обезьяна_NOUN', model_ru)

