import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier


from sklearn.metrics import accuracy_score
import pickle

#Read data
data_frame = pd.read_csv("cords.csv")
x = data_frame.drop("class", axis=1)
y = data_frame['class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#Train model
pieline = {
    'lr': make_pipeline(StandardScaler(), LogisticRegression()),
    'rc': make_pipeline(StandardScaler(), RidgeClassifier()),
    'rf': make_pipeline(StandardScaler(), RandomForestClassifier()),
    'gb': make_pipeline(StandardScaler(), GradientBoostingClassifier())
}

fit_models = {}
for algo, pipeline in pieline.items():
    model = pipeline.fit(x_train, y_train)
    yhat = model.predict(x_test)
    fit_models[algo] = model

    print(algo, accuracy_score(y_test, yhat))

with open('action_game.pkl', 'wb') as f:
    pickle.dump(fit_models['rf'], f)




