# Optimization Methods In Finance
This repository contains the code and results of Optimization Methods in Finance course at IIT Kharagpur

## Dataset
We extracted data from `pandas_datareader` for following stocks:
- SBIN.NS'
- HDFCBANK.NS
- ASIANPAINT.NS
- ACC.NS
- HCLTECH.NS
- YESBANK.NS
- KOTAKBANK.NS
- WIPRO.BO
- MARUTI.BO
- ITC.BO
- COALINDIA.BO
- BHARTIARTL.BO


## MeanVarianceModel.ipynb	
- This notebook calculates rate of returns of 10 indian stocks and presents classical **Markovitz Mean-Variance Model** on them. This also presents a variant of model with returns constraint. We have also plotted optimal frontier of the model by showing tradeoff between rate of returns and risk. 
[[ TODO Image ]]
- We depict **Two Fund Theorem** that 'Any two optimal porftolio generates the optimal frontiers'. We then use this theorem to generate the same optimal frontier.
- We then show the **Capital Asset Pricing Model** and the **Market Capital Line** for the set of stocks.

## PortfolioDiagram.ipynb
- This shows effect of correlation between stock on the optimal frontier. The current model takes two stocks and shows the impact of the correlation parameter.

## Fuzzy Portfolio Optimization
