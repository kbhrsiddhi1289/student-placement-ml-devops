import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Sample training data (CGPA, IQ, Past Backlogs -> Placed: 1 or 0)
data = {
    'cgpa': [8.5, 6.2, 7.8, 5.5, 9.0, 6.8, 7.2, 4.8, 8.9, 6.5],
    'iq': [115, 90, 105, 85, 125, 95, 100, 80, 120, 92],
    'backlogs': [0, 1, 0, 2, 0, 1, 0, 3, 0, 1],
    'placed': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
X = df[['cgpa', 'iq', 'backlogs']]
y = df['placed']

model = LogisticRegression()
model.fit(X, y)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully as model.pkl")