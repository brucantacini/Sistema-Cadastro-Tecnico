# Sistema-Cadastro-Tecnico

Este projeto é um sistema em Python para gerenciamento de ocorrências técnicas com armazenamento e manipulação de dados em um banco Oracle. Os usuários podem cadastrar, atualizar, excluir, listar e exportar ocorrências por status.

## Funcionalidades

Cadastro de ocorrências: registra novos incidentes no banco de dados.

Atualização de status: permite atualizar o status de uma ocorrência.

Atualização do responsável técnico: altera o técnico designado para uma ocorrência.

Exclusão de ocorrências: remove registros específicos do banco.

Listagem geral: exibe todas as ocorrências registradas.

Exportação por status: exporta os dados filtrados por status em arquivos .json.

## table para criação no sql

CREATE TABLE OCORRENCIAS (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cliente_nome VARCHAR2(100),
    descricao_problema VARCHAR2(500),
    status VARCHAR2(20),
    responsavel_tecnico VARCHAR2(100)
);

## Necessário instalar pacote oracledb
pip install oracledb

