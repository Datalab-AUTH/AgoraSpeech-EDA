### AgoraSpeech: A comprehensive dataset of political pre-election discourse - the Greek national elections case
Political discourse datasets are important for gaining political insights, analyzing communication strategies or social science phenomena. Although numerous political discourse corpora exist, comprehensive, high-quality, annotated datasets are scarce. This is largely due to the substantial manual effort, multidisciplinarity, and expertise required for the nuanced annotation of rhetorical strategies and ideological contexts. In this paper, we present **AgoraSpeech**, a meticulously curated, high-quality dataset of 171 political speeches from six parties during the Greek national elections in 2023. The dataset includes annotations (per paragraph) for six natural language processing (NLP) tasks: text classification, topic identification, sentiment analysis, named entity recognition, polarization and populism detection. A two-step annotation was employed, starting with ChatGPT-generated annotations and followed by exhaustive human-in-the-loop validation. The dataset was initially used in a case study to provide insights during the pre-election period, however, it has general applicability by serving as a rich source of information for political and social scientists, journalists, or data scientists. Also it can be used for benchmarking and fine-tuning NLP and large language models (LLMs).

## AgoraSpeech EDA
This is a repository for sharing exploratory data analysis (EDA) of the **AgoraSpeech dataset**, provided through the CSV file 'AgoraSpeech.csv'. In summary, the dataset contains information (text, metadata, and speech analysis results) about the speeches during the two pre-election periods of the Greek National elections in 2023 (21 May 2023 and 25 June 2023). Each row corresponds to a paragraph of a speech (in total 5279 rows) and each column to information about this paragraph (in total 20 columns). More information about the structure of the dataset is provided in Zenodo (https://doi.org/10.5281/zenodo.13957176). This repository includes notebooks regarding the preprocessing, analysis, and visualizations of the AgoraSpeech dataset, as follows:

1. _preprocessing.ipynb_: Applies basic preprocessing actions (e.g., continuous to categorical features conversion, factorization, etc.) to the AgoraSpeech dataset and creates a preprocessed version of it.
2. _descriptive_statistics_computation.ipynb_: Computes the descriptive statistics (e.g., total number of words, average paragraphs per speech, average sentiment score per speech, etc.) of the metadata and human annotations.
3. _human_annotations_eda.ipynb_: Analyzes and creates visualizations of the human annotations for all six NLP tasks.
4. _chatgpt_annotations_eda.ipynb_: Creates visualizations of the ChatGPT annotations in comparison to human annotations for the NLP tasks.
5. _accuracy_computation.ipynb_: Computes the most prevalent human annotation value for each NLP task and the accuracy of ChatGPT annotations based on the human annotations.

## Dataset Availability
The AgoraSpeech dataset is stored as a CSV file in Zenodo, a general-purpose open repository, and can be accessed online (https://doi.org/10.5281/zenodo.13957176).

## Acknowledgments
The dataset is created by [Data & Web Science Lab](https://datalab.csd.auth.gr/) and [iMEdD Lab](https://lab.imedd.org/en/).
