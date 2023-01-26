import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import seaborn as sns
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
##Dataframe 
pd.set_option('display.max_columns',10)
pd.set_option('display.width',50)
##importing dataset
data=pd.read_csv('data.csv')
print(data.head(5))
import matplotlib.pyplot as plt
%matplotlib inline
x=np.array([20,25,30,35,40]).reshape((-1,1))
y=np.array([45,37,28,22,18])
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
np.random.seed()
model=LinearRegression()
model.fit(x,y)
model=LinearRegression().fit(x,y)
print(f"intercept:{model.intercept_}")
print(f"slope:{model.coef_}")
y_pred=model.predict(x)
print(f"predicted:\n{y_pred}")
import numpy as np
import matplotlib.pyplot as plt
 def estimate_coef(x, y):
    # number of observations/points
  n = np.size(x)
      # mean of x and y vector
   m_x = np.mean(x)
    m_y = np.mean(y)
  # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
  return (b_0, b_1)
def plot_regression_line(x, y, b): 
   # plotting the actual points as scatter plot
 plt.scatter(x, y, color = "m",
marker = "o", s = 30)
  # predicted response vector
  y_pred = b[0] + b[1]*x
    # plotting the regression line
 plt.plot(x, y_pred, color = "g")
  # putting labels
plt.xlabel('x')
plt.ylabel('y')
# function to show plot
plt.show()
def main():
# observations / data
x = np.array([20,25,30,35,40])
y = np.array([45,37,28,22,18])
# estimating coefficients
    b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {}  \
\nb_1 = {}".format(b[0], b[1]))
# plotting regression line
    plot_regression_line(x, y, b)
if __name__ == "__main__"
    main()
## To Find The Sale Of Coffee at 32°C
x_predict = np.array([32]).reshape(-1,1)
y_predict = model.predict(x_predict)
y_predict

