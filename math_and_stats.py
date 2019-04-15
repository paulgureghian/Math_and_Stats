""" Created in April 2019 by Paul A. Gureghian. """

""" Calculate Stats and use Math on some sample data. """

### Imprt Numpy
import numpy as np

### Savings info
savings = [1000,2000,1000,10000,3000,2500,19000,7000,21000,32000]

### Compute some stats
count = len(savings)
 
mean = np.mean(savings)

var = np.var(savings)

std = np.std(savings)

coeff_var = (std/mean) * 100

### Print the stat values
print(f"Total Count: {count}")
print(f"Mean: {mean}")
print(f"Variance: {var}")
print(f"Standard Deviation: {std:.2f}")
print(f"Correlation of Variance: {coeff_var:.2f}%") 
