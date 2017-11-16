import numpy as np

def TTsplit(all_data, train_ratio = 0.75):
	np.random.shuffle(all_data)
	train_data = all_data[:int(len(all_data)*train_ratio)]
	test_data = all_data[int(len(all_data)*train_ratio):]
	return train_data, test_data

def getSubset(train_data, d):
	if d < 0 or d > 100:
		print "proportion out of range"
		return
	length = int(len(train_data)*d/100)
	sub_train = train_data[np.random.permutation(len(train_data))[:length]]
	return sub_train