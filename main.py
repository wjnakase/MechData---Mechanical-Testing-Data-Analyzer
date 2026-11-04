from src.data_loader import load_data


def main():
    arquivo = "data/raw/20250604 BAJA long.XLS"

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

    except Exception as erro:
        print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()