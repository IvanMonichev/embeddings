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