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
insert into post (id_author, title, created) values (%s, %s, %s);
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

sql_delete_post = """
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

Posts podem ser buscados também pelo ID do autor com o comando `select_by_author`"""

exit_msg = "Finalizando..."

welcome_msg = "Digite `help` para listar os comandos disponíveis ou `exit` para sair"

###### SHELL SETUP #######
alive = True

con = mysql.connector.connect(host='localhost', database='blog', user='root', password='root')
# Run `create database if not exists blog`

cursor = con.cursor()

cursor.execute(sql_author_table)
cursor.execute(sql_post_table)
con.commit()

print(welcome_msg)

###### SHELL LOOP #######

while alive:
    usr_input = input('> ').split(" ")
    
    cmd = usr_input[0]
    obj = ""
    if len(usr_input) > 1:
        obj = usr_input[1]

    if cmd == "create":
        if obj == "author":
            name = input("Digite o nome do autor: ")
            cursor.execute(sql_create_author,[name])
            con.commit()

            print(f"Autor `{name}` criado com sucesso")
        elif obj == "post":
            author_id = input("Digite o ID do autor: ")
            title = input("Digite o título do post: ")
            created = datetime.now()
            cursor.execute(sql_create_post, [author_id, title, created])
            con.commit()

            print(f"Post `{title}` criado com sucesso")
        else:
            print("Objeto `", obj, "` desconhecido!")
    elif cmd == "select":
        if obj == "author":
            cursor.execute(sql_select_author)

            print("ID - Nome")
            for row in cursor.fetchall():
                print(f"{row[0]} - {row[1]}")
        elif obj == "post":
            cursor.execute(sql_select_post)
            
            print("ID - ID Autor - Titulo - Data criacao")
            for row in cursor.fetchall():
                print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")
        else:
            print(f"Objeto `{obj}` desconhecido!")
    elif cmd == "select_by_author":
        if obj == "post":
            id = input("Digite o ID do autor: ")
            cursor.execute(sql_select_post_author_id, [id])
            
            print("ID - ID Autor - Titulo - Data criacao")
            for row in cursor.fetchall():
                print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")
        else:
            print(f"Objeto `{obj}` desconhecido!")
    elif cmd == "update":
        if obj == "author":
            id = input("Digite o ID do autor: ")
            name = input("Digite o novo nome do autor: ")
            cursor.execute(sql_update_author, [name, id])
            con.commit()

            print(f"Autor `{id}` atualizado com sucesso")
        elif obj == "post":
            id = input("Digite o ID do post: ")
            title = input("Digite o novo título do post: ")
            cursor.execute(sql_update_post, [title, id])
            con.commit()

            print(f"Post `{id}` atualizado com sucesso")
        else:
            print("Objeto `", obj, "` desconhecido!")
    elif cmd == "delete":
        if obj == "author":
            id = input("Digite o ID do autor: ")
            cursor.execute(sql_delete_author, [id])
            con.commit()

            print(f"Autor `{id}` deletado com sucesso")
        elif obj == "post":
            id = input("Digite o ID do post: ")
            cursor.execute(sql_delete_post, [id])
            con.commit()

            print(f"Post `{id}` deletado com sucesso")
        else:
            print("Objeto `", obj, "` desconhecido!")
    elif cmd == "exit":
        print(exit_msg)
        alive = False
    elif cmd == "help":
        print(help_msg)
    else:
        print(f"Comando `{cmd}` desconhecido!")
        print(welcome_msg)