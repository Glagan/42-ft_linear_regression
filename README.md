# ft_linear_regression

## Requirements

``Python 3`` and ``matplotlib``.

## Usage

Train to get theta0 and theta1 first:

```python
python train.py
```

You can then estimate a price for a given mileage:

```python
python estimate.py [mileage]
```

To see the effect of changing the learning rate with the given parameters you can use ``learning_rate.py``.  
This will display a graph with the sum of squarred residuals for 1000 iterations.

```python
python learning_rate.py
```

## Bonuses

* Graph with dataset and trained linear regression line
* Graph with the effect of different learning rates

## Resources

* Machine Learning
	* Full Course
		* This is *mandatory*
		* Look at the 42-AI Bootcamp Machine Learning module 6 to see what parts you should watch
		* https://www.coursera.org/learn/machine-learning
	* StatQuest
		* https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF
		* Linear Regression
			* https://www.youtube.com/watch?v=PaFPbb66DxQ
		* Gradient Descent
			* https://www.youtube.com/watch?v=sDv4f4s2SB8
	* Linear Regression
		* https://www.youtube.com/watch?v=GhrxgbQnEEU
		* https://towardsdatascience.com/linear-regression-cost-function-gradient-descent-normal-equations-1d2a6c878e2c
	* Linear Regression with Gradient Descent
		* https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931
	* Feature Scaling
		* https://en.wikipedia.org/wiki/Feature_scaling#Standardization
		* https://stackoverflow.com/questions/32108179/linear-regression-normalization-vs-standardization
* 42-AI
	* https://github.com/42-AI/bootcamp_machine-learning
* Python
	* https://github.com/42-AI/bootcamp_python
	* Head First Python, Second Edition (Paul Barry, Editions O'Reilly)
