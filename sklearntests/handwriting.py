from sklearn import datasets
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

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

images_and_labels = list(zip(digits.images, digits.target));

for index,(image,label) in enumerate(images_and_labels[:8]):

	plt.subplot(2,4, index+1);
	plt.axis('off');
	plt.imshow(image,cmap = plt.cm.gray_r,interpolation = 'nearest');

	plt.title('Training' + str(label));

plt.show();

# print(images_and_labels[:8]);