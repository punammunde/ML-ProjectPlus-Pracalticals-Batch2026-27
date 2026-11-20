# House Price Prediction Using Machine Learning

A Machine Learning mini project that predicts an estimated house price using:
- Area (square feet)
- Number of bedrooms
- Number of bathrooms

**Algorithm:** Linear Regression  
**Interface:** Streamlit  
**Output:** Estimated price in lakh

## Repository structure

```text
House_Price_Prediction/
├── app.py
├── train_model.py
├── requirements.txt
├── house_price_model.pkl       # generated after training; add your trained model
├── data/
│   └── house_data.csv          # original 22-row dataset
├── reports/
│   └── House_Price_Prediction_Report.pdf
└── practicals/                 # add your ML lab practicals here
```

## Dataset

The original project dataset has 22 records and four columns:
`area`, `bedrooms`, `bathrooms`, `price`.

Place the exact original `house_data.csv` in the `data/` folder. The original full CSV was not attached when this starter package was prepared, so no data rows have been invented.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Train the model

```bash
python train_model.py
```

This reads `data/house_data.csv`, trains Linear Regression, prints evaluation metrics and creates `house_price_model.pkl`.

## Run the Streamlit app

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit (normally `http://localhost:8501`).

## Recorded test predictions

| Test | Actual price (lakh) | Predicted price (lakh) |
|---|---:|---:|
| 1 | 35 | 33.6113 |
| 2 | 84 | 82.4154 |
| 3 | 64 | 65.2955 |
| 4 | 39 | 37.3305 |
| 5 | 93 | 89.8539 |

These are the five recorded test values from the project work. Re-running training may produce slightly different outputs if the dataset or software versions differ.

## Limitations

- Dataset size is small (22 records).
- Only three property features are used.
- Location, property age, construction quality and other market factors are not included.
- This is an academic demonstration, not a professional valuation tool.

## Author

Punam B. Munde  
TY CSE, MGM's College of Engineering, Nanded  
Academic Year: 2026–2027

## Submission checklist

- [ ] Original 22-row dataset in `data/`
- [ ] Trained `house_price_model.pkl`
- [ ] Project source code
- [ ] PDF report
- [ ] `requirements.txt`
- [ ] All completed ML lab practicals in `practicals/`
- [ ] Actual application screenshots
