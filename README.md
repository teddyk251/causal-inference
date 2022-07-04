# Causal Inference
**Table of Contents**

  - [Overview](#overview)
  - [Project Structure](#project-structure)
    - [data:](#data)
    - [notebooks:](#notebooks)
        - [logs:](#logs)
        - [reports:](#reports)
    - [scripts](#scripts)
    - [tests:](#tests)
    
    - [root folder](#root-folder)
  - [Installation guide](#installation-guide)

## Overview
- A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:
    - “What will happen if I halve the price of my product?”
    - “Which clients will pay their debts only if I call them?”

- The causal graph is a central object in the framework mentioned above, but it
is often unknown, subject to personal knowledge and bias, or loosely
connected to the available data. The main objective of this task is to
highlight the importance of the matter in a concrete way.

- In this project we applied a casual graph model on a breast cancer dataset
using a library called CausalNex in order to learn about the cause and effect structure behind
the diagnosis of breast cancer.

## Project Structure
The repository has a number of files including python scripts, jupyter notebooks, pdfs and text files. Here is their structure with a brief explanation.

## Data
- We are using the Breast Cancer Wisconsin (Diagnostic) Data Set extracted from [kaggle](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
## notebooks
- [EDA.ipynb](https://github.com/teddyk251/causal-inference/blob/main/notebooks/EDA.ipynb): a jupyter notebook for exploratory data analysis
- [causal_graph.ipynb](https://github.com/teddyk251/causal-inference/blob/main/notebooks/causal_graph.ipynb): a jupyter notebook for exploratory data analysis
## scripts
- [dataclearner.py](https://github.com/teddyk251/causal-inference/blob/main/scripts/datacleaner.py)
    - a python script for data cleanin
- [log.py](https://github.com/teddyk251/causal-inference/blob/main/scripts/log.py)

    - a python script for handling logs
- [plotter.py](https://github.com/teddyk251/causal-inference/blob/main/scripts/plotter.py)
    - a python script for creating plots
- [utils.py](https://github.com/teddyk251/causal-inference/blob/main/scripts/utils.py)
    - a python script for loading and writing files

## tests:
- the folder containing unit tests for components in the scripts

## logs:
- the folder containing log files (if it doesn't exist it will be created once logging starts)

## reports:
- the folder contains cml reports


## Installation Guide:
 ```
git clone https://github.com/teddyk251/causal-inference.git 
cd causal-inference/
pip install -r requirements.txt
    
```



