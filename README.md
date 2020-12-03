## pywsgim

pywgsim is a python wrapper around the wgsim short read simulator

* https://github.com/lh3/wgsim

## Usage

    pywgsim -h

or

    python -m pywgsim
    
## Installation

    pip install pywgsim
    
## API

The interface to `wgsim` can be made in a single function call 

    from pywgsim import wgsim

    wgsim.core(r1="r1.fq", r2="r2.fq", ref="genome.fa", err_rate=0.02, mut_rate=0.001, indel_frac=0.15, indel_ext=0.25, max_n=0.05, is_hap=0, N=100000,  dist=500, stdev=50, size_l=100, size_r=100, is_fixed=0, seed=0)

                
## Changes

The original code for wgsim has been expanded a little bit. The main changes are:

1. The information on the mutations introduced by `wgsim` are now generated in GFF format.
1. There is a new flag called `--fixed` that generates the same `N` number of reads for each chromosome.
1. The separator character in the read name has been changed from `_` to `|`. This follows a more widely accepted standard (i.e. NCBI) and allows identifying the contig name from the read name. 

In the default operation of wgsim the `N` reads are distribute such to create a uniform coverage across all chromosomes (longer chromosomes get a larger fraction of N)
 
Example mutation output:

    ##gff-version 3
    #
    # N=1000 err_rate=0.02 mut_rate=0.001 indel_frac=0.15000001 indel_ext=0.25 size=500 std=50 len1=100 len2=100 seed=1606965870
    #
    NC_001416.1     wgsim   snp     1047    1047    .       +       .       Name=A/C;Ref=A;Alt=C;Type=hom
    NC_001416.1     wgsim   snp     1308    1308    .       +       .       Name=C/Y;Ref=C;Alt=Y;Type=het
    NC_001416.1     wgsim   snp     1533    1533    .       +       .       Name=G/T;Ref=G;Alt=T;Type=hom
    NC_001416.1     wgsim   snp     2472    2472    .       +       .       Name=C/M;Ref=C;Alt=M;Type=het
    NC_001416.1     wgsim   snp     2964    2964    .       +       .       Name=A/M;Ref=A;Alt=M;Type=het
    NC_001416.1     wgsim   snp     5375    5375    .       +       .       Name=G/R;Ref=G;Alt=R;Type=het
    
Read names are now of the form:

       @NC_002945.4|1768156|1768694|0:0:0|4:0:0|4

Where:

   * `NC_002945.4` is the contig name that the fragment was generated from.
   * `1768156` is the left-most position of the fragment.
   * `1768694` is the right-most position of the fragment.
   * `0:0:0` are the number of errors, substitutions and indels in the left-most read of the pair.
   * `4:0:0` are the number of errors, substitutions and indels in the right-most read of the pair.
   * `4` is the read pair number, unique, per contig.

[wgsim]: https://github.com/lh3/wgsim

