import requests
import click

SOURCE_URL = "https://transparencia.joaopessoa.pb.gov.br:8080/filter-licitacoes"


@click.group()
def cli():
    pass


@click.command()
@click.option("--data_inicial", help="Primeira data do período de busca.")
@click.option("--data_final", help="Última data do período de busca.")
def read_licitacao_list(data_inicial, data_final):
    """
    Função que lê a lista de licitações da prefeitura de João Pessoa.
    """
    payload = {
        "data_inicial": data_inicial,
        "data_final": data_final,
    }

    response = requests.post(SOURCE_URL, data=payload)
    return response.text


@click.command()
@click.option("--id_licitacao", help="ID da licitação.", type=int)
def read_licitacao_data(id_licitacao):
    # TODO: add output format option (json, csv, stdout)
    """
    Função que lê os detalhes de uma licitação específica.
    """

    payload = {"id": id_licitacao}
    url = f"https://transparencia.joaopessoa.pb.gov.br:8080/licitacao-details"
    response = requests.post(url, data=payload)
    print(response.text)
    return response.text


cli.add_command(read_licitacao_data)
cli.add_command(read_licitacao_list)

if __name__ == "__main__":
    cli()
