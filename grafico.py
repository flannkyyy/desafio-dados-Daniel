import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
sns.set_palette("coolwarm")
df = pd.read_csv("teste_indicium_precificacao.csv")
plt.figure(figsize=(12, 6))
sns.histplot(df["price"], bins=50, kde=True, color="orange", edgecolor="black")
plt.xlim(0, 1000)
plt.title("Distribuição de Preços dos Anúncios", fontsize=14, fontweight="bold")
plt.xlabel("Preço (USD)", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
plt.figure(figsize=(12, 6))
sns.scatterplot(x=df["minimo_noites"], y=df["price"], alpha=0.5, color="darkorange", edgecolor="black")
plt.xlim(0, 30)
plt.ylim(0, 1000)
plt.title("Relação entre Mínimo de Noites e Preço", fontsize=14, fontweight="bold")
plt.xlabel("Número Mínimo de Noites", fontsize=12)
plt.ylabel("Preço (USD)", fontsize=12)

