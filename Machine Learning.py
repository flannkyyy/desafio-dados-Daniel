import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import tkinter as tk
from tkinter import messagebox
import os
caminho_arquivo = r"C:\Users\Daniel\Documents\Programação\Processo Seletivo\teste_indicium_precificacao.csv"
if not os.path.exists(caminho_arquivo):
    print(f"Erro: Arquivo não encontrado no caminho especificado: {caminho_arquivo}")
else:
    try:
        print("Lendo o arquivo CSV...")
        df = pd.read_csv(caminho_arquivo)       
        print("Limpando dados...")
        df = df.dropna(subset=["price"])        
        features = ["latitude", "longitude", "minimo_noites", "disponibilidade_365"]
        if not all([col in df.columns for col in features + ["price"]]):
            raise ValueError("Uma ou mais colunas esperadas não foram encontradas no arquivo CSV.")
        X = df[features]
        y = df["price"]        
        print("Dividindo os dados...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("Treinando o modelo...")
        modelo = RandomForestRegressor(n_estimators=200, random_state=42)
        modelo.fit(X_train, y_train)
        print("Fazendo previsões...")
        y_pred = modelo.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        print(f"Erro Médio Absoluto (MAE): {mae:.2f}")
        print("Salvando o modelo...")
        joblib.dump(modelo, "modelo_precificacao.pkl")
        def mostrar_resultado():
            root = tk.Tk()
            root.withdraw()  # Oculta a janela principal
            messagebox.showinfo("Resultado", f"Erro Médio Absoluto (MAE): {mae:.2f}\n\nModelo salvo com sucesso!")
            root.destroy()
        mostrar_resultado()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
