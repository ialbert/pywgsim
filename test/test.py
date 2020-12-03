from pywgsim import wgsim
import os

TEST_DIR = os.path.dirname(__file__)


def test_run(capsys=None):

    r1 = os.path.join(TEST_DIR, "read1.fq")
    r2 = os.path.join(TEST_DIR, "read2.fq")

    ref = os.path.join(TEST_DIR, "lambda.fa")

    wgsim.core(r1=r1, r2=r2, ref=ref, N=1000, indel_frac=0.5, seed=1)

    assert 1


if __name__ == '__main__':
    test_run()