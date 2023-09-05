import mysql.connector
from datetime import datetime

###### CRUD QUERIES #######

sql_author_table = """
create table if not exists author(
    id int auto_increment primary key,
    name varchar(80)
);
"""

sql_post_table = """
create table if not exists post(
    id int auto_increment primary key,
    id_author int,
    title varchar(80),
    created datetime
);
"""

sql_select_author = """
select * from author;
"""

sql_select_post = """
select * from post;
"""
sql_select_post_author_id = """
select * from post where id_author = %s;
"""

sql_create_author = """
insert into author (name) values (%s);
"""

sql_create_post = """
insert into author (id_author, title, created) values (%s, %s, '%s');
"""

sql_update_author = """
update author set name = %s where id = %s;
"""

sql_update_post = """
update post set title = %s where id = %s;
"""

sql_delete_author = """
delete from author where id = %s;
"""

sql_update_post = """
delete from post where id = %s;
"""

#### Messages ####

help_msg = """Para efetuar uma operação digite `[COMANDO] [OBJETO]`, onde:
- Valores possíveis de `[COMANDO]`: 
    - `create`: Criar um objeto
    - `update`: Atualizar um objeto
    - `delete`: Deletar um objeto
    - `select`: Listar objetos
- Valores possíveis de `[OBJETO]`:
    - `author`: operar com objetos autores
    - `post`: operar com objetos posts de autores
Posts podem ser buscados também pelo ID do autor com o comando `select_by_author`
"""

exit_msg = "Finalizando..."

welcome_msg = "Digite `help` para listar os comandos disponíveis ou `exit` para sair"

###### SHELL #######
alive = True

print(welcome_msg)

while alive:
    cmd = input('> ')
    if cmd == "exit":
        print(exit_msg)
        alive = False
    elif cmd == "help":
        print(help_msg)
    else:
        print("COMANDO DESCONHECIDO")