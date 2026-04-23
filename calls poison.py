import scipy.stats as stats

prob1 = 1 - stats.poisson.cdf(20, 15)
print("The probability of having more than 20 calls in a 15-day period is:", prob1)

prob2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(17, 15)
print("The probability of having between 18 and 21 calls in a 15-day period is:", prob2)