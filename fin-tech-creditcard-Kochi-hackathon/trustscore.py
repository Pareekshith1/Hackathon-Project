from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np
np.random.seed(42)

app = Flask(__name__)

df = pd.read_csv('trustScore.csv')

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['HourOfDay'] = df['Timestamp'].dt.hour
df['IsBusinessHours'] = (df['HourOfDay'] >= 9) & (df['HourOfDay'] <= 17)

df['IsSuspiciousAmount'] = df['Amount'] > 1000  # Adjust the threshold as needed

# Dummy location data for demonstration purposes
df['IsSuspiciousLocation'] = df['Location'].apply(lambda x: x.lower() == 'suspicious_location')

# Select features for training
features = ['Amount', 'IsBusinessHours', 'IsSuspiciousAmount', 'IsSuspiciousLocation']  # Add other features as needed

# Target variable
target = 'Isfraud'

# Split the data into training and testing sets
X = df[features]
y = df[target]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestClassifier()  # Use a random classifier for demonstration
model.fit(X_scaled, y)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mobile_number = request.form['mobile_number']
        trust_score, alert_flag = get_trust_score(mobile_number)
        return render_template('result.html', trust_score=trust_score, mobile_number=mobile_number,
                               alert_flag=alert_flag)
    return render_template('trustscore.html')



def get_trust_score(mobile_number):
    user_search_column = 'Contact'
    user_data = df[df[user_search_column] == int(mobile_number)]

    if user_data.empty:
        print(f"No data found for Contact {mobile_number}")
        return None, False

    user_features = user_data[features]
    user_features_scaled = scaler.transform(user_features)
    trust_score = model.predict_proba(user_features_scaled)[:, 1][0]

    # Multiply trust_score by 10
    trust_score *= 10

    # Format trust_score to have two decimal places
    trust_score = '{:.4f}'.format(trust_score)

    # Convert to float to remove trailing zeros
    trust_score = float(trust_score)

    # Extract integer part of the trust score
    integer_part = int(trust_score)

    # Set alert flag if the integer part is less than 10
    alert_flag = integer_part < 5

    return trust_score, alert_flag


if __name__ == '__main__':
    app.run(debug=True)
