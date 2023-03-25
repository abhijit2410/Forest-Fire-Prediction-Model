# Forest-Fire-Prediction-Model
<p>
  <img height="400px" width="900px" src="https://user-images.githubusercontent.com/77913276/227736240-acd92f39-f1e9-4d87-8cf3-138db58adf43.jpg">
</p>
This repository contains a forest fire prediction model that uses machine learning algorithms to predict the likelihood of a forest fire occurrence. The model is based on a dataset that includes meteorological data such as temperature, humidity, wind speed, and rain.

The project is built using Python programming language and utilizes several libraries, including Pandas, Numpy, Scikit-learn, and Matplotlib. The dataset used in this project is publicly available and has been preprocessed to ensure its accuracy and completeness.

## Installation
To run the model, you will need to install the following libraries:

* Pandas
* Numpy
* Scikit-learn
* Matplotlib

## Data Overview
 <p> 
      <img height="300px" src="https://user-images.githubusercontent.com/77913276/227735634-8e670613-94bb-4020-b9d1-a43a56f5adbc.jpg">   
 </p>
 
> ## Key Features

* X : x-axis spatial coordinate within the Montesinho park map: 1 to 9
* Y : y-axis spatial coordinate within the Montesinho park map: 2 to 9
* month : month of the year: ‘jan’ to ‘dec’
* day : day of the week: ‘mon’ to ‘sun’
* FFMC : FFMC (Fine Fuel Moisture Code) index from the FWI system: 18.7 to 96.20
* DMC : DMC (Duff Moisture Code) index from the FWI system: 1.1 to 291.3
* DC : DC (Drought Code) index from the FWI system: 7.9 to 860.6
* ISI : ISI (Initial Spread Index) index from the FWI system: 0.0 to 56.10
* temp : temperature in Celsius degrees: 2.2 to 33.30
* RH : relative humidity in %: 15.0 to 100
* wind : wind speed in km/h: 0.40 to 9.40
* rain : outside rain in mm/m2 : 0.0 to 6.4
* area : the burned area of the forest (in ha): 0.00 to 1090.84

## Data Preprocessing
  > ## 1.Data preprocessing for days
![0_8vRSFWy7wadlV-Qu](https://user-images.githubusercontent.com/77913276/227735850-25405781-bfa3-4e50-b34e-0affcfe0e3ac.jpg)

  > ## 2.Scaling Area and Rain
![1_neB73_M12k6iqRMS3qfhsg](https://user-images.githubusercontent.com/77913276/227735903-62edf2b3-bca6-47b2-be12-5fda72d312b0.jpg)

## Testing with different values of hyperparametes
   > ## Batch Size: 4, 6, 10, 16, 32, 64, 128, 260
![1_XXnnLLdvd32_b9LYlvjl4A](https://user-images.githubusercontent.com/77913276/227735995-1aa050fd-a3ff-4604-8acc-5f6e84136916.jpg)


## Curves
  > ## Loss Curve
<p>
   <img src="https://user-images.githubusercontent.com/77913276/227736161-6b9c2bd0-1e22-42f2-ac76-b35be1538899.jpg">
</p>
  > ## Accuracy Curve
<p>
  <img src="https://user-images.githubusercontent.com/77913276/227736181-794e7cb3-d90b-43a2-acbd-e1be163cc391.jpg">
</p>
    
## Acknowledgements

* The dataset used in this project is publicly available and can be found on Kaggle.
* The code for this project was inspired by the work of several machine learning researchers and practitioners.
