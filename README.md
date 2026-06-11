
**Spam Detection using Machine Learning**

A Machine Learning-based Spam Detection System that classifies text messages as Spam or Not Spam (Ham) using Natural Language Processing (NLP) techniques and machine learning algorithms.
The application provides a simple and interactive web interface where users can enter a message and instantly receive a prediction.

**Project Overview**

Spam Detection is one of the most common applications of Machine Learning and Natural Language Processing.
This project analyzes the content of a message and predicts whether it belongs to the Spam category or the Not Spam (Ham) category.
The system uses text preprocessing techniques and a trained machine learning model to perform classification.

**This project demonstrates concepts related to:**
Machine Learning
Natural Language Processing (NLP)
Text Classification
Data Preprocessing
Model Deployment
Streamlit Web Applications

**Features**

Detects Spam messages
Detects Not Spam (Ham) messages
Real-time prediction
Interactive Streamlit web interface
NLP-based text preprocessing
Lightweight and easy-to-use system
Fast prediction results

**Technologies Used**

Programming Language
Python
Libraries
Streamlit
Pandas
NumPy
NLTK
Scikit-learn
Pickle

**How the System Works**

Step 1 — User Input

The user enters a text message.
Example:
Plain text
Congratulations! You have won a free iPhone.

Step 2 — Text Preprocessing

The message is processed using NLP techniques:
Convert to lowercase
Remove special characters
Tokenization
Stopword removal
Stemming

Step 3 — Feature Extraction

The processed text is converted into numerical features using:
TF-IDF Vectorization

Step 4 — Prediction

The trained machine learning model analyzes the message.

Step 5 — Output
The system displays:
Plain text
Spam
or
Plain text
Not Spam
**Dataset Information**
The project uses an SMS Spam Collection Dataset containing messages labeled as:
Spam
Ham (Not Spam)
The dataset is used for training and evaluating the machine learning model.
**Project Structure**
Plain text
Spam_Detection/
│
├── dataset/
│   └── spam.csv
│
├── models/
│   └── spam_model.pkl
│
├── screenshots/
│   ├── output1.png
│   ├── output2.png
│   └── output3.png
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
**Installation**
Clone Repository
Bash
git clone https://github.com/yourusername/spam-detection.git
Move to Project Folder
Bash
cd spam-detection
Install Requirements
Bash
pip install -r requirements.txt
**Requirements**
Plain text
streamlit
pandas
numpy
nltk
scikit-learn
**Run the Application**
Bash
streamlit run app.py
After running the command, open:
Plain text
http://localhost:8501
**Output Screenshots**
### Output 1

![Output 1](./screenshots/Screenshot%202026-06-11%20091451.png)

*Description:* Home page of the Spam Detection system where users can enter a message for prediction.

---

### Output 2

![Output 2](./screenshots/Screenshot%202026-06-11%20091513.png)

*Description:* Example showing a message classified as Spam.

---

### Output 3

![Output 3](./screenshots/Screenshot%202026-06-11%20091539.png)

*Description:* Example showing a message classified as Not Spam (Ham).


**Advantages**
Easy to use
Fast prediction results
Beginner-friendly Machine Learning project
Uses NLP concepts
Lightweight web application
Real-time message classification
**Limitations**
Accuracy depends on dataset quality
May misclassify unseen message patterns
Limited to text-based spam detection
Performance depends on training data
Future Improvements
Deep Learning-based classification
Email spam detection
Multi-language support
Mobile application integration
Cloud deployment
Improved prediction accuracy
Learning Outcomes
**This project helped in understanding:**
Natural Language Processing (NLP)
Text preprocessing techniques
Feature extraction using TF-IDF
Machine Learning classification
Model training and evaluation
Streamlit web application development
Model deployment concepts
**Use Cases**
SMS Spam Detection
Email Filtering Systems
Customer Support Systems
Educational Projects
NLP Practice Projects
Machine Learning Demonstrations
**Developed By**
Nayana N S
Machine Learning Project – Spam Detection using NLP and Machine Learning :::
