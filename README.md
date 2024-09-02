


# Algerian Forest Fire Prediction using Ridge Regression

This project is a beginner's exploration into Machine Learning, focusing on predicting Algerian forest fires using Ridge Regression models from scikit-learn. The project also integrates a web application using the Flask framework, allowing users to interact with the model through a simple webpage.

## Project Overview

The goal of this project is to predict forest fires in Algeria based on a dataset of environmental factors. The steps involved are:

1. **Data Cleansing**: Preparing the dataset by handling missing values, outliers, and formatting issues to ensure it is ready for preprocessing.
2. **Data Preprocessing**: Applying the Standard Scaler to normalize the features and split the dataset into training (75%) and testing (25%) sets.
3. **Model Training**: Training the Ridge Regression model on the training dataset.
4. **Prediction**: Predicting forest fire occurrences on the test dataset using the trained model.
5. **Performance Evaluation**: Measuring and reporting the model's performance using appropriate metrics.

The project is further extended with a Flask-based web application that provides an interactive interface for users to input data and receive predictions.

## Project Structure

- `app/`: Contains the Flask web application files.
- `notebooks/`: Jupyter Notebook files for data analysis, model training, and evaluation.
- `data/`: The `.csv` dataset used for training and testing the model.
- `requirements.txt`: A list of all Python libraries and dependencies required to run the project.

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/algerian-forest-fire-prediction.git
    cd algerian-forest-fire-prediction
    ```

2. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the Dataset**:
   Place the `.csv` dataset file in the `data/` directory.

4. **Run the Jupyter Notebook**:
   Open the notebook in the `notebooks/` directory and run it to train the model and evaluate its performance.

5. **Run the Web Application**:
    ```bash
    cd app
    flask run
    ```
    Access the application at `http://127.0.0.1:5000/` in your web browser.

## Usage

- **Prediction**: Use the web interface to input environmental data and predict forest fire occurrences.
- **Model Analysis**: Review the Jupyter Notebook for detailed analysis, model training steps, and performance metrics.

## Performance Metrics

The model's performance is evaluated using metrics such as Mean Squared Error (MSE), R² score, and others, which are reported in the notebook.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bug reports.

## License

This project is licensed under the MIT License.

---

This README provides a clear overview of your project, instructions for setup, and details on usage.
