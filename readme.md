# embeddings

## Инструкция по развертыванию

1. Скачиваем модель в директорию content
```bash
mkdir -p content && wget -P content http://vectors.nlpl.eu/repository/20/180.zip
```

2. Разархивируем модель в директорию model

```bash
unzip ./content/180.zip -d ./model
```

3. Скачивает датасет
```bash
mkdir -p content/data && wget -P content/data https://raw.githubusercontent.com/ancatmara/data-science-nlp/master/data/w2v/train/unlabeledTrainData.tsv
```

4. Если возникают проблемы с SSL, необходимо перейти в директорию где установлен Python 3.12 и выполнить команду
```bash
./Install\ Certificates.command 
```