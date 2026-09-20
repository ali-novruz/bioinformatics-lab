# Evolutionary-scale prediction of atomic-level protein structure with a language model

**Authors:** Lin et al.

**Year:** 2023

**Primary source:** [https://doi.org/10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574)
**Reading status:** method, principal evidence and limitations reviewed; no full-paper reproduction claimed.

## Question and method

The paper asks how to obtain sequence representations and predicted folds. Its central method is **protein language modelling and structure prediction**. Input unit, objective function, validation dataset and comparison baseline must be read together; the tool name alone does not define an analysis.

## What the evidence supports

The reported experiments support the method in the paper's datasets and benchmark design. They do not automatically validate a new species, instrument, cohort or clinical use. Reproduction means matching versioned inputs, parameters and evaluation—not merely invoking a similarly named package.

## Main limitation to carry into this repository

training-corpus leakage, confidence and function inference require separate evaluation. Any local result must therefore report data origin, split/unit, parameter version, uncertainty and the claim boundary.

## Repository connection

See [`resources/databases/alphafold-db.md`](../../resources/databases/alphafold-db.md). A useful exercise is to identify which paper assumptions are satisfied there, which are only approximated, and one control that would falsify the local interpretation.

## Next experiment

Freeze one small input and metric, run the baseline and one controlled variation, preserve all outputs, and explain disagreement before expanding the dataset. Negative and unstable results belong in `research/findings/` as much as positive results.
