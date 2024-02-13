##Phase 1 : Imports and reading data
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')

df1 = pd.read_csv('Documents/groundhog predictions dataset/groundhogs.csv')
df2= pd.read_csv('Documents/groundhog predictions dataset/predictions.csv')

##Phase 2: Data Understanding
df1.merge(df2,on='id',how='inner')
df1.head()
