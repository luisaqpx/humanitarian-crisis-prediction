**Humanitarian Crisis Prediction Using Adaptive AI**
An AI system designed to predict humanitarian crisis severity using machine learning and a contextual bandit that learns from feedback

**Project Overview**
Humanitarian crises caused by armed conflict, natural disasters, and displacement can change significantly over time. Predicting changes in crisi severity may help humanitarian organizations identify worsening conditions and respond more effectively .
5 categories: 
-Very Low
-Low
-Medium
-High
-Very High
Instead of relying on a single prediction model, our system will use a contextual bandit to select between three machine learning models and learn from previous predictions 

**Team members**
-Marim Abbas 
Luisa Quintero

**Data Sources**
Index for Risk Management (INFORM) Severity Index-avaialbe through the Humanitarian Data Exchange (HDX)
Armed Conflict Location & Event Data Project (ACLED): Confluict events and related data
World Bank Open Data: Socioeconomic indicators (GDP per capita, Poverty rate, refugee pop, etc.)

**Machine Learning Models**
1. Decision Tree
2. Random Forest
3. Multilayer Preceptron (MLP)

**Contextual Bandit**
a contextual bandit using an epsilon-greedy strategy will select which prediction model to use based on the available humanitarian crisis indicators. Then, the system will compare the prediction with the observed outcome and assign a reward. The bandit will use this feedback to update its model-selection strategy.

**Reward System**
assigns higher rewards to predictions that are closer to the actual severity level
Exact-1
One level off-0.75
Two levels off-0.5
Three levels off-0.25
Four levels off-0

**Model Retraining**
We will compare the bandit's perforrmance with and without retraining the three models while also comparing it against nonadaptive approaches under the same conditions 

**Evaluation**
We will evaluate the system using:
-Prediction accuracy
-Macro F1-score
-Average reward 
-Learning curves 

We will also compare the contextual bandit against
1. Best individual model: always using the best-performing model selected using validation data
2. Ensemble voting: All three models predict, and the majority prediction wins 

To prevent future information from influencing earlier predictions, we will use chronologically ordered data 

-Python
-Scikit-learn
-Pandas
-NumPy

Current Planned Steps:
-Collecting and preprocessing the dataset
-training the three prediction models
-implementing the contextual bandit and reward system 
