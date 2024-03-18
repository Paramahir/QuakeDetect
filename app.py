from flask import Flask, render_template, request, flash, redirect
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os

app = Flask(__name__)
app.secret_key = "super secret key"

# Load and prepare your data
file_path = 'seismic_data_with_labels.csv'  # Make sure this path is correct
data = pd.read_csv(file_path)
if 'label' in data.columns:
    X = data.drop('label', axis=1)
    y = data['label']
else:
    raise ValueError("No 'label' column found in the dataset")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

event_labels = {
    0: "Earthquake",
    1: "Explosion",
    2: "Background Noise",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            waveform = pd.read_csv(file).values.flatten().reshape(1, -1)
            prediction = clf.predict(waveform)[0]
            label = event_labels.get(prediction, "Unknown")
            return render_template('result.html', label=label)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
