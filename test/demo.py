from pywgsim import wgsim
import os

TEST_DIR = os.path.dirname(__file__)


if __name__ == '__main__':

    r1 = os.path.join(TEST_DIR, "r1.fq")
    r2 = os.path.join(TEST_DIR, "r2.fq")

    ref = os.path.join(TEST_DIR, "lambda.fa")

    wgsim.core(r1=r1, r2=r2, ref=ref, N=1000, indel_frac=0.5)
