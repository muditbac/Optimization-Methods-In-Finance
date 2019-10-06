import datetime
import numpy as np
import os
import pandas as pd
import pandas_datareader as pdr
from IPython.core.display import HTML

"""
This file provides functions for different protfolio optimizations problems 
"""


def get_stocks_data(stock_indices, filename="stock.h5", cache=True, start_date=datetime.datetime(2015, 1, 1), interval='w'):
	"""
	If file exists then fetches stock prices from file otherwise fetches the data from Yahoo Finance and 
	save it to file
	""" 
	if filename and os.path.exists(filename):
	    historical_data = pd.read_hdf(filename, "/yahoo")
	else:
	    historical_data = pdr.data.YahooDailyReader(stock_indices, start=start_date , interval=interval).read()
	    if filename and cache: historical_data.to_hdf(filename, "/yahoo")
	return historical_data

def get_rate_of_return(prices):
	"""
	Returns rate of return from the prices. Assuming data is provided in descending order of date
	"""
	return_rate = (prices - prices.shift(-1)) / prices.shift(-1)
	return_rate = return_rate[1:-1]
	return return_rate

# Helper functions for markowitz mean variance models
def get_risk_and_return(ror_mean, ror_covariance, weights):
	"""
	Computes risk and rate of return of the weighted portfolio
	"""
	risk = weights.transpose().dot(ror_covariance.dot(weights))
	mean_return = weights.transpose().dot(ror_mean)
	return np.sqrt(risk.values.ravel()[0]), mean_return.values.ravel()[0]

def get_optimial_portfolio(ror_mean, ror_covariance, rate_of_return=None, covariance_inv=None):
	"""
	Returns optimal portfolio for minimization of covariance risk
	"""
	if not covariance_inv:
		covariance_inv = np.linalg.inv(ror_covariance.values)
	if not rate_of_return:
		w_optimal = covariance_inv.sum(1)
		w_optimal = w_optimal/w_optimal.sum()
	else:
		a = [[ror_mean.dot(covariance_inv).dot(ror_mean), ror_mean.dot(covariance_inv).sum()],
			[covariance_inv.dot(ror_mean).sum(), covariance_inv.sum()]]
		b = [2*rate_of_return, 2]
		l1, l2 = np.linalg.solve(a,b)
		w_optimal = l1*covariance_inv.dot(ror_mean)/2+l2*covariance_inv.sum(1)/2
	
	w_optimal = pd.DataFrame(w_optimal, ror_covariance.columns, ['weights'])
	risk, ror = get_risk_and_return(ror_mean, ror_covariance, w_optimal)
	return w_optimal, risk, ror

def rectify_font():
	return HTML("""
	<style>
	div.text_cell_render { /* Customize text cells */
	font-family: 'Times New Roman';
	/*font-size:1.5em;
	line-height:1.4em;
	padding-left:3em;
	padding-right:3em;*/
	}
	</style>
	""")