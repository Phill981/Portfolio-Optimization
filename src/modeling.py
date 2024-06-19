import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class AssetSelectionModel:
    def __init__(self, data):
        self.data = data
    
    def train_model(self):
        features = self.data[['MA50', 'MA200', 'Returns']]
        target = (self.data['Returns'] > 0).astype(int)
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model

if __name__ == "__main__":
    data = pd.read_csv('../data/processed/processed_data.csv', index_col=0, parse_dates=True)
    asm = AssetSelectionModel(data)
    model = asm.train_model()
