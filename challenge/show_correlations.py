import yfinance as yf
import pandas as pd
from dateutil import parser
import os
import itertools
import math
import numpy as np
import statistics
from statistics import mean
import matplotlib.pyplot as plt

#download the data using yfinance

#change the path to the file

data = [line.strip() for line in open('/home/luka/machine-learning/challenge/challenge_stocks.txt', 'r')]

print(data)

print(len(data))


def get_historical_data():

	for element in data:
		try:
			input_stock = element.strip()
			dataset = yf.download(input_stock, start="2019-1-1", end="2020-1-1")

		except:
			pass
		
		#change the path to the file

		dataset.to_csv(os.path.join('/home/luka/machine-learning/challenge/data/', input_stock + '.csv'))


get_historical_data()


def main():

	all_stocks = pd.DataFrame()

	for element in data:
		input_stock = element.strip()

		coefficients_list = []

		#read Adj close data for a stock

		close = pd.read_csv(os.path.join('/home/luka/machine-learning/challenge/data/', input_stock + '.csv'), usecols=['Date','Adj Close'])

		#create a dataframe for further use

		stock = pd.DataFrame({'ticker': np.repeat(input_stock, len(close)), 'Date': close['Date'],'close': close['Adj Close']})

		all_stocks = all_stocks.append(stock)


	df = all_stocks.pivot(index='Date', columns='ticker', values='close').pct_change().apply(lambda x: np.log(1+x))

	df = df.corr(method='pearson')

	print(df)

	plt.matshow(df)
	plt.show()

main()

