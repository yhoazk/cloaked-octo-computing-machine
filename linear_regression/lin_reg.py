from pylab import plot,show
from scipy import stats

xi = range(9)
print(xi)
# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)


line = slope*xi+intercept
plot(xi,line,'r-',xi,y,'o')
show()
