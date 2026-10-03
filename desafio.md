# Desafio Técnico: API de Automação Comercial

## Objetivo

Desenvolver uma API REST com autenticação para um sistema de automação comercial, usando Django. O projeto deve ser organizado em três módulos: **Cadastros**, **Faturamento** e **Relatórios**.

---

## Requisitos técnicos

- Python 3 e Django (o uso de Django REST Framework é recomendado).
- Banco de dados **SQLite**. O arquivo do banco deve ser enviado junto com o projeto, já com dados de exemplo cadastrados.
- Todos os endpoints, exceto o de login, devem exigir autenticação.
- Documentação da API em uma **collection do Postman**, enviada junto com o projeto.
- Código versionado em **Git**, com commits feitos ao longo do desenvolvimento.
- Um **README** explicando como instalar, configurar e rodar o projeto.

---

## Módulo Cadastros

Cada cadastro deve permitir **criar, listar, consultar, alterar e excluir** registros.

| Cadastro | Descrição |
|---|---|
| **Usuário** | Usuários que acessam o sistema. |
| **Empresa** | Empresa que realiza as vendas. |
| **Cliente** | Cliente que realiza as compras. |
| **Marca** | Marca dos produtos. |
| **Coleção** | Coleção dos produtos. |
| **Forma de pagamento** | Por exemplo: dinheiro, Pix, cartão de crédito, cartão de débito. |
| **Produto** | Todo produto pode ter uma marca e uma coleção. As duas são **opcionais**. |

Os campos de cada cadastro ficam a seu critério, desde que façam sentido para um sistema comercial.

---

## Módulo Faturamento

### Vendas

Funcionamento semelhante a um **PDV (ponto de venda)**. A venda deve registrar:

- empresa;
- cliente;
- usuário que realizou a venda;
- data;
- forma de pagamento;
- os produtos vendidos com suas quantidades.

**Regras:**

- O sistema **não controla estoque**.
- **Não existe** cancelamento de venda.
- Toda venda tem um **status**: `Pendente` ou `Finalizado`. A venda nasce como `Pendente`.

**Endpoints obrigatórios da venda** (além de criar, listar e consultar):

| Endpoint | Descrição |
|---|---|
| **Atualizar venda** | Recebe o **mesmo formato do create**, inclusive a lista de produtos com suas quantidades. |
| **Remover item** | Remove um produto (item) de uma venda. |
| **Finalizar venda** | Muda o status para `Finalizado`. |

Depois de **finalizada**, a venda **não pode mais ser alterada**: atualizar a venda ou remover item deve ser recusado.

---

## Módulo Relatórios

Os dois relatórios devem permitir filtrar por **período** (data inicial e data final).

### 1. Top 10 produtos vendidos

Retorna os 10 produtos mais vendidos no período. Deve ter uma opção para ranquear por:

- **quantidade** vendida; ou
- **valor** vendido.

### 2. Vendas com produtos (aglutinado por venda)

Lista as vendas do período. Cada venda mostra:

- **Dados da venda:** número, data, cliente, usuário, forma de pagamento e valor total.
- **Lista dos produtos vendidos nela:** descrição, quantidade, valor unitário e valor total do item.

---

## Entrega

- [ ] Link do repositório Git.
- [ ] Arquivo do banco SQLite com dados de exemplo.
- [ ] Collection do Postman.
- [ ] README com instruções de instalação e execução.

**Prazo:** _[definir]_

---

## Dúvidas

Dúvidas sobre o enunciado são bem-vindas. Pergunte sempre que algo não estiver claro.

Boa sorte! 🚀
