import json


with open("./stop_words_spanish.txt") as stopwords:
    stopwords = [word[:-1] for word in stopwords]
    #print(stopwords)

words = []
books = [f"./libro{i}.txt" for i in range(1, 7)]

matrix = {}

for bookname in books:
    with open(bookname) as libro:
        for parrafo in libro:
            if parrafo == "\n":
                continue
            parrafo = parrafo[:-1]
            for word in parrafo.split():
                if word.endswith((".", ",", ":", ";")): 
                    word = word[:-1]
                
                if word in stopwords:
                    continue

                if word in matrix:
                    matrix[word] = matrix[word] |  2** books.index(bookname)
                else:
                    matrix[word] = 2** books.index(bookname)

with open("matrix.json", 'w') as matrixjson:
    json.dump(matrix, matrixjson, indent=4)