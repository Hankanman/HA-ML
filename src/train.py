import pandas as pd
from sklearn.model_selection import train_test_split
from model import create_model

def train_model():
    df = pd.read_csv('data/processed/combined_data.csv')
    X = df[['motion', 'temperature', 'humidity', 'luminance']].values
    y = df['presence'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = create_model()
    model.fit(X_train, y_train, epochs=50, batch_size=10, validation_split=0.2)

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Accuracy: {accuracy:.2f}')
    model.save('model.h5')
