from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])
        backlogs = int(request.form['backlogs'])
        
        features = np.array([[cgpa, iq, backlogs]])
        prediction = model.predict(features)
        result = "Placed 🎉" if prediction[0] == 1 else "Not Placed ⚠️"
        
        return render_template('index.html', prediction_text=f"Prediction Result: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error in input: {str(e)}")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "Placement Predictor API"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)