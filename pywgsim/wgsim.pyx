
cdef extern from "wgsim_mod.h":
    int wgsim_wrap(const char *r1, const char *r2, const char *ref, float err_rate, float mut_rate, float indel_frac, float indel_extend, float max_n, int is_hap, long N, int dist, int std_dev, int size_l, int size_r, int is_fixed, int seed)

def core(r1, r2, ref, err_rate=0.02, mut_rate=0.001, indel_frac=0.15, indel_ext=0.25, max_n=0.05, is_hap=0, N=100000,  dist=500, stdev=50, size_l=100, size_r=100, is_fixed=0, seed=0):

    # Convert to
    r1 = r1.encode()
    r2 = r2.encode()
    ref = ref.encode()

    wgsim_wrap(r1, r2, ref, err_rate, mut_rate, indel_frac, indel_ext, max_n, is_hap, N,  dist, stdev, size_l, size_r, is_fixed, seed)
