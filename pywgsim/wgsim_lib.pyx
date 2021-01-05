import os, sys


cdef extern from "wgsim_mod.h":
    int wgsim_wrap(const char *r1, const char *r2, const char *ref, float err_rate, float mut_rate, float indel_frac,
                   float indel_extend, float max_n, int is_hap, long N, int dist, int std_dev, int size_l, int size_r,
                   int is_fixed, int seed)

def fraction(value):
    value = float(value)
    if value > 1:
        raise Exception("invalid fraction %s" % value)
    return value

def error(msg):
    sys.stderr.write("*** %s\n" % msg)
    sys.stderr.write("*** exiting\n")
    sys.exit(1)

def core(ref, r1="read1.fq", r2="read2.fq", err_rate=0.02, mut_rate=0.001, indel_frac=0.15, indel_ext=0.25, max_n=0.05,
         is_hap=0, N=100000, dist=500, stdev=50, size_l=100, size_r=100, is_fixed=0, seed=0):

    # Validating input parameters
    try:
        if not os.path.isfile(ref):
            error("genome not found: %s" % ref)

        # Verify that read names are writeable files.
        for name in [r1, r2]:
            fp = open(name, 'wt')
            fp.close()

        err_rate = fraction(err_rate)
        mut_rate = fraction(mut_rate)
        indel_frac = fraction(indel_frac)
        indel_ext = fraction(indel_ext)
        max_n = fraction(max_n)

    except Exception as exc:
        error(str(exc))

    # Convert to
    r1 = r1.encode()
    r2 = r2.encode()
    ref = ref.encode()

    wgsim_wrap(r1, r2, ref, err_rate, mut_rate, indel_frac, indel_ext, max_n, is_hap, N, dist, stdev, size_l, size_r,
               is_fixed, seed)
