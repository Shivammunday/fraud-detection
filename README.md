## fraud-detection
It is a machine learning project designed to detect fraudulent financial transactions from a large real-world dataset of **6.3 million records**. The model aims to improve existing fraud detection systems by using better preprocessing and strong classification techniques. It also highlights the weaknesses in traditional rule-based systems.
## 📁 Files

- `app.py`: Main Streamlit app (your `.ipynb` code saved as `.py`)
- `fraud_detection.pkl`: Pre-trained machine learning model
- `report_csv`: Dataset
🧾 **Dataset Overview**
The dataset comprises 6.3 million mobile money transaction records. Some transactions were incorrectly labeled by existing detection algorithms, providing an opportunity to train a better fraud prediction model.
##🧠 Objective
--Predict fraudulent transactions more accurately than existing methods.

--Understand patterns behind frauds missed by traditional models.

--Evaluate performance using metrics like precision, recall, f1-score, and confusion matrix.

## 🧪 Model Performance (Logistic Regression)

# 📈 Classification Report

| Label       | Precision | Recall | F1-Score | Support   |
|-------------|-----------|--------|----------|-----------|
| **0 (Legit)** | **1.00**     | **0.95**   | **0.97**     | **1,906,322** |
| **1 (Fraud)** | **0.02**     | **0.94**   | **0.04**     | **2,464**     |

**Accuracy:** 95%  
**Macro Average F1:** 0.51  
**Weighted F1:** 0.97  

# 🔍 Confusion Matrix
[[1803358, 102964],
[ 147, 2317]]

##Tech Stack
 *Language*: Python 3.8+

 *ML*: scikit-learn, pandas, numpy

 *App* (Optional): streamlit, joblib

 ## 🧠 Model Info

- Trained using logistic regression / random forest (adjust based on your model)
- Binary classification: 1 = Fraud, 0 = Not Fraud

