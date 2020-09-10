import pandas as pd
import numpy as np
import seaborn as sns

test_table = pd.read_csv('testdata.csv')
print(test_table)
test_table.plot.scatter('Observation','Observation 2',c='Day')
sns.scatterplot(data=test_table,x='Observation',y="Observation 2",size = 'Day')