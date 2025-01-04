from gensim.models import Word2Vec
from gensim.models import KeyedVectors

en_wiki_word2vec_model = KeyedVectors.load('/Users/eamonyin/Downloads/迪哥nlp/练习/Gemsim练习/wiki.zh.text.model')

# 测试 和这5个词向量最近的词
testwords = ['苹果', '数学', '学术', '白痴', '篮球']
for i in range(5):
    res = en_wiki_word2vec_model.most_similar(testwords[i]) #most_similar()最相近的词
    print(testwords[i])
    print(res)
