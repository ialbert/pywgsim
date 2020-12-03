from pywgsim import wgsim
import os

TEST_DIR = os.path.dirname(__file__)
TEST_REF = os.path.join(TEST_DIR, "lambda.fa")

if __name__ == '__main__':
    wgsim.core(r1="read1.fq", r2="read2.fq", ref=TEST_REF, N=100, indel_frac=0.5)
