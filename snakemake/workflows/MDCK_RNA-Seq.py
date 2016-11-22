_author__ = "Sebastian Kurscheid (sebastian.kurscheid@anu.edu.au)"
__license__ = "MIT"
__date__ = "2015-04-22"

from snakemake.exceptions import MissingInputException
import os

rule:
    version: 0.3

localrules:
    all, run_kallisto, run_STAR, run_htseq, run_cutadapt

home = os.environ['HOME']

wrapper_dir = home + "/Development/snakemake-wrappers/bio"

include_prefix= home + "/Development/JCSMR-Tremethick-Lab/H2AZ_EMT/snakemake/rules/"

include:
     include_prefix + "perform_fastqc.py"
include:
    include_prefix + "perform_cutadapt.py"
include:
    include_prefix + "run_kallisto.py"
include:
    include_prefix + "run_STAR.py"

rule run_kallisto:
    input:
        expand("{assayID}/{runID}/{outdir}/{reference_version}/kallisto/{unit}",
               assayID = "RNA-Seq",
               runID = ["NB501086_0067_RDomaschenz_JCSMR_RNASeq", "NB501086_0082_RDomaschenz_JCSMR_mRNAseq"],
               outdir = config["processed_dir"],
               reference_version = config["references"]["version"],
               unit = config["RNA-Seq"])

rule run_STAR:
    input:
        expand("{assayID}/{runID}/{outdir}/{reference_version}/STAR/full/{unit}.aligned.bam",
               assayID = "RNA-Seq",
               runID = ["NB501086_0067_RDomaschenz_JCSMR_RNASeq", "NB501086_0082_RDomaschenz_JCSMR_mRNAseq"],
               outdir = config["processed_dir"],
               reference_version = config["references"]["version"],
               unit = config["RNA-Seq"])

rule run_STAR_untrimmed:
    input:
        expand("{assayID}/{runID}/{outdir}/{reference_version}/STAR/full/untrimmed/{unit}.aligned.bam",
               assayID = "RNA-Seq",
               runID = ["NB501086_0067_RDomaschenz_JCSMR_RNASeq", "NB501086_0082_RDomaschenz_JCSMR_mRNAseq"],
               outdir = config["processed_dir"],
               reference_version = config["references"]["version"],
               unit = config["RNA-Seq"])

rule run_htseq:
    input:
        expand("{assayID}/NB501086_0067_RDomaschenz_JCSMR_RNASeq/{outdir}/{reference_version}/HTSeq/count/{unit}.txt",
               assayID = "RNA-Seq",
               outdir = config["processed_dir"],
               reference_version = config["references"]["version"],
               unit = config["RNA-Seq"])

rule run_cutadapt:
    input:
        expand("{assayID}/NB501086_0067_RDomaschenz_JCSMR_RNASeq/{outdir}/{trim_data}/{unit}_{suffix}.QT.CA.fastq.gz",
               assayID = "RNA-Seq",
               outdir = config["processed_dir"],
               unit = config["RNA-Seq"],
               trim_data = config["trim_dir"],
               suffix = ["R1_001", "R2_001"]),

rule all:
    input:
        expand("{assayID}/{runID}/{processed_dir}/{reports_dir}/{sample}",
               assayID = "RNA-Seq",
               runID = ["NB501086_0067_RDomaschenz_JCSMR_RNASeq", "NB501086_0082_RDomaschenz_JCSMR_mRNAseq"],
               outdir = config["processed_dir"],
               reports_dir = config["reports_dir"],
               sample = config["samples"]["RNA-Seq"]["NB501086_0082_RDomaschenz_JCSMR_mRNAseq"]
        ),
        expand("{assayID}/{runID}/{outdir}/{reference_version}/kallisto/{unit}",
               assayID = "RNA-Seq",
               runID = ["NB501086_0067_RDomaschenz_JCSMR_RNASeq", "NB501086_0082_RDomaschenz_JCSMR_mRNAseq"],
               outdir = config["processed_dir"],
               reference_version = config["references"]["version"],
               unit = config["RNA-Seq"]),
        expand("{assayID}/{runID}/{outdir}/{reference_version}/STAR/full/{unit}.aligned.bam",
               assayID = "RNA-Seq",
               runID = ["NB501086_0067_RDomaschenz_JCSMR_RNASeq", "NB501086_0082_RDomaschenz_JCSMR_mRNAseq"],
               outdir = config["processed_dir"],
               reference_version = config["references"]["version"],
               unit = config["RNA-Seq"]),
        expand("{assayID}/{runID}/{outdir}/{reference_version}/HTSeq/count/{unit}.txt",
               assayID = "RNA-Seq",
               runID = ["NB501086_0067_RDomaschenz_JCSMR_RNASeq", "NB501086_0082_RDomaschenz_JCSMR_mRNAseq"],
               outdir = config["processed_dir"],
               reference_version = config["references"]["version"],
               unit = config["RNA-Seq"])
