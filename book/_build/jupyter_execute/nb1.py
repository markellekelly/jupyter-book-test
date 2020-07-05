# This is a test notebook.

Gonna make it into a book. Check out some plots

import seaborn as sns

iris = sns.load_dataset('iris')
iris.head()

sns.violinplot(x='species',y='sepal_length',data=iris)

sns.jointplot(x='sepal_length',y='sepal_width',data=iris)

