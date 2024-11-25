# Gestão de Stock

Este é um sistema desenvolvido para auxiliar a gestão de estoque de materiais e equipamentos de construção civil, focado nas necessidades da empresa *Silvano Construção e Aluguer de Equipamentos*. Ele permite o controle e monitoramento de produtos, incluindo prumos, tábuas, vigas, chapas e blocos, além de gerenciar valores de aluguel e transporte.

## Funcionalidades Principais

- **Gestão de Produtos**:
  - Cadastro, edição, exclusão e visualização de produtos.
  - Controle de atributos como preço, estoque, código NCM e status de importação.

- **Gestão de Estoque**:
  - Controle de entradas e saídas de materiais.
  - Cálculo automático de saldo em estoque.

- **Relatórios e Dashboards**:
  - Visualização de relatórios detalhados sobre estoque, vendas e alugueis.
  - Gráficos dinâmicos para análise de dados.

- **Controle de Usuários**:
  - Perfis para administradores, gerentes e clientes.
  - Permissões diferenciadas para cada tipo de usuário.

- **Integração com APIs**:
  - Futuro suporte para integração com serviços de transporte e pagamento.

## Tecnologias Utilizadas

- **Backend**:
  - Django 5.1.2
  - Python 3.8

- **Frontend**:
  - Bootstrap 4 para estilização responsiva.
  - Jinja2 para renderização de templates.

- **Banco de Dados**:
  - SQLite (desenvolvimento).
  - PostgreSQL (recomendação para produção).

- **Outros Pacotes**:
  - `django-extensions`, `django-bootstrap-form`, `django-widget-tweaks`

- **Integrações Futuras**:
  - Firebase para notificações e armazenamento.

## Estrutura do Projeto

O projeto segue uma estrutura padrão do Django, com aplicações separadas para diferentes funcionalidades:

- **Core**: Configurações e arquivos principais.
- **Produto**: Modelos e funcionalidades para gestão de produtos.
- **Estoque**: Lógica para controle de entradas e saídas.

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```bash
git clone git@github.com:SilverPro17/Gestao_Stock.git
cd 
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Links

[python-decouple](https://github.com/henriquebastos/python-decouple)

[package-of-the-week-python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)

[github.com/rg3915/tutoriais django-basic](https://github.com/rg3915/tutoriais/tree/master/django-basic)

[bootstrap starter-template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)

[emmet](https://emmet.io/)

[start.html](https://github.com/JTruax/bootstrap-starter-template/blob/master/template/start.html)

[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

[Class Based View - ccbv.co.uk](https://ccbv.co.uk/)

[form-inline](http://felipefrizzo.github.io/post/form-inline/)

[form-inline-cbv](http://felipefrizzo.github.io/post/form-inline-cbv/)

[django-bootstrap-form](https://django-bootstrap-form.readthedocs.io/en/latest/)

[Paginação - gist](https://gist.github.com/rg3915/01ca76f099f431c24bc0536bef83076b)

[Paginação - Bootstrap](https://getbootstrap.com/docs/4.3/components/pagination/)
