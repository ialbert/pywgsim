import plac
from pywgsim import wgsim


@plac.opt('r1', "name for first in pair", abbrev='a')
@plac.opt('r2', "name for second in pair ", abbrev='b')
@plac.pos('genome', "the FASTA reference sequence")
@plac.opt('err', "the base error rate", abbrev='e', type=float)
@plac.opt('mut', "rate of mutations", abbrev='r', type=float)
@plac.opt('frac', "fraction of indels", abbrev='R', type=float)
@plac.opt('ext', "probability an indel is extended", abbrev='X', type=float)
@plac.opt('dist', "outer distance between the two ends", abbrev='D', type=int)
@plac.opt('stdev', "standard deviation", abbrev='s', type=int)
@plac.opt('len1', "length of the first read", abbrev='1', type=int)
@plac.opt('len2', "length of the second read", abbrev='2', type=int)
@plac.opt('num', "number of read pairs", abbrev='N', type=int)
@plac.opt('seed', "seed for the random generator", abbrev='S', type=int)
@plac.flg('fixed', "each chromosome gets N sequences", abbrev='f')
def cmd(genome, r1="1.fq", r2="2.fq", num=1000, fixed=False, err=0.02, mut=0.001, frac=0.15, ext=0.25, dist=500, stdev=50, seed=0):

    seed = 0 if not seed else int(seed)
    fixed = int(fixed)

    wgsim.core(r1=r1, r2=r2, N=num, ref=genome, err_rate=err, mut_rate=mut, indel_frac=frac, indel_ext=ext,
               dist=dist, stdev=stdev, seed=seed, is_fixed=fixed)

    pass

def run():
  plac.call(cmd)


if __name__ == '__main__':
    run()



