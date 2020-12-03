import plac
import os
from pywgsim import wgsim


@plac.pos('genome', "FASTA reference sequence")
@plac.pos('read1', "FASTQ file for first in pair (read1.fq)")
@plac.pos('read2', "FASTQ file for second in pair (read2.fq)")
@plac.opt('err', "the base error rate", abbrev='e', type=float)
@plac.opt('mut', "rate of mutations", abbrev='r', type=float)
@plac.opt('frac', "fraction of indels", abbrev='R', type=float)
@plac.opt('ext', "probability an indel is extended", abbrev='X', type=float)
@plac.opt('dist', "outer distance between the two ends", abbrev='D', type=int)
@plac.opt('stdev', "standard deviation", abbrev='s', type=int)
@plac.opt('L1', "length of the first read", abbrev='1', type=int)
@plac.opt('L2', "length of the second read", abbrev='2', type=int)
@plac.opt('num', "number of read pairs", abbrev='N', type=int)
@plac.opt('seed', "seed for the random generator", abbrev='S', type=int)
@plac.opt('amb', "disregard if the fraction of ambiguous bases higher than FLOAT", abbrev='A', type=float)
@plac.flg('fixed', "each chromosome gets N sequences", abbrev='f')
def cmd(genome, read1="read1.fq", read2="read2.fq", err=0.02, dist=500, stdev=50, num=1000, L1=70, L2=70,  mut=0.001,
        frac=0.15, ext=0.25,  seed=0, amb=0.05, fixed=False,):

    # Sanity check on the parameters.
    seed = 0 if not seed else int(seed)
    fixed = int(fixed)

    wgsim.core(ref=genome, r1=read1, r2=read2, err_rate=err, dist=dist, stdev=stdev,
               N=num, mut_rate=mut, indel_frac=frac, indel_ext=ext, size_l=L1, size_r=L2, max_n=amb,
                 seed=seed, is_fixed=fixed)

    pass

def run():
  plac.call(cmd)


if __name__ == '__main__':
    run()



