from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import subprocess

app = Flask(__name__)

# Code for the RandomForestClassifier and related functions
model_fraud = RandomForestClassifier()
df_fraud = pd.read_csv('fraud_dataset_example.csv')
df_fraud['orig_balance_change'] = df_fraud['newbalanceOrig'] - df_fraud['oldbalanceOrg']
df_fraud['dest_balance_change'] = df_fraud['newbalanceDest'] - df_fraud['oldbalanceDest']
features_fraud = ['amount', 'orig_balance_change', 'dest_balance_change']
X_fraud = df_fraud[features_fraud]
y_fraud = df_fraud['isFraud']
X_train_fraud, X_test_fraud, y_train_fraud, y_test_fraud = train_test_split(X_fraud, y_fraud, test_size=0.2, random_state=42)
model_fraud.fit(X_train_fraud, y_train_fraud)

# Dummy users for double verification
dummy_users = [
    {'name': 'User1', 'mobile': '9876543210', 'aadhar': '123456789012'},
    {'name': 'User2', 'mobile': '9876543211', 'aadhar': '234567890123'},
    {'name': 'User3', 'mobile': '9876543212', 'aadhar': '234567890123'}
]

# Code for the trust score application
df_trust = pd.read_csv('trustScore.csv')
df_trust['Timestamp'] = pd.to_datetime(df_trust['Timestamp'])
df_trust['HourOfDay'] = df_trust['Timestamp'].dt.hour
df_trust['IsBusinessHours'] = (df_trust['HourOfDay'] >= 9) & (df_trust['HourOfDay'] <= 17)
df_trust['IsSuspiciousAmount'] = df_trust['Amount'] > 1000
df_trust['IsSuspiciousLocation'] = df_trust['Location'].apply(lambda x: x.lower() == 'suspicious_location')
features_trust = ['Amount', 'IsBusinessHours', 'IsSuspiciousAmount', 'IsSuspiciousLocation']
target_trust = 'Isfraud'
X_trust = df_trust[features_trust]
y_trust = df_trust[target_trust]

scaler_trust = StandardScaler()
X_scaled_trust = scaler_trust.fit_transform(X_trust)

model_trust = RandomForestClassifier()  # Use a random classifier for demonstration
model_trust.fit(X_scaled_trust, y_trust)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/registration')
def registration():
    return render_template('registrationindex.html')


@app.route('/complaintform')
def complaintform():
    return render_template('complaintform.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/admin', methods=['POST'])
def admin():
    return render_template('admin.html')


@app.route('/login_user', methods=['POST'])
def login_inside():
    return render_template('afterlogin.html')


@app.route('/user_info')
def user_info():
    return render_template('user_info.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/activity')
def activity():
    subprocess.run(['python', 'activity.py'])
    return render_template('activity.html')


@app.route('/display_suspicious')
def display_suspicious():
    predictions_fraud = model_fraud.predict(X_test_fraud)
    suspicious_transactions = df_fraud.loc[X_test_fraud.index[predictions_fraud == 1], ['nameDest', 'amount', 'type']]
    return render_template('suspicioustransaction.html', transactions=suspicious_transactions.to_html(index=False))


@app.route('/double_verification', methods=['GET', 'POST'])
def double_verification():
    if request.method == 'GET':
        return render_template('double_verification_index.html')

    elif request.method == 'POST':
        verification_number = request.form.get('verification_number')
        receiver_number = request.form.get('receiver_number')

        verification_aadhar = next((user['aadhar'] for user in dummy_users if user['mobile'] == verification_number), None)
        receiver_aadhar = next((user['aadhar'] for user in dummy_users if user['mobile'] == receiver_number), None)

        result = 'Matching' if verification_aadhar == receiver_aadhar else 'Mismatch'

        return jsonify({'result': result})


@app.route('/trust_score_start', methods=['GET', 'POST'])
def trust_score_start():
    if request.method == 'POST':
        mobile_number = request.form['mobile_number']
        trust_score, alert_flag = get_trust_score(mobile_number)
        return render_template('result.html', trust_score=trust_score, mobile_number=mobile_number,
                               alert_flag=alert_flag)
    return render_template('trustscore.html')


def get_trust_score(mobile_number):
    user_search_column = 'Contact'
    user_data = df_trust[df_trust[user_search_column] == int(mobile_number)]

    if user_data.empty:
        print(f"No data found for Contact {mobile_number}")
        return None, False

    user_features = user_data[features_trust]
    user_features_scaled = scaler_trust.transform(user_features)
    trust_score = model_trust.predict_proba(user_features_scaled)[:, 1][0]

    trust_score *= 10
    trust_score = '{:.4f}'.format(trust_score)
    trust_score = float(trust_score)
    integer_part = int(trust_score)
    alert_flag = integer_part < 5

    return trust_score, alert_flag


if __name__ == '__main__':
    app.run(debug=True)
