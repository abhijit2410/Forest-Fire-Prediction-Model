

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("f_fire.csv")
data = np.array(data)

X = data[1:, 1:-1]
y = data[1:, -1]