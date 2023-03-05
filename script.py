from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

print('Cotação Moedas Em Tempo Real')
print('Fonte: InfoMoney')

def obter_cotacao_moedas() -> PrettyTable:
    try:
        URL_INFOMONEY_CAMBIO = 'https://www.infomoney.com.br/ferramentas/cambio/'
        requestSite = requests.get(URL_INFOMONEY_CAMBIO)
        requestSite.raise_for_status()  # verificação de erros na request
        content = BeautifulSoup(requestSite.text, 'html.parser')
        createTable = PrettyTable(['Moeda', 'Tipo', 'Compra', 'Venda', 'Var%'])
        container_table = content.find('div', attrs={'id': 'container_table'})
        default_table = container_table.find('table', attrs={'class': 'default-table'}).find('tbody').find_all('tr')
        for table in default_table:
            row_values = table.text.strip().split()
            if len(row_values) == 4:
                row_values.insert(1, "Todos")
            createTable.add_row(row_values)
        print(createTable)
        return createTable

    except requests.exceptions.HTTPError as http_err:
        print(f'Houve um erro HTTP: {http_err}')
    except Exception as err:
        print(f'Houve um erro na aplicação: {err}')
        raise

obter_cotacao_moedas()
