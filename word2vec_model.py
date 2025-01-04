import logging
import os.path
import multiprocessing
from gensim.corpora import wikicorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import codecs, sys

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)')
    logging.root.setLevel(level=logging.INFO)
    logger.info('running %s' % ' '.join(sys.argv))

    if len(sys.argv) < 4:
        print(globals()['__doc__'] % locals())
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]
    with open(inp, 'r', encoding='utf-8', errors='ignore') as file:
        model = Word2Vec(LineSentence(file), vector_size=400, window=5, min_count=5, workers=int(multiprocessing.cpu_count()))
    model.wv.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)
