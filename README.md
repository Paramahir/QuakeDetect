# QuakeDetect: Seismic Event Classifier

QuakeDetect is a Flask-based web application designed to classify seismic events. Utilizing a Random Forest Classifier, the application can predict various types of seismic activities based on waveform data provided in a CSV format.

## Features

- Upload seismic waveform data in CSV format.
- Get instant classification of the seismic event.
- Utilizes a trained Random Forest Classifier for predictions.

## Data

The current version of QuakeDetect uses a synthetically generated dataset for training and demonstration purposes. This synthetic dataset is intended to illustrate the functionality of the application and is not based on real seismic event data.

### Note on Real Data

For practical applications or research, users should obtain and use real seismic data. Real seismic datasets can be downloaded from official and reputable sources, such as governmental or research institutions dedicated to seismology and earthquake research.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository: git clone https://github.com/yourusername/quakedetect.git
2. Navigate to the project directory: cd quakedetect
3. Install the required Python packages: pip install flask scikit-learn


## Usage

To run the Flask application locally:

1. Set the FLASK_APP environment variable: export FLASK_APP=app.py # On Windows, use 'set' instead of 'export'
2. Run the application: flask run
3. Visit `http://127.0.0.1:5000/` in your web browser to use the application.

## How to Use

1. Prepare your seismic waveform data in a CSV file. The file should contain a single row of 1000 numeric values representing the waveform.
2. Navigate to `http://127.0.0.1:5000/` in your browser.
3. Click the "Upload" button and select your CSV file.
4. Click "Classify" to get the prediction.

## Project Structure

- `app.py`: The main Flask application script.
- `templates/`: Directory containing the HTML templates for the web interface.
- `static/`: Directory for static files (CSS, JS, images, etc. - if applicable).
- `requirements.txt`: File containing the list of dependencies to install.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request.




      

