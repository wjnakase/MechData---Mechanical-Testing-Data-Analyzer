from pathlib import Path
import matplotlib.pyplot as plt
from src.data_loader import load_data


def main():
    arquivo = "data/raw/BAJA 20261013 frag 3_001.xlsx"

    try:
        dados, metadados = load_data(arquivo)

        print("\n===== MECHDATA =====")

        print("\nInformações do arquivo:")
        print(metadados)

        print("\nPrimeiras linhas dos dados:")
        print(dados.head())

        print("\nDimensões:")
        print(f"Linhas: {dados.shape[0]}")
        print(f"Colunas: {dados.shape[1]}")

        print("\nEstatísticas:")
        print(dados.describe())

        # ======Plotting the data TEST=======
        figura, eixo = plt.subplots(figsize=(9, 6))
        eixo.plot(dados.iloc[:, 0], dados.iloc[:, 1], linewidth=1.5)
        eixo.set_title("tempo x torque")
        eixo.grid(True, alpha=0.3)
        figura.tight_layout()

        caminho_grafico = Path("reports/curva_tempo_torque.png")
        figura.savefig(caminho_grafico, dpi=150)
        print(f"\nGráfico salvo em: {caminho_grafico}")
        plt.show()

    except Exception as erro:
        print(f"\nErro: {erro}")

if __name__ == "__main__":
    main()