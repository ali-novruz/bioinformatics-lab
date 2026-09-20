# Initial sequencing and analysis of the human genome

**Authors:** International Human Genome Sequencing Consortium

**Year:** 2001

**Primary source:** [https://doi.org/10.1038/35057062](https://doi.org/10.1038/35057062)
**Reading status:** method, principal evidence and limitations reviewed; no full-paper reproduction claimed.

## Question and method

The paper asks how to obtain a public draft human reference. Its central method is **hierarchical clone-based genome sequencing and annotation**. Input unit, objective function, validation dataset and comparison baseline must be read together; the tool name alone does not define an analysis.

## What the evidence supports

The reported experiments support the method in the paper's datasets and benchmark design. They do not automatically validate a new species, instrument, cohort or clinical use. Reproduction means matching versioned inputs, parameters and evaluation—not merely invoking a similarly named package.

## Main limitation to carry into this repository

draft gaps, assembly errors and limited representation shaped downstream analyses. Any local result must therefore report data origin, split/unit, parameter version, uncertainty and the claim boundary.

## Repository connection

See [`docs/molecular-biology/README.md`](../../docs/molecular-biology/README.md). A useful exercise is to identify which paper assumptions are satisfied there, which are only approximated, and one control that would falsify the local interpretation.

## Next experiment

Freeze one small input and metric, run the baseline and one controlled variation, preserve all outputs, and explain disagreement before expanding the dataset. Negative and unstable results belong in `research/findings/` as much as positive results.
