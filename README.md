# MechData

Ferramenta em desenvolvimento para importar, organizar e visualizar dados brutos de ensaios mecânicos exportados pelo catman.

## Funcionalidades atuais

- Importa arquivos Excel `.xls` e `.xlsx`.
- Separa os metadados do início da planilha dos dados experimentais numéricos.
- Exibe metadados, primeiras linhas, dimensões e estatísticas descritivas no terminal.
- Plota as duas primeiras colunas numéricas e salva a imagem em `reports/curva_tempo_torque.png`.

O cálculo de propriedades mecânicas, como tensão, deformação e limite de escoamento, ainda não está implementado.

## Planos futuros

- Desenvolver um painel interativo com Streamlit para carregar arquivos e visualizar os resultados.
- Integrar a API da OpenAI para auxiliar na interpretação dos resultados dos ensaios, como apoio à análise técnica.

## Requisitos

- Python 3
- Dependências listadas em `requirements.txt`

## Instalação

Na raiz do projeto, crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No Windows, ative o ambiente com:

```powershell
.venv\Scripts\Activate.ps1
```

## Como executar a principio

Coloque o arquivo de ensaio em `data/raw/` e atualize a variável `arquivo` em `main.py` com o caminho desejado. Em seguida, execute:

```bash
python main.py
```

O programa mostra os dados e as estatísticas no terminal, abre uma janela com o gráfico e salva uma cópia em `reports/curva_tempo_torque.png`.

## Formato dos arquivos

O carregador foi pensado para exportações do catman em Excel. Ele lê a primeira aba da planilha, procura a primeira linha em que todas as células são numéricas e considera as linhas anteriores como metadados. Linhas de dados com células vazias ou não numéricas são removidas.

Atualmente, o gráfico usa as duas primeiras colunas numéricas, na ordem em que aparecem no arquivo. Portanto, confirme a ordem dos canais antes de interpretar o gráfico. O cabeçalho e as unidades ainda não são associados automaticamente às colunas.

## Estrutura do projeto

```text
.
├── data/
│   ├── processed/   # Dados tratados
│   └── raw/         # Arquivos originais dos ensaios
├── reports/         # Gráficos e relatórios gerados
├── src/
│   └── data_loader.py
├── tests/           # Testes automatizados
├── main.py
└── requirements.txt
```