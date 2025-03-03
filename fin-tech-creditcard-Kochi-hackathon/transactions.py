from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

model = RandomForestClassifier()

df = pd.read_csv('fraud_dataset_example.csv')

df['orig_balance_change'] = df['newbalanceOrig'] - df['oldbalanceOrg']
df['dest_balance_change'] = df['newbalanceDest'] - df['oldbalanceDest']

features = ['amount', 'orig_balance_change', 'dest_balance_change']
X = df[features]

y = df['isFraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
suspicious_transactions = df.loc[X_test.index[predictions == 1], ['nameDest', 'amount', 'type']]

print("Suspicious Transactions:")
print(suspicious_transactions)