import mysql.connector
from datetime import datetime

###### CRUD QUERIES #######

sql_course_table = """
create table if not exists course(
    course_id int auto_increment primary key,
    name varchar(80),
    study_area varchar(80)
);
"""

sql_student_table = """
create table if not exists student(
    student_id int auto_increment primary key,
    course_id int,
    name varchar(80),
    created datetime,
    age int,
    cpf varchar(11),
    foreign key (course_id) references course (course_id) on delete cascade
);
"""

sql_select_course = """
select * from course;
"""

sql_select_student = """
select * from student;
"""
sql_select_student_course_id = """
select * from student where course_id = %s;
"""

sql_create_course = """
insert into course (name, study_area) values (%s, %s);
"""

sql_create_student = """
insert into student (course_id, name, created, age, cpf) values (%s, %s, %s, %s, %s);
"""

sql_update_course = """
update course set name = %s, study_area = %s where course_id = %s;
"""

sql_update_student = """
update student set course_id = %s, name = %s, age = %s, cpf = %s where student_id = %s;
"""

sql_delete_course = """
delete from course where course_id = %s;
"""

sql_delete_student = """
delete from student where student_id = %s;
"""

#### Messages ####

help_msg = """Para efetuar uma operação digite `[COMANDO] [OBJETO]`, onde:
- Valores possíveis de `[COMANDO]`: 
    - `create`: Criar um objeto
    - `update`: Atualizar um objeto
    - `delete`: Deletar um objeto
    - `select`: Listar objetos
- Valores possíveis de `[OBJETO]`:
    - `course`: operar com objetos cursos
    - `student`: operar com objetos estudantes de cursos

Estudantes podem ser buscados também pelo ID do curso com a operação `select_by_course student`
Seleção de cursos com seus estudantes pode ser feita com a operação `select_detailed course`
"""

exit_msg = "Finalizando..."

welcome_msg = "Digite `help` para listar os comandos disponíveis ou `exit` para sair"

###### SHELL SETUP #######
alive = True

con = mysql.connector.connect(host='localhost', database='school', user='root', password='root')
# Run `create database if not exists school`

cursor = con.cursor()

cursor.execute(sql_course_table)
cursor.execute(sql_student_table)
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
        if obj == "course":
            name = input("Digite o nome do curso: ")
            study_area = input("Digite a área de estudo do curso: ")
            cursor.execute(sql_create_course, [name, study_area])
            con.commit()

            print(f"Curso `{name}` criado com sucesso")
        elif obj == "student":
            course_id = input("Digite o ID do curso que o aluno(a) participa: ")
            name = input("Digite o nome do estudante: ")
            age = int(input("Digite a idade do estudante: "))
            cpf = input("Digite o cpf do estudante: ")
            created = datetime.now()

            cursor.execute(sql_create_student, [course_id, name, created, age, cpf])
            con.commit()

            print(f"student `{name}` criado com sucesso")
        else:
            print("Objeto `", obj, "` desconhecido!")
    elif cmd == "select":
        if obj == "course":
            cursor.execute(sql_select_course)

            print("ID - Nome - Área de estudo")
            for row in cursor.fetchall():
                print(f"{row[0]} - {row[1]} - {row[2]}")
        elif obj == "student":
            cursor.execute(sql_select_student)
            
            print("ID Aluno - Nome Aluno - Idade - CPF - Data criação - ID curso")
            for row in cursor.fetchall():
                print(f"{row[0]} - {row[2]} - {row[4]} - {row[5]} - {row[3]} - {row[1]}")
        else:
            print(f"Objeto `{obj}` desconhecido!")
    elif cmd == "select_by_course":
        if obj == "student":
            id = input("Digite o ID do curso: ")
            cursor.execute(sql_select_student_course_id, [id])
            
            print("ID Aluno - Nome Aluno - Idade - CPF - Data criação - ID curso")
            for row in cursor.fetchall():
                print(f"{row[0]} - {row[2]} - {row[4]} - {row[5]} - {row[3]} - {row[1]}")
        else:
            print(f"Objeto `{obj}` desconhecido!")
    elif cmd == "update":
        if obj == "course":
            id = int(input("Digite o ID do curso: "))
            name = input("Digite o nome do curso: ")
            study_area = input("Digite a área de estudo do curso: ")
            cursor.execute(sql_update_course, [name, study_area, id])
            con.commit()

            print(f"Curso `{id}` atualizado com sucesso")
        elif obj == "student":
            id = int(input("Digite o ID do estudante: "))
            course_id = int(input("Digite o ID do curso que o aluno(a) trocou (se não escreva o que está agora): "))
            name = input("Digite o nome do estudante: ")
            age = int(input("Digite a idade do estudante: "))
            cpf = input("Digite o cpf do estudante: ")

            cursor.execute(sql_update_student, [course_id, name, age, cpf, id])

            print(f"Estudante `{id}` atualizado com sucesso")
        else:
            print("Objeto `", obj, "` desconhecido!")
    elif cmd == "delete":
        if obj == "course":
            id = input("Digite o ID do curso: ")
            cursor.execute(sql_delete_course, [id])
            con.commit()

            print(f"Curso `{id}` deletado com sucesso")
        elif obj == "student":
            id = input("Digite o ID do estudante: ")
            cursor.execute(sql_delete_student, [id])
            con.commit()

            print(f"Estudante `{id}` deletado com sucesso")
        else:
            print("Objeto `", obj, "` desconhecido!")
    elif cmd == "select_detailed":
        if obj == 'course':
            cursor.execute(sql_select_course)

            courses = cursor.fetchall()

            for course_row in courses:
                print(f"### Estudantes de \"{course_row[1]}\" (ID: {course_row[0]})")
                cursor.execute(sql_select_student_course_id, [course_row[0]])
                course_students = cursor.fetchall()
                for student_row in course_students:
                    print(f"- \"{student_row[2]}\", criado em {student_row[3]} (ID: {student_row[0]})")
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