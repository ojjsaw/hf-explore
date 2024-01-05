import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import RNN, LSTMCell, Dense, Reshape
from tensorflow.keras.optimizers import Adam

# Define the input shape in NCHW format
N, C, H, W = 100, 3, 10, 10  # Example values: 100 samples, 3 channels, 10x10 image

# Define the model
model = Sequential()

# First, reshape the input to (N, H, C*W) to treat each row of the image as a sequence
model.add(Reshape((H, C*W), input_shape=(C, H, W))) 

# Add an RNN layer with an LSTMCell
model.add(RNN(LSTMCell(50)))  # 50 units in the LSTM cell

# Output layer - for simplicity, let's assume a regression problem
model.add(Dense(1))

# Compile the model
model.compile(optimizer=Adam(), loss='mean_squared_error')

# Generate some dummy NCHW format data
X_dummy = np.random.random((N, C, H, W))

# Generate dummy output data
y_dummy = np.random.random((N, 1))

# Train the model on the dummy data
model.fit(X_dummy, y_dummy, epochs=5, batch_size=32)

# Save the model
model.save('my_nchw_lstm_model.h5')

model.summary()
