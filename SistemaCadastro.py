# Amanda Galdino - RM560066
# Bruno Cantacini - RM560242
# Gustavo Gonçalves - RM556823
import json

import oracledb
def cadastrar_ocorrencia():
    try:
        print("----- CADASTRAR OCORRÊNCIAS  -----\n")

        cliente_nome = input("Nome do Cliente: ")
        descricao_problema = input("Descrição do problema: ")
        status = input("Status (ABERTO|EM ANDAMENTO|FECHADO): ")
        responsavel_tecnico = input("Nome do responsável: ")

        # Monta a instrução SQL de cadastro em uma string
        script = f"""INSERT INTO OCORRENCIAS (cliente_nome, descricao_problema, status, responsavel_tecnico) 
                       VALUES ('{cliente_nome}', '{descricao_problema}', '{status}', '{responsavel_tecnico}')"""

        # Executa e grava o registro na Tabela
        cursor.execute(script)
        conn.commit()

        print("\nOcorrência cadastrada com sucesso.")
    except ValueError:
        print("Digite um número inteiro para o id!")
    except Exception as error:
        print(f"Erro na transação do BD: {error}")

def atualizar_status():
    try:
        print("----- ATUALIZAR STATUS OCORRÊNCIA -----\n")

        id_ocorrencia = int(input("Digite o ID da ocorrência: "))

        script = f"""SELECT * FROM OCORRENCIAS WHERE ID = {id_ocorrencia}"""

        cursor.execute(script)
        lista_dados = cursor.fetchall()

        if len(lista_dados) == 0:
            print(f"Não há dados cadastrados com o ID = {id_ocorrencia}")
        else:
            status = input("Status (ABERTO|EM ANDAMENTO|FECHADO): ")
            script = f"""UPDATE OCORRENCIAS SET
                         STATUS = '{status}'
                         WHERE id = {id_ocorrencia}"""
            cursor.execute(script)
            conn.commit()

            print("\nStatus alterado com sucesso!")
    except ValueError:
        print("Digite um número inteiro para o id!")
    except Exception as error:
        print(f"Erro na transação do BD: {error}")

def atualizar_responsavel():
    try:
        print("----- ATUALIZAR RESPONSÁVEL TÉCNICO -----\n")

        id_ocorrencia = int(input("Digite o ID da ocorrência: "))

        script = f"""SELECT * FROM OCORRENCIAS WHERE ID = {id_ocorrencia}"""

        cursor.execute(script)
        lista_dados = cursor.fetchall()

        if len(lista_dados) == 0:
            print(f"Não há dados cadastrados com o ID = {id_ocorrencia}")
        else:
            responsavel_tecnico = input("Nome do responsável: ")
            script = f"""UPDATE OCORRENCIAS SET
                         RESPONSAVEL_TECNICO = '{responsavel_tecnico}'
                         WHERE id = {id_ocorrencia}"""
            cursor.execute(script)
            conn.commit()

            print("\nTécnico Responsável alterado com sucesso!")
    except ValueError:
        print("Digite um número inteiro para o id!")
    except Exception as error:
        print(f"Erro na transação do BD: {error}")


def excluir_ocorrencia():
    try:
        print("----- EXCLUIR UMA OCORRÊNCIA  -----\n")

        id_ocorrencia = int(input("Digite o ID da ocorrência: "))

        script = f"""SELECT * FROM OCORRENCIAS WHERE ID = {id_ocorrencia}"""

        cursor.execute(script)

        lista_dados = cursor.fetchall()

        if len(lista_dados) == 0:
            print(f"Não há dados cadastrado com o ID = {id_ocorrencia}")
        else:
            # Cria a instrução SQL de exclusão
            script = f"""DELETE FROM OCORRENCIAS WHERE ID = {id_ocorrencia}"""

            # Executa a instrução e atualiza a tabela
            cursor.execute(script)
            conn.commit()

            print("\nOcorrência excluída com sucesso.")
    except ValueError:
        print("Digite um número inteiro para o id!")
    except Exception as error:
        print(f"Erro na transação do BD: {error}")

def listar_ocorrencias():
    try:
        print("----- LISTAR OCORRÊNCIAS -----\n")

        script = f"""SELECT * FROM OCORRENCIAS ORDER BY ID"""
        cursor.execute(script)

        lista_dados = cursor.fetchall()

        if len(lista_dados) == 0:
            print(f"Não há dados cadastrados!")
        else:
            for item in lista_dados:
                print(item)
    except ValueError:
        print("Digite um número inteiro para o id!")
    except Exception as error:
        print(f"Erro na transação do BD: {error}")

def exportar_ocorrencias_status():
    try:
        print("----- BUSCAR E EXPORTAR OCORRÊNCIAS POR STATUS -----")
        status = input("Digite o status (ABERTO | EM ANDAMENTO | FECHADO): ").upper()

        if status not in ['ABERTO', 'EM ANDAMENTO', 'FECHADO']:
            print("Status inválido. Escolha as opções corretas.")
            return

        query = "SELECT * FROM OCORRENCIAS WHERE STATUS = :status"
        cursor.execute(query, {"status": status})
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhuma ocorrência encontrada com esse status.")
        else:
            colunas = [col[0] for col in cursor.description]
            dados_json = [dict(zip(colunas, linha)) for linha in resultados]

            nome_arquivo = f"ocorrencias_status_{status.lower().replace(' ', '_')}.json"
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                json.dump(dados_json, f, indent=4, ensure_ascii=False)

            print(f"{len(dados_json)} ocorrências exportadas para '{nome_arquivo}' com sucesso.\n")
    except Exception as error:
        print(f"Erro ao consultar ocorrências: {error}")

# Solicitar credenciais de Acesso (usuário e senha)
login = input("Usuário..: ")
senha = input("Senha....: ")

# Tentativa de Conexão com o Banco de Dados
try:
    # Conexão com o banco de dados
    conn = oracledb.connect(user=login,
                            password=senha,
                            host="oracle.fiap.com.br",
                            port=1521,
                            service_name="ORCL")

    # Cria o cursor para realizar as operações no banco de dados
    cursor = conn.cursor()

    # Loop principal do sistema
    while True:
        print()
        print("1 - Cadastrar Ocorrência")
        print("2 - Atualizar Status ")
        print("3 - Atualizar técnico responsável")
        print("4 - Excluir uma ocorrência")
        print("5 - Listar todas as ocorrências registradas")
        print("6 - Exportar ocorrências por status")
        print("7 - Sair")
        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                cadastrar_ocorrencia()
            case 2:
                atualizar_status()
            case 3:
                atualizar_responsavel()
            case 4:
                excluir_ocorrencia()
            case 5:
                listar_ocorrencias()
            case 6:
                exportar_ocorrencias_status()
            case 7:
                print('Programa finalizado.')
                conn.close()
                break
            case _:
                print('Opção inválida.')
except Exception as erro:
    print(f"Erro: {erro}")
