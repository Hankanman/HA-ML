import pandas as pd
import keras

def evaluate_model():
    df = pd.read_csv('data/processed/combined_data.csv')
    X = df[['motion', 'temperature', 'humidity', 'luminance']].values
    y = df['presence'].values

    model = keras.models.load_model('model.h5')
    predictions = model.predict(X)
    predictions = (predictions > 0.5).astype(int)

    accuracy = (predictions == y.reshape(-1, 1)).mean()
    print(f'Overall Accuracy: {accuracy:.2f}')
