import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Question 7
# Part A

d = pd.read_csv("homework1_clinic.csv",
                dtype = {"id" : "string"})

d["severity"] = pd.Categorical(
    d["severity"],
    ["Mild", "Moderate", "Severe"],
    ordered = True)

print(d.shape)

print(d["id"].duplicated().sum())

print(d["wait_min"].isna().sum())

print((d["wait_min"] < 0).sum())

# Part B

x = d.dropna(subset = ["wait_min"])["wait_min"]

print(x.size)

print(x.mean(), np.median(x))

print(x.var(ddof = 1), x.std(ddof = 1))

print(np.quantile(x,[0.25, 0.5, 0.75],
                  method = "linear"))

q1 = np.quantile(x, 0.25, method = "linear")

q3 = np.quantile(x, 0.75, method = "linear")

iqr = q3 - q1

L = q1 - 1.5 * iqr

U = q3 + 1.5 * iqr

print(q1, q3, iqr, L, U)

print(x[(x < L) | (x > U)])

# These calculated values are the same as written values in question 4. 

# Part C

edges =  np.arange(0, 35, 5)

counts, _ = np.histogram(x, edges)

plt.hist(x, bins = edges,
         color = "#FF9CB5", edgecolor = "white")

plt.xlabel("Wait (minutes)")

plt.ylabel("Number of visits")

print(counts); plt.show()

plt.boxplot(x,
            orientation = "horizontal",
            whis = 1.5, showmeans = False)

plt.xlabel("Wait (minutes)")

plt.show()

# Part D

# Similar to the example in Lecture 3, most of the wait times for this dataset
# are in the lower bins, with the 25 minute outlier forming a tail on the
# right. The mean uses the 9 observed wait time count since missing values 
# cannot be calculated into the numerical mean. I would check and see if the 25
# minute wait was potentially a data collection error or what the cause of it
# was before making a decision on whether to remove it from the analysis. 

# Question 9
