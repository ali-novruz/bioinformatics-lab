# Deep generative modeling for single-cell transcriptomics

**Authors:** Lopez et al.

**Year:** 2018

**Primary source:** [https://doi.org/10.1038/s41592-018-0229-2](https://doi.org/10.1038/s41592-018-0229-2)
**Reading status:** method, principal evidence and limitations reviewed; no full-paper reproduction claimed.

## Question and method

The paper asks how to obtain probabilistic latent representation and uncertainty. Its central method is **hierarchical variational autoencoder for counts**. Input unit, objective function, validation dataset and comparison baseline must be read together; the tool name alone does not define an analysis.

## What the evidence supports

The reported experiments support the method in the paper's datasets and benchmark design. They do not automatically validate a new species, instrument, cohort or clinical use. Reproduction means matching versioned inputs, parameters and evaluation—not merely invoking a similarly named package.

## Main limitation to carry into this repository

model fit and latent separation do not establish biological causality. Any local result must therefore report data origin, split/unit, parameter version, uncertainty and the claim boundary.

## Repository connection

See [`docs/data-formats/h5ad-10x.md`](../../docs/data-formats/h5ad-10x.md). A useful exercise is to identify which paper assumptions are satisfied there, which are only approximated, and one control that would falsify the local interpretation.

## Next experiment

Freeze one small input and metric, run the baseline and one controlled variation, preserve all outputs, and explain disagreement before expanding the dataset. Negative and unstable results belong in `research/findings/` as much as positive results.
