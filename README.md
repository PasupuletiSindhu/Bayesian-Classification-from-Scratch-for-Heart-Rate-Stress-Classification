# Bayesian-Classification-from-Scratch-for-Heart-Rate-Stress-Classification

This repository implements fundamental Bayesian classification techniques from scratch using Python. It demonstrates how prior probabilities, class distributions, and basic statistical calculations can be used to build a working classification system without relying on high-level machine learning libraries.

## What is Classification?

Classification is a supervised learning task where the goal is to assign a category label to new observations based on a training dataset of labeled examples. Bayesian classification uses probability theory to estimate the likelihood that a given data point belongs to a particular class, and assigns the label with the highest probability.

This project focuses on **prior-based classification**, where only the prior probability of each class is used to make decisions, serving as a building block for more advanced Bayesian models.

## Contents

- `util.py` – Custom implementations of statistical functions:
  - `mean`, `stdev`, `sampleMean`, and `covariance`
- `classifiers.py` – Implements a basic Prior Classifier using prior probabilities of classes.
- `bayesian_classifier.ipynb` – Jupyter notebook that:
  - Visualizes distributions
  - Compares custom and NumPy statistical functions
  - Tests prior-based classification
- Dataset – A synthetic dataset representing heart rate values under various stress levels.

## Dataset Description

The dataset is synthetically generated to simulate heart rate values labeled under different stress categories:

- Binary Classification: `"Stressed"` vs `"Not Stressed"`
- Multiclass Classification: `"Stress"`, `"Moderate"`, and `"Not Stress"`

Each row in the dataset includes:
- A numerical heart rate value
- A class label

Class probabilities are computed from the generated data:

Binary class priors:
```
{'Not Stressed': 0.476, 'Stressed': 0.524}
```

Multiclass priors:
```
{'Stress': 0.293, 'Moderate': 0.320, 'Not Stress': 0.388}
```

## How to Run

### Requirements

```bash
pip install numpy pandas matplotlib
```

### Steps

1. Clone this repository.
2. Open `bayesian_classifier.ipynb` using Jupyter or VSCode.
3. Run the cells sequentially to:
   - Compare statistical functions from `util.py` with NumPy equivalents
   - Visualize the heart rate distributions
   - Train and test the Prior Classifier

## Highlights

- Custom implementation of core statistical functions
- Prior probability-based classification without using likelihood or posterior
- Synthetic data generation with controlled distribution parameters
- Visualization of class distributions and classification outcomes
- Comparison of binary and multiclass prior-based decisions

## License

This project is intended for educational and experimental use.
