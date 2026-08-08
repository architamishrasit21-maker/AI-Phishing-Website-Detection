# AI Phishing Website Detection

## Project Overview

This project is a simple AI-powered phishing website detection application built with Flask and a machine learning model.

It includes scripts for loading and inspecting the dataset, training a model, saving the trained model, and serving a web interface where users can submit a URL to check whether it is classified as phishing or legitimate.

## Project Structure

- `app.py`
  - Main Flask application and web app entrypoint.
  - Loads the saved model from `phishing_model.pkl`.
  - Displays the form UI and returns the prediction result.

- `index.html`
  - HTML template for the web interface.
  - Contains a simple form to enter a website URL and display the prediction.

- `dataset_small.csv`
  - Dataset used for model training and inspection.
  - Contains feature columns and the `phishing` target label.

- `train_model.py`
  - Reads the dataset.
  - Trains a `RandomForestClassifier` on a training split.
  - Evaluates model accuracy on a test split.

- `save_model.py`
  - Reads the full dataset.
  - Trains a `RandomForestClassifier` on all available data.
  - Saves the model as `phishing_model.pkl` using `joblib`.

- `read_dataset.py`
  - Loads the dataset and prints sample rows, shape, and column names.
  - Useful for quickly exploring the data structure.

- `variables.py`
  - Contains a small demo of basic Python variables and print output.
  - Not directly used by the web application.

- `hello.py`
  - Likely a simple example or test script.

## How to Run

1. Open a terminal in the project folder:
   ```powershell
   cd C:\Users\samya\Documents\Python_Venvs\AI-Phishing-Website-Detection
   ```

2. (Optional) Activate your virtual environment if you have one:
   ```powershell
   .\venv\Scripts\Activate
   ```

3. Install required packages if needed:
   ```powershell
   pip install flask joblib scikit-learn pandas
   ```

4. Ensure the model file exists. If not, create it with:
   ```powershell
   python save_model.py
   ```

5. Start the Flask app:
   ```powershell
   python app.py
   ```

6. Open your browser and go to:
   ```text
   http://127.0.0.1:5000/
   ```

## Notes

- The current `app.py` uses placeholder feature data (`[1, 1, 1, 1, 1]`) for prediction, so real URL feature extraction is not implemented yet.
- To make the app fully functional, add URL feature extraction logic and match the model input format.
- `phishing_model.pkl` is required for `app.py` to run successfully.
