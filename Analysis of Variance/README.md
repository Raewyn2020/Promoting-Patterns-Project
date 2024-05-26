# Analysis of Variance for User Trust Scores

This directory contains the Python scripts and datasets used to perform Analysis of Variance (ANOVA) and T-tests for assessing the significance of differences in user trust scores across various thought models in different tasks.

## Overview

The statistical analyses aim to determine whether the differences in user trust scores observed across different prompting methods are statistically significant and not due to random chance. This folder contains scripts for conducting ANOVA tests across multiple groups and T-tests for pairwise comparisons.

## Contents

### Scripts
- `ANOVA.py`: Script to perform ANOVA for each task. It compares the mean scores across four different responses in each task to determine if there are significant differences.
- `t_test.py`: Script to conduct pairwise T-tests following ANOVA to identify specific pairs of thought models that differ significantly in their trust scores.

### Data Files
- `q1.xlsx` to `q5.xlsx`: These Excel files contain the user trust scores for tasks 1 through 5. Each file corresponds to a different task assessed in the study.

## Usage

To run the ANOVA or T-tests, ensure Python is installed along with necessary libraries like `pandas` and `scipy`. Execute the scripts in a Python environment to view the analysis results. Make sure the data files are in the same directory as the scripts or modify the script paths as needed.

## How to Run the Scripts

1. Open your command line interface (CLI).
2. Navigate to the directory containing the scripts.
3. Run the following command to perform ANOVA:
   ```bash
   python3 ANOVA.py
4. Run the following command to perform T-tests:
   ```bash
   python3 t_test.py
   
