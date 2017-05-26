import numpy as np
import pandas as pd

def C_read(covertype_path):
	#read file covertype
	print "Loading data for CoverType data..."

	names = [
	    'Elevation',
	    'Aspect',
	    'Slope',
	    'Horizontal_Distance_To_Hydrology',
	    'Vertical_Distance_To_Hydrology',
	    'Horizontal_Distance_To_Roadways',
	    'Hillshade_9am',
	    'Hillshade_Noon',
	    'Hillshade_3pm',
	    'Horizontal_Distance_To_Fire_Points',
	]

	Wilderness_Area = []
	for i in range(4):
	    Wilderness_Area.append('Wilderness_Area_{}'.format(i+1))

	Soil_Type = []
	for i in range(40):
	    Soil_Type.append('Soil_Type_{}'.format(i+1))

	names.extend(Wilderness_Area + Soil_Type + ['Cover_Type'])
	covertype_df = pd.read_csv(covertype_path, names=names)
	#create training/testing data
	CX = covertype_df.drop('Cover_Type',axis=1)
	Cy = covertype_df['Cover_Type']
	C = np.concatenate((CX, Cy.reshape((len(Cy), 1))), axis=1)
	print "done"
	return C

def M_read(mnist_train_path):
	#read file
	print "Loading data for MNIST..."
	mnist_train_df = pd.read_csv(mnist_train_path, header=None)
	M = np.array(mnist_train_df)[1:]
	M = np.array(M, dtype='float')
	M = np.concatenate((M[:, 1:], M[:, 0].reshape((len(M[:, 0]), 1))), axis=1)
	print "done"
	return M