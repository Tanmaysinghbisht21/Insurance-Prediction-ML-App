import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st
#this streamlit is for web based apllication project


#Web Page code
st.title("HEALTH INSURANCE PREDICTION")
img_url  = "https://www.dreamstime.com/stock-illustration-health-insurance-concept-doodle-chart-keywords-icons-image78777274"
st.image(img_url)

# Load DATA and ML MODEL PART
#Step2:
url = "https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df = pd.read_csv(url)

#Step3 : EDA: Exploratory Data Analysis
df.drop("Customer_ID",axis = 1, inplace = True)

df['Previous_Insurance'] = df['Previous_Insurance'].map({'No':0,'Yes':1})
df['Insurance_Bought'] = df['Insurance_Bought'].map({'No':0,'Yes':1})

# Step 4: Divide dataset into features and target
X = df.iloc[:,:-1]
y = df.iloc[:,-1].values.ravel()

#Step5 Divide data into Training & testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 42

#Step 6 : Train Model
model = LogisticRegression()
model.fit(X_train,y_train)



#show data sample
st.write(df.head())
#create side bar for user input form
st.sidebar.title("Fill Customer DetailS")
st.sidebar.image(img_url)


for index , col_name in enumerate(X.columns):
 min_v = X[col_name].min()
 max_v = X[col_name].max()
   if col_name != "Previous_Insurance":
    value = st.sidebar.slider(f"Select value for {col_name}",
                              min_value = min_y,
                              max_value = max_y)
  else:
    value = st.sidebar.number_input(f"Select value for {col_name} (0:No, 1:yes): ")

all_ans.append(value)

ud = {j:all_ans[i]for i.j in enumerate(X.columns)}
user_df = pd.DataFrame(ud, index = [1])
user_df = pd.DataFrame(all_ans,  columns = X.columns)
st.write(user_df)

#=================Prediction================
if st.button("click to Predict : "):
  with st.spinner("Prediction.."):
    import time
    time.sleep(2)
final_ans = model.predict([all_ans])[0]
 if final_ans == 0:
        st.info("❌Customer will not Buy the Insurance❌")
    else:
        st.success("✅Customer will buy the Insurance✅")
                                                 
