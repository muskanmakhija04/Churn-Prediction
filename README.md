## Tele Customer Churn Prediction

### Project Overview

This project aims to predict customer churn for a telecommunications company using machine learning. It involves building a Flask-based web service that takes customer information as input and returns a prediction about whether the customer is likely to churn, along with the confidence level of the prediction.

### Features

- **Input**: Customer details via a POST request
- **Output**: Churn prediction (Churn/Not Churn) with confidence percentage
- **Model**: Pre-trained machine learning model
- **Deployment**: Flask web application

### Files

- `app.py`: Main application file containing the Flask web service.
- `trained_model_new2.sav`: Pre-trained machine learning model.
- `Telco_customer_churn (copy).xlsx`: Original dataset for feature extraction and preprocessing.

### Dependencies

- Python 3.10
- Flask
- Pandas
- Pickle
- openpyxl (for reading Excel files)

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/tele-customer-churn-prediction.git
   cd tele-customer-churn-prediction
   ```

2. **Create a virtual environment and activate it**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**
   ```sh
   pip install -r requirements.txt
   ```

4. **Place the model and dataset in the specified directory**
   Ensure that `trained_model_new2.sav` and `Telco_customer_churn (copy).xlsx` are located in the appropriate paths specified in `app.py`.

### Running the Application

To run the Flask application, execute the following command:
```sh
python app.py
```
The application will start in debug mode and listen on `http://127.0.0.1:5000/`.

### API Endpoint

**URL**: `/`
**Method**: `POST`

**Input Parameters**:
- `Senior_Citizen (0 or 1)`
- `Monthly_Charges (float)`
- `Total_Charges (float)`
- `Gender (Male or Female)`
- `Partner (Yes or No)`
- `Dependents (Yes or No)`
- `Phone_Service (Yes or No)`
- `Multiple_Lines (No phone service, No, or Yes)`
- `Internet_Service (DSL, Fiber optic, or No)`
- `Online_Security (No internet service, No, or Yes)`
- `Online_Backup (No internet service, No, or Yes)`
- `Device_Protection (No internet service, No, or Yes)`
- `Tech_Support (No internet service, No, or Yes)`
- `Streaming_TV (No internet service, No, or Yes)`
- `Streaming_Movies (No internet service, No, or Yes)`
- `Contract (Month-to-month, One year, or Two year)`
- `Paperless_Billing (Yes or No)`
- `Payment_Method (Bank transfer (automatic), Credit card (automatic), Electronic check, or Mailed check)`
- `Tenure_Months (integer, representing months)`

**Example Request**:
```json
{
    "Senior_Citizen": "0",
    "Monthly_Charges": "50.0",
    "Total_Charges": "500.0",
    "Gender": "Male",
    "Partner": "Yes",
    "Dependents": "No",
    "Phone_Service": "Yes",
    "Multiple_Lines": "No phone service",
    "Internet_Service": "Fiber optic",
    "Online_Security": "No",
    "Online_Backup": "Yes",
    "Device_Protection": "No internet service",
    "Tech_Support": "No",
    "Streaming_TV": "No",
    "Streaming_Movies": "No",
    "Contract": "Month-to-month",
    "Paperless_Billing": "Yes",
    "Payment_Method": "Electronic check",
    "Tenure_Months": "24"
}
```

**Example Response**:
```json
{
    "Churn Prediction": "Not Churn",
    "Confidence": 78.56
}
```

### Testing with Postman

You can use Postman or a similar tool to test the API. Use the example request above and POST it to `http://127.0.0.1:5000/`.

### Acknowledgments

- Data Source: [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)
- Model Training and Preprocessing: [Muskan Makhija]

---

Feel free to update the paths and descriptions according to your specific project setup.
