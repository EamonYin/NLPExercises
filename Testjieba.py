import jieba
import jieba.analyse
import jieba.posseg as pseg
import codecs, sys


def cut_word(sentens):
    return ' '.join(jieba.cut(sentens)).encode('utf-8')


f = codecs.open('/Users/eamonyin/Downloads/迪哥nlp/练习/Gemsim练习/wiki_zh_simple.txt', 'r', encoding='utf-8')
target = codecs.open('/Users/eamonyin/Downloads/迪哥nlp/练习/Gemsim练习/wiki_zh_fenci.txt','w',encoding='utf-8')
print('open file')
line_num = 1
line = f.readline()
while line:
    print('---- processing ', line_num, 'article-----------')
    line_seg = ' '.join(jieba.cut(line))
    target.writelines(line_seg)
    line_num = line_num + 1
    line = f.readline()

f.close()
target.close()
exit()
