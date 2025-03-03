from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dummy_users = [
    {'name': 'User1', 'mobile': '9876543210', 'aadhar': '123456789012'},
    {'name': 'User2', 'mobile': '9876543211', 'aadhar': '234567890123'},
    {'name': 'User3', 'mobile': '9876543212', 'aadhar': '234567890123'}
]


@app.route('/')
def index():
    return render_template('double_verification_index.html')

@app.route('/verify', methods=['POST'])
def verify_aadhar():
    verification_number = request.form.get('verification_number')
    receiver_number = request.form.get('receiver_number')

    verification_aadhar = next((user['aadhar'] for user in dummy_users if user['mobile'] == verification_number), None)
    receiver_aadhar = next((user['aadhar'] for user in dummy_users if user['mobile'] == receiver_number), None)

    result = 'Matching' if verification_aadhar == receiver_aadhar else 'Mismatch'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
