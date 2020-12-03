#
# View the GFF in context of a VCF file.
#
# Run the script in a test directory

set -uex

# Clean up files from previous run.
rm -f  eval_*

# Get reference from command line
REF=$1

# Set up the simulation parameters
N=10000
GFF=eval_mut.gff
READ1=eval_read_1.fq
READ2=eval_read_2.fq
BAM=eval_aln.bam
VCF=eval_snp.vcf

# Simulate the reads.
pywgsim -e 0 -N $N $REF $READ1 $READ2 > $GFF

# Index the genome.
bwa index  $REF

# Create the alignments.
bwa mem $REF $READ1 $READ2 | samtools sort > $BAM

# Index the BAM file.
samtools index $BAM

# Call SNPs with bcftools to compare with predicted mutations.
bcftools mpileup -Ou -f $REF $BAM | bcftools call -mv -Ov -o $VCF

