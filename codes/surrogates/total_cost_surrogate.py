import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2
from keras.callbacks import History, LearningRateScheduler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError, MeanSquaredLogarithmicError
import argparse
import os

# Setting random seed for reproducibility
np.random.seed(1234)
tf.random.set_seed(0)

# Argument parser for input/output paths, hyperparameters, and model saving options
parser = argparse.ArgumentParser(description='Train a MLP for regression with customizable architecture.')
parser.add_argument('--input', type=str, default='C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\\Energy PR\\codes\\simulation\\input_output_pairs\\inputFD.csv', help='Path to the input CSV file.')
parser.add_argument('--output', type=str, default='C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\\Energy PR\\codes\\simulation\\input_output_pairs\\outputFD.csv', help='Path to the output CSV file.')
parser.add_argument('--hidden_units', type=int, nargs='+', default=[64, 128, 256, 256, 128, 64], help='List of hidden units per layer.')
parser.add_argument('--reg_coeffs', type=float, nargs='+', default=[1, 1, 1, 1, 1, 1], help='List of regularization coefficients corresponding to each layer.')
parser.add_argument('--loss', type=str, choices=['mse', 'msle'], default='mse', help='Loss function to use (mse for Mean Squared Error, msle for Mean Squared Logarithmic Error).')
parser.add_argument('--epochs', type=int, default=200, help='Number of epochs to train.')
parser.add_argument('--model_dir', type=str, default='.\\models', help='Directory to save the trained model.')
parser.add_argument('--model_name', type=str, default='FR_total_model', help='Name to save the trained model under.')

args = parser.parse_args()

# Ensure hidden_units and reg_coeffs lists have the same length
if len(args.hidden_units) != len(args.reg_coeffs):
    raise ValueError("The length of hidden_units and reg_coeffs must be the same.")

# Function to adjust learning rate over epochs
def scheduler(epoch, lr):
    decay = 0
    return 0.0003 * 1/(1 + decay * epoch)

# Loading data
X = np.array(pd.read_csv(args.input, header=None))
y = np.array(pd.read_csv(args.output, header=None))[:, 0].reshape(-1, 1)

# Removing NaNs
ynans = np.isnan(y).flatten()
xnans = np.isnan(X).any(axis=1)
X, y = np.delete(X, np.unique(np.concatenate((ynans, xnans))), axis=0), np.delete(y, np.unique(np.concatenate((ynans, xnans))), axis=0)

# Splitting data into train, dev, and test sets
train_test_split = np.random.uniform(0, 1, len(X))
train_idx, dev_idx, test_idx = train_test_split <= 0.75, (train_test_split > 0.75) & (train_test_split <= 0.9), train_test_split > 0.9
X_train, y_train = X[train_idx], y[train_idx]
X_dev, y_dev = X[dev_idx], y[dev_idx]
X_test, y_test = X[test_idx], y[test_idx]

# Building the model
model = Sequential()
model.add(Dense(args.hidden_units[0], input_dim=X_train.shape[1], activation='relu', kernel_regularizer=l2(args.reg_coeffs[0])))
for units, reg in zip(args.hidden_units[1:], args.reg_coeffs[1:]):
    model.add(Dense(units, activation='relu', kernel_regularizer=l2(reg)))
model.add(Dense(1, activation='linear'))

# Choosing the loss function based on the argument
loss_function = MeanSquaredError() if args.loss == 'mse' else MeanSquaredLogarithmicError()

# Compiling the model
model.compile(loss=loss_function, optimizer=Adam(), metrics=['mae'])

# Training the model
history = model.fit(X_train, y_train, epochs=args.epochs, verbose=2, callbacks=[History(), LearningRateScheduler(scheduler)])

# Evaluating the model
train_mae = mean_absolute_error(y_train, model.predict(X_train))
dev_mae = mean_absolute_error(y_dev, model.predict(X_dev))
test_mae = mean_absolute_error(y_test, model.predict(X_test))

print(f'Train MAE: {train_mae:.4f}, Dev MAE: {dev_mae:.4f}, Test MAE: {test_mae:.4f}')

# Saving the model
model_json = model.to_json()
model_json_path = os.path.join(args.model_dir, f"{args.model_name}.json")
model_weights_path = os.path.join(args.model_dir, f"{args.model_name}.h5")

# Ensuring the directory exists
os.makedirs(args.model_dir, exist_ok=True)

# Writing the model architecture to a JSON file
with open(model_json_path, "w") as json_file:
    json_file.write(model_json)

# Saving the model weights
model.save_weights(model_weights_path)

print(f"Model architecture saved to {model_json_path}")
print(f"Model weights saved to {model_weights_path}")
