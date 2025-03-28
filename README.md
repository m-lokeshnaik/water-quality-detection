# Water Quality Detection

[water quality.pptx](https://github.com/user-attachments/files/16588083/water.quality.pptx)

---

# Water Potability Analysis Using Anomaly Detection

## Overview

This project aims to analyze water quality data to determine potability using anomaly detection techniques. By leveraging machine learning models, the project identifies anomalies in water quality parameters and predicts whether the water is potable.

## Dataset

The dataset used in this project contains various water quality parameters, including:
- pH
- Turbidity
- Chlorine
- Dissolved Oxygen
- Temperature
- Potability (target variable)

## Project Structure

- `data/`: Contains the `custom-dataset.csv` file with water quality data.
- `notebooks/`: Jupyter notebooks for data exploration, model training, and evaluation.
- `src/`: Source code for data preprocessing, model implementation, and utility functions.
- `results/`: Contains results of model evaluations and visualizations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lokeshnaik7569/water-potability-analysis.git
   cd water-potability-analysis
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preprocessing**: Run the data preprocessing script to clean and prepare the dataset.
   ```bash
   python src/preprocess_data.py
   ```

2. **Model Training**: Train the anomaly detection models using the prepared dataset.
   ```bash
   python src/train_models.py
   ```

3. **Evaluation**: Evaluate the models and visualize the results.
   ```bash
   python src/evaluate_models.py
   ```

## Key Features

- **Data Cleaning**: Handles missing values and outliers in the dataset.
- **Anomaly Detection**: Implements various models to detect anomalies in water quality parameters.
- **Visualization**: Provides visual insights into data distribution and model performance.

## Results

The project successfully identifies key factors affecting water potability and improves prediction accuracy through optimized model parameters. Visualizations effectively communicate findings and support decision-making in water quality management.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [lokeshnaik7569@gmail.com](mailto:lokeshnaik7569@gmail.com).

