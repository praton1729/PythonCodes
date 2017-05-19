from sklearn import datasets
from sklearn import decomposition
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import PCA

digits = datasets.load_digits();

# digits = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra",header=None);

# print(digits.keys());
# print(digits.data);

digits_data = digits.data;

# print(digits.data.shape);
# print(digits.target.shape);

number_digits = len(np.unique(digits.target));

# print(digits.images.shape);
# print(number_digits);

b = np.all((digits.images.reshape(1797,64)) == digits_data);
# print(b);

# fig = plt.figure(figsize = (6,6));

# fig.subplots_adjust(left =0, right = 1, bottom = 0, top = 1, hspace = 0.05, wspace = 0.05);

# for i in range(64):

# 	ax = fig.add_subplot(8, 8, i+1, xticks = [], yticks = []);
# 	ax.imshow(digits.images[i], cmap= plt.cm.binary, interpolation = 'nearest');
# 	ax.text(0, 7, str(digits.target[i]));

# plt.show();

randomized_pca = decomposition.RandomizedPCA(n_components = 2);

reduced_data_rcp = randomized_pca.fit_transform(digits_data);

pca = PCA(n_components = 2);

reduced_data_pca = pca.fit_transform(digits_data);

print("Random one\n");
print(reduced_data_rcp);
print("\n");
print("Regular one\n");
print(reduced_data_pca);
# colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray'];