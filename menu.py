import psycopg2
from connection import Connection

#---------------------------------------------------
#Menu de print
def print_menu():

    option = int(input("Choose the option:\n1- INSERT\n2- SELECT\n3- UPDATE\n4- DELETE\n0- EXIT\n>> "))
    executa_operacao(option)

#---------------------------------------------------
#Pegar dados separados
"""
def get_nome():

    nome = input("Digite o nome: ")
    
def get_cpf():

    cpf = input("Digite o CPF: ")

def get_email():

    email = input("Digite o email: ")

#---------------------------------------------------
#Validar CPF
def validate_cpf(cpf_on):
    #cpf existente no banco ou nao
    @validate_cpf
    def exist_cpf (self, cpf_on):

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM pessoa WHERE cpf = '{0}'".format(cpf_on))
        #Se a query retornar maior que zero, você retorna a mensagem pro cliente dizendo que ja existe cpf
        if cur.execute > 0:
            situation_cpf = 1
            print("CPF ja cadastrado, favor inserir novamente.")
            conn.close()
            print_menu()
        else:
            situation_cpf = 0
            
        conn.close()
        #se existir, retorna 1, senao 0
        return situation_cpf

        exist_cpf_here = exist_cpf(cpf_on)
        

        if cpf_on.isdigit() == True and (len(cpf_on) == 11):
            return 1
        else:
            return 0

    @validate_cpf
    def is_number(self, cpf_on):
        if not cpf_on.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():
            return False
        try:
            float(cpf_on)
        except ValueError:
            return False
        return True
    
    exist_cpf(cpf_on)
    is_number(cpf_on)
    
#---------------------------------------------------
#Validar NOME
def validate_nome(nome_on):
    #somente letras
    if nome_on.isalpha() == True and (len(nome_on) <= 150):
        return 1
    else:
        return 0

#---------------------------------------------------
#Validar EMAIL
def validate_email(email_on):
    #somente letras
    if (len(email_on) <= 400):
        return 1
    else:
        return 0
"""
#---------------------------------------------------
#Menu de Operacoes Principal
def executa_operacao(opcao):

    #---------------------------------------------------
    #Menu de Operacoes Principal - INSERT
    if opcao == 1:
        #INSERT

        cpf = input("Digite o CPF: ")

        nome = input("Digite o nome: ")
    
        email = input("Digite o email: ")

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute ("insert into pessoa (nome, cpf, email, situacao)\
                    values ('{0}','{1}','{2}', '1')".format(nome, cpf, email))

        conn.commit()
        conn.close()

        print_menu()

    #-------------------------------------------------------
    #Menu de Operacoes Principal - SELECT
    elif opcao == 2:
        #SELECT

        option_on = int(input("Insert option:\n1- View all\n2- CPF Search\n3- EMAIL Search\n4- EXIT\n>> "))

        if option_on == 1:
            #View all
            conn = Connection().get_connection()

            cur = conn.cursor()
            cur.execute("select * from pessoa where situacao = '1'")

            rows = cur.fetchall()

            for row in rows:
                print(row[0],str(row[1]),row[2],row[3])

            conn.close()
            print_menu()

        #---------------------------   
        elif option_on == 2:
            #CPF
            cpf = input("Insert the CPF: ")

            conn = Connection().get_connection()

            cur = conn.cursor()
            cur.execute("select * from pessoa where situacao = '1' AND cpf = '{0}'".format(cpf))

            conn.close()
            print_menu()

        #--------------------------- 
        elif option_on == 3:
            #EMAIL

            email = input("Insert the email: ")

            conn = Connection().get_connection()

            cur = conn.cursor()
            cur.execute("select * from pessoa where situacao = '1' AND email = '{0}'".format(email))

            conn.close()
            print_menu()

        #--------------------------- 
        elif option_on == 4:
            #EXIT
            print("Bye bye...")
            print_menu()
     
        #--------------------------- 
        else:
            print("Wrong way")
            print_menu()


    #-------------------------------------------------------
    #Menu de Operacoes Principal - UPDATE
    elif opcao == 3:
        #UPDATE

        option_on = int(input("Insert option:\n1- Update NAME\n2- Update EMAIL\n3- EXIT\n>> "))

        if option_on == 1:
            cpf = input("Insert the cpf to search...")
            nome = input("Insert the name: ")

            conn = Connection().get_connection()

            cur = conn.cursor()
            cur.execute("Update pessoa set nome = '{0}' WHERE cpf = '{1}'".format(nome, cpf))
            conn.commit()
            conn.close()

        elif option_on == 2:
            cpf = input("Insert the cpf to search...")
            email = input("Insert the email: ")

            conn = Connection().get_connection()

            cur = conn.cursor()
            cur.execute("Update pessoa set nome = '{0}' WHERE cpf = '{1}'".format(email, cpf))
            conn.commit()
            conn.close()

        elif option_on == 3:
            print_menu()

        else:
            print("Wrong way")
            print_menu()

    #-------------------------------------------------------
    #Menu de Operacoes Principal - DELETE
    elif opcao == 4:
        #DELETE
        
        cpf = input("Insert the CPF: ")

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("Update pessoa set situacao = 0 WHERE cpf = '{0}'".format(cpf))
        conn.commit()

        conn.close()
        print_menu()

    #-------------------------------------------------------
    #Menu de Operacoes Principal - EXIT
    elif opcao == 0:
        #EXIT
        option_on = int(input("Insert option:\n1- Keep ON\n2- EXIT NOW\n>> "))
        
        if option_on == 1:
            print_menu()

        elif option_on == 2:
            print("Cya")
            exit()
        else:
            print("Wrong way")
            print_menu()
    #-------------------------------------------------------
    #Menu de Operacoes Principal - WRONG OPTION
    else:
        print("Wrong way")
        print_menu()

#---------------------------------------------------