from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
from modules import Perceptron


# wczytanie zbioru danych
irys_data = load_iris()
# obrobienie jedynie do potrzebnych zmiennych
irys_data_final = pd.DataFrame(data=np.c_[irys_data["data"], irys_data["target"]],
                               columns=irys_data["feature_names"] + ["target"])
# wybieram tylko versicolor i virginica
irys_data_final = irys_data_final[irys_data_final.loc[:,"target"] != 0]
irys_data_final = irys_data_final.drop(["sepal width (cm)", "petal width (cm)"], axis=1)

# obliczenie parametrow modelu
perceptron_model = Perceptron()
perceptron_model.fit(irys_data_final.iloc[:, :2].values, irys_data_final.target.values)

app = Flask(__name__)

@app.route('/predykcja', methods=['GET'])
def home():
    # wpisujemy tutaj wartości sepal length i petal length
    # mozna tez w linku po /predykcja dopisa ?sl=wartosc1&pl=wartosc2
    sl = request.args.get("sl", 1)
    pl = request.args.get("pl", 1)
    res = perceptron_model.predict([float(sl), float(pl)]).tolist()
    res = {1: 'Versicolor', 2: 'Virginica'}[res]
    return f"{res}"

app.run(port='5013')
