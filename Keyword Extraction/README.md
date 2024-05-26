# Keyword Extraction for User Trust Analysis

This folder contains Python scripts and data files used to extract and analyze keywords from user feedback related to responses. The aim is to identify and categorize words that significantly reflect user trust or distrust in promoting patterns, providing valuable insights for improving thought models.

## Overview

The keyword extraction process involves:
- Pre-processing user feedback to standardize text and remove noise.
- Employing custom stopword lists to exclude uninformative words.
- Performing frequency analysis to identify the most significant terms related to user trust.
- Categorizing keywords using manual and automated methods to understand the dynamics of user trust.

## Contents

### Scripts
- `find_keywords.py`: Python script to extract keywords from the feedback data.
- `download.py`: Script to download `WordNet`. 
- `words_categories.py`: Script to categorize extracted keywords (attempts using WordNet included).

### Data Files
- `original open closed feedback.xlsx`: Original feedback data including both open and closed responses.
- `final_open_ended_feedback.xlsx`: Contains the final set of open-ended feedback from users. The `final_open_ended_feedback.xlsx` file contains refined user feedback initially gathered in the `original open closed feedback.xlsx`. This refinement process involved translating all non-English responses into English and correcting any spelling errors using Grammarly, ensuring that the dataset is consistent and suitable for further analysis in English.
- `stopwords.txt`: Custom list of stopwords tailored to ignore common but uninformative words specific to this analysis.
- `keywords.txt`: List of 463 keywords extracted from the user feedback.
- `word_categories.txt`: Categorization of keywords using WordNet (not meeting expectations).

## Methodology

The feedback text is first converted to lowercase, punctuation is removed, and the text is split into words. Using a custom list of stopwords, the text is filtered to retain only significant words. These words are then analyzed for frequency and relevance to user trust or distrust.

Despite the categorization efforts using WordNet, the tool was not fully capable of capturing the nuanced evaluative language used in the feedback. Future improvements could include more sophisticated AI-driven tools for semantic analysis to enhance categorization accuracy and depth.

## Running the Scripts

Ensure Python and necessary libraries (e.g., `pandas`, `nltk`) are installed. You can run the scripts as follows:
```bash
python find_keywords.py
python words_categories.py
