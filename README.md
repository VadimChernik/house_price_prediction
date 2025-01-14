# House Price Prediction

This project aims to build a machine learning model to accurately forecast house prices and deploy it locally with Docker.
The goal is to provide accurate and actionable insights for real estate stakeholders. Below, we highlight use cases for this project.

## **Key Use Cases**

### 1. **Real Estate Valuation**
Accurately predict property values to assist buyers, sellers, and real estate agents in making informed decisions. This includes:
- Automated valuation models (AVMs).
- Providing a realistic price range based on current market trends and historical data.

### 2. **Loan Risk Assessment for Financial Institutions**
Enable banks and lenders to assess mortgage risks more effectively by predicting the value of properties being used as collateral. This improves risk management and helps in setting appropriate loan terms.

### 3. **Investment Analysis**
Assist real estate investors in:
- Evaluating the potential return on investment (ROI) of properties.
- Identifying neighborhoods or areas with appreciating value for better investment decisions.

### 4. **Home Improvement ROI Estimation**
Guide homeowners by predicting how specific renovations or upgrades (e.g., kitchen remodeling, energy-efficient installations) impact the property’s market value.

### 5. **Price Recommendations for Property Listings**
Empower property listing platforms by:
- Recommending optimal listing prices for sellers.
- Helping buyers find properties within their budget by suggesting accurate price ranges.


## Data

The dataset used for training the machine learning model can be found on Kaggle: [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data).


## Dependencies

This project uses `pipenv` for managing the Python environment and dependencies. Ensure you have the following installed:

- Python (version 3.12)
- `pipenv` (Python package for managing virtual environments)

## Installation

### Clone the Repository

Clone this repository to your local machine:

```bash
git https://github.com/VadimChernik/house_price_prediction.git
cd house_price_prediction
```

### Set Up the Environment

Ensure `pipenv` is installed. If not, install it via pip:

```bash
pip install pipenv
```

Then, create the virtual environment and install dependencies using `pipenv`:

```bash
pipenv install
```

### Activate the Environment

Activate the virtual environment to work within it:

```bash
pipenv shell
```


## Local Deployment with Docker

1. **Build the Docker Image:**
   - Use the following command to build the Docker image:
   ```bash
   docker build -t capstone-project .
   ```

2. **Run the Docker Container:**
   - Start a container locally using the following command:
   ```bash
   docker run -it --rm -p 9696:9696 capstone-project
   ```

3. **Access the Application:**
   - Update the `url` variable in the `test.py`. After making this change, execute the `test.py` script. This will enable you to view the response in JSON format.