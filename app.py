import pandas as pd
from flask import Flask, request, jsonify
import pickle

app = Flask("__name__")

# Load the trained model
model = pickle.load(open("/home/mayur/Downloads/My projects/POCs/Churn prediction/model/trained_model_new2.sav", "rb"))

# Load the original dataset for initial feature extraction and preprocessing
df_1_path = "/home/mayur/Downloads/My projects/POCs/Churn prediction/Telco_customer_churn (copy).xlsx"
df_1 = pd.read_excel(df_1_path)

@app.route("/", methods=['POST'])
def predict():
    # Extract input values from form data
    inputQuery1 = request.form['Senior_Citizen (0 or 1)']
    inputQuery2 = request.form['Monthly_Charges (float)']
    inputQuery3 = request.form['Total_Charges (float)']
    inputQuery4 = request.form['Gender (Male or Female)']
    inputQuery5 = request.form['Partner (Yes or No)']
    inputQuery6 = request.form['Dependents (Yes or No)']
    inputQuery7 = request.form['Phone_Service (Yes or No)']
    inputQuery8 = request.form['Multiple_Lines (No phone service, No, or Yes)']
    inputQuery9 = request.form['Internet_Service (DSL, Fiber optic, or No)']
    inputQuery10 = request.form['Online_Security (No internet service, No, or Yes)']
    inputQuery11 = request.form['Online_Backup (No internet service, No, or Yes)']
    inputQuery12 = request.form['Device_Protection (No internet service, No, or Yes)']
    inputQuery13 = request.form['Tech_Support (No internet service, No, or Yes)']
    inputQuery14 = request.form['Streaming_TV (No internet service, No, or Yes)']
    inputQuery15 = request.form['Streaming_Movies (No internet service, No, or Yes)']
    inputQuery16 = request.form['Contract (Month-to-month, One year, or Two year)']
    inputQuery17 = request.form['Paperless_Billing (Yes or No)']
    inputQuery18 = request.form['Payment_Method (Bank transfer (automatic), Credit card (automatic), Electronic check, or Mailed check)']
    inputQuery19 = request.form['Tenure_Months (integer, representing months)']

    # Create a new DataFrame with the input data
    data = {
        'Senior_Citizen': [inputQuery1],
        'Monthly_Charges': [float(inputQuery2)],
        'Total_Charges': [float(inputQuery3)],
        'Gender': [inputQuery4],
        'Partner': [inputQuery5],
        'Dependents': [inputQuery6],
        'Phone_Service': [inputQuery7],
        'Multiple_Lines': [inputQuery8],
        'Internet_Service': [inputQuery9],
        'Online_Security': [inputQuery10],
        'Online_Backup': [inputQuery11],
        'Device_Protection': [inputQuery12],
        'Tech_Support': [inputQuery13],
        'Streaming_TV': [inputQuery14],
        'Streaming_Movies': [inputQuery15],
        'Contract': [inputQuery16],
        'Paperless_Billing': [inputQuery17],
        'Payment_Method': [inputQuery18],
        'Tenure_Months': [int(inputQuery19)]
    }

    new_df = pd.DataFrame(data)

    # Combine with original dataset for feature extraction
    df_combined = pd.concat([df_1, new_df], ignore_index=True)

    # Bin tenure into groups
    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
    df_combined['tenure_group'] = pd.cut(df_combined['Tenure_Months'], bins=range(1, 80, 12), right=False, labels=labels)

    # Drop unnecessary columns
    df_combined.drop(columns=['Tenure_Months'], inplace=True)

    # Get dummies for categorical variables
    cat_cols = ['Gender', 'Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 'Multiple_Lines',
                'Internet_Service', 'Online_Security', 'Online_Backup', 'Device_Protection',
                'Tech_Support', 'Streaming_TV', 'Streaming_Movies', 'Contract', 'Paperless_Billing',
                'Payment_Method', 'tenure_group']
    
    # Ensure consistent encoding of categorical variables
    df_dummies = pd.get_dummies(df_combined[cat_cols], drop_first=True)

    
    feature_names = model.get_booster().feature_names
    df_dummies = df_dummies.reindex(columns=feature_names, fill_value=0)

    # Predict using the model
    X_pred = df_dummies.tail(1)  
    prediction = model.predict(X_pred)
    probability = model.predict_proba(X_pred)[:, 1] * 100

    # Interpret prediction
    if prediction == 1:
        churn_status = "Churn"
    else:
        churn_status = "Not Churn"

    response = {
        "Churn Prediction": churn_status,
        "Confidence": round(float(probability), 2)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)




# example to run on Postman
# {
#     "query1": "0",                  // Senior_Citizen (0 or 1)
#     "query2": "50.0",               // Monthly_Charges (float)
#     "query3": "500.0",              // Total_Charges (float)
#     "query4": "Male",               // Gender (Male or Female)
#     "query5": "Yes",                // Partner (Yes or No)
#     "query6": "No",                 // Dependents (Yes or No)
#     "query7": "Yes",                // Phone_Service (Yes or No)
#     "query8": "No phone service",   // Multiple_Lines (No phone service, No, or Yes)
#     "query9": "Fiber optic",        // Internet_Service (DSL, Fiber optic, or No)
#     "query10": "No",                // Online_Security (No internet service, No, or Yes)
#     "query11": "Yes",               // Online_Backup (No internet service, No, or Yes)
#     "query12": "No internet service", // Device_Protection (No internet service, No, or Yes)
#     "query13": "No",                // Tech_Support (No internet service, No, or Yes)
#     "query14": "No",                // Streaming_TV (No internet service, No, or Yes)
#     "query15": "No",                // Streaming_Movies (No internet service, No, or Yes)
#     "query16": "Month-to-month",    // Contract (Month-to-month, One year, or Two year)
#     "query17": "Yes",               // Paperless_Billing (Yes or No)
#     "query18": "Electronic check",  // Payment_Method (Bank transfer (automatic), Credit card (automatic), Electronic check, or Mailed check)
#     "query19": "24"                 // Tenure_Months (integer, representing months)
# }


