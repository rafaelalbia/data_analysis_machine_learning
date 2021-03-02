import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/athlete_events.csv')
print(data.head())

# histogram = data.hist(column='Weight', bins = 100)
# plt.show()

array = np.array([6, 5, 1, 7, 9, 4])
plt.hist(array, bins = 10)
plt.show()
