#Hypergeometric calculation in python following Sanbomics' tutorial on youtube at https://youtu.be/Go3qssiBzuY

# Have a marathon: Team A: n = 50 people, 1000 people in the marathon at the start
# At the end, Team A has 16 people, and only 200 people total finished. What is the chance that Team A had 16 people finish by chance (rather than skill?)

from scipy import stats
import seaborn as sns

total_runners = 1000
num_teamA = 50
num_winners = 200
num_A_winners = 16

#prob that exactly 16 from team A finished by chance
p = stats.hypergeom.pmf(num_A_winners, total_runners, num_winners, num_teamA)
print(p)

pmf = range(0,25)
pmf = list(map(lambda x: stats.hypergeom.pmf(x, total_runners, num_winners, num_teamA),pmf))
ax = sns.lineplot(x = range(0,25), y = pmf)

#cumulative distribtuion function, sum of the area under the curve
cdf = range(0,25)
cdf = list(map(lambda x: stats.hypergeom.cdf(x, total_runners, num_winners, num_teamA),cdf))
ax = sns.lineplot(x = range(0,25), y = cdf)

#use cdf to calculate the p-value
#prob that 16 or less finished, we need: prob that fewer than 16 from team A finish: p(1) + p(2) ... p(15)

1 - stats.hypergeom.cdf(num_A_winners-1, total_runners, num_winners, num_teamA)
1-p




