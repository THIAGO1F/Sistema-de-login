import PySimpleGUI as sg
from time import sleep
'''with open('usuarios.txt','a',newline='') as self.arquivo:
    self.arquivo.write(f'email:  {self.email}, senha: {senha} \n' )'''

'''with open('usuarios.txt','r') as arquivo:
        for linhas in arquivo:
            self.linha=linhas.split(',')[0]'''
#CLASS DO PROGRAMA
class syslogin():
    #MENU PRINCIPAL DO PORGRAMA
    def menu(self):
        sg.theme('black')#TealMono SystemDefault Material1
        layout = [[sg.Text('Usuário',size=(6,1)),sg.Input('',key='email'.strip())],
        [sg.Text('Senha',size=(6,1)),sg.Input('',key='senha',password_char="*".strip())],
        [sg.Text(' ')],
        [sg.Button('Login'),sg.Text('     '),sg.Button('Cadastrar'),sg.Text('     ') ,sg.Button('esqueci minha senha',button_color='red')],
        
        ]
        return sg.Window('login/cadastrar', layout=layout, finalize=True, size=(360,135))
    #MENU SECUNDÁRIO
    def menu2(self):
        sg.theme('black')
        menu_layout = [
        ['Menu',['Apagar Conta','Mudar E-mail','Mudar Senha','Mudar Usuário']],
        ]
        layou_frame = [
            [sg.Text('ola2')],
            [sg.Image('instagram.png')]
        ]
        layout = [[sg.Menu(menu_layout)],
            [sg.Frame('Coloque um nome aqui',layout=layou_frame,size=(498,498),key='frame')]
           
        ]
        return sg.Window('teste',layout=layout,size=(500,500),finalize=True)
    #MENU DE CONFIGURAÇÕES
    def menu_mudar_senha(self):
        layout = [
            [sg.Text('Mudar senha')],
            [sg.Text('Senha Antiga:',size=(10,1)),sg.Input('',key='antiga_senha')],
            [sg.Text('Senha Nova:',size=(10,1)),sg.Input('',key='nova_senha')],
            [sg.Text(' ')],
            [sg.Button('Confirmar'),sg.Text(' '),sg.Button('Cancelar')]
        ]
        return sg.Window('configurações',layout=layout,size=(300,155),finalize=True)
    
    def menu_mudar_email(self):
        layout = [
            [sg.Text('Mudar E-mail')],
            [sg.Text('E-mail Antigo:',size=(10,1)),sg.Input('',key='email_antigo')],
            [sg.Text('E-mail novo:',size=(10,1)),sg.Input('',key='email_novo')],
            [sg.Text(' ')],
            [sg.Button('Confirmar'),sg.Text(' '),sg.Button('Cancelar')]
        ]
        return sg.Window('configurações',layout=layout,size=(300,155),finalize=True)

    def menu_mudar_user(self):
        layout = [
            [sg.Text('Mudar Usuário')],
            [sg.Text('Usuário Antigo:',size=(10,1)),sg.Input('',key='user_antigo')],
            [sg.Text('Usuário novo:',size=(10,1)),sg.Input('',key='user_novo')],
            [sg.Text(' ')],
            [sg.Button('Confirmar'),sg.Text(' '),sg.Button('Cancelar')]
        ]
        return sg.Window('configurações',layout=layout,size=(300,155),finalize=True)

    def menu_apagar_conta(self):
        layout = [
            [sg.Text('Apagar Conta')],
            [sg.Text('Tem centeza que deseja apagar a conta?')],
            [sg.Text(' ')],
            [sg.Button('Confirmar',button_color='red'),sg.Text(' '),sg.Button('Cancelar')]
        ]
        return sg.Window('configurações',layout=layout,size=(270,140),finalize=True)

    #MENU DE RECUPERAÇÃO DE SENHA
    def recuperar_senha_menu(self):
        layout = [ 
            [sg.Text('Informe seu E-mail:'),sg.Input('',key='confirmar_email')],
            [sg.Text('Sua senha:'),sg.Text(' ',key='senharec')],
            [sg.Button('Confirmar'),sg.Button('Voltar')]
        ]
        return sg.Window('recuperar senha', layout=layout, size=(300,100),finalize=True)
    #MENU DE CADASTRO DE CONTA NOVA
    def menu_cadastrar(self):
        layout = [ 
            [sg.Text('Usuario:',size=(6,1)),sg.Input('',key='usuario_cadastrado')],
            [sg.Text('E-mail:',size=(6,1)),sg.Input('',key='email')],
            [sg.Text('Senha:',size=(6,1)),sg.Input('',key='senha',password_char="*")],
            [sg.Text(' ')],
            [sg.Button('Confirmar'),sg.Button('Voltar')]
        ]
        return sg.Window('Cadastrar', layout=layout, size=(300,160),finalize=True)

# FUNÇOES DO APLICATIVO 
    #FUNÇÃO MUDAR SENHA
    def mudar_senha(self):
        self.nova_senha = self.values['nova_senha']
        self.nova_senha = self.nova_senha.strip()
        antiga_senha = self.values['antiga_senha']
        with open('usuarios.txt','r') as arquivo:
            for linhas in arquivo:
                self.linha_user=linhas.split(',')[0].strip()
                self.linha_senha=linhas.split(',')[1].strip()
                self.linha_email=linhas.split(',')[2].strip()
                if self.nova_senha == '':
                    sg.popup('Senha Inválida tente novamente!!!')
                    continue
                if antiga_senha != self.linha_senha:
                    sg.popup('Senha antiga INVÁLIDA!!',button_color='red')
                    break
                if antiga_senha == self.linha_senha:
                    with open('usuarios.txt','w',newline='') as self.arquivo:
                        self.arquivo.write(f' {self.linha_user},{self.nova_senha},{self.linha_email}')
                        sg.popup('Senha alterada com sucesso!!',button_color='green')
                        sleep(0.5)
                        self.janela5.hide()
                        break

    def mudar_email(self):
        self.novo_email = self.values['email_novo']
        self.novo_email = self.novo_email.strip()
        antigo_email = self.values['email_antigo']
        with open('usuarios.txt','r') as arquivo:
            for linhas in arquivo:
                self.linha_user=linhas.split(',')[0].strip()
                self.linha_senha=linhas.split(',')[1].strip()
                self.linha_email=linhas.split(',')[2].strip()
                if self.novo_email == '':
                    sg.popup('Email Inválido tente novamente!!!')
                    continue
                if antigo_email != self.linha_email:
                    sg.popup('Email antigo INVÁLIDO!!',button_color='red')
                    break
                if antigo_email == self.linha_email:
                    with open('usuarios.txt','w',newline='') as self.arquivo:
                        self.arquivo.write(f' {self.linha_user},{self.linha_senha},{self.novo_email}')
                        sg.popup('Email alterado com sucesso!!',button_color='green')
                        sleep(0.5)
                        self.janela6.hide()
                        break
                        
    def mudar_usuario(self):
        self.novo_usuario = self.values['user_novo']
        self.novo_usuario = self.novo_usuario.strip()
        antigo_usuario = self.values['user_antigo']
        with open('usuarios.txt','r') as arquivo:
            for linhas in arquivo:
                self.linha_user=linhas.split(',')[0].strip()
                self.linha_senha=linhas.split(',')[1].strip()
                self.linha_email=linhas.split(',')[2].strip()
                if self.novo_usuario == '':
                    sg.popup('Usuário Inválido tente novamente!!!')
                    continue
                if antigo_usuario != self.linha_user:
                    sg.popup('Usuário antigo INVÁLIDO!!',button_color='red')
                    break
                if antigo_usuario == self.linha_user:
                    with open('usuarios.txt','w',newline='') as self.arquivo:
                        self.arquivo.write(f' {self.novo_usuario},{self.linha_senha},{self.linha_email}')
                        sg.popup('Usuário alterado com sucesso!!',button_color='green')
                        sleep(0.5)
                        self.janela7.hide()
                        break
        
    def ok_deleta(self):
        teste = sg.popup_ok_cancel('Tem certeza disso?',text_color='red')
        return teste

    def apagar_conta(self):
        if self.ok_deleta() == 'OK':
            with open('usuarios.txt','w',newline='') as self.arquivo:
                self.arquivo.write(' ')
                sg.popup('Conta deletada com sucesso!!',button_color='green')
                sleep(0.5)
                self.janela8.hide()
                self.janela2.hide()
                self. janela1.un_hide()
        
        else:
            sg.popup('Otima decisão',button_color='green')
            
            self.janela8.hide()
      
    #FUNÇÃO PARA CRIAR A CONTA
    def criarlogin(self):
        

        user = self.values['usuario_cadastrado']
        user = user.strip()
        self.senha = self.values['senha']
        self.senha = self.senha.strip()
        self.email = self.values['email']
        self.email = self.email.strip()
        if user == '':
            sg.popup('Usuário Inválido tente novamente!!',button_color='red')
        elif self.email == '':
            sg.popup('Email Inválido tente novamente!!',button_color='red')
        elif not '@gmail.com' in self.email:
            sg.popup('Email Inválido tente novamente!!',button_color='red')
        
        
        elif self.senha == '':
            sg.popup('Senha Inválida tente novamente!!',button_color='red')  
        else:
        
            with open('usuarios.txt','a',newline='') as self.arquivo:
                self.arquivo.write(f'{user},{self.senha},{self.email}')
                sg.popup('Conta criada com sucesso!',button_color='green')
                self.janela4.hide()
                self.janela1.un_hide()
    #FUNÇÃO DE ENTRAR NA CONTA/VERIFICAR SE EMAIL E SENNHA SÃO COMPATIVEIS
    def login(self):
        self.email = self.values['email']
        senha = self.values['senha']
        with open('usuarios.txt','r') as arquivo:
            for linhas in arquivo:
                if linhas == ' ':
                    sg.popup('Você não possui uma conta',button_color='red')
                    break
                self.email_arquivo=linhas.split(',')[0].strip()
                self.senha_arquivo = linhas.split(',')[1]
                if self.email == self.email_arquivo:
                    if senha == self.senha_arquivo:
                        print('senha correta')
                    if senha != self.senha_arquivo:
                        print('senha incorreta')
                        print(self.senha_arquivo)
                        sg.popup('Senha Incorreta',text_color="red",button_color="red",background_color="black")

                if senha == self.senha_arquivo:
                    if self.email == self.email_arquivo:
                        print('email correto')
                        self.janela1.hide()
                        self.janela2 = self.menu2()
                    if self.email != self.email_arquivo:
                        print('email incorreto')
                        sg.popup('Usuário Inválido!',text_color="red",button_color="red",background_color="black")

                if senha != self.senha_arquivo:
                    if self.email != self.email_arquivo:
                        sg.popup('Usuário e Senha invalidos!',text_color='red',button_color="red",background_color="black")
    #FUNÇÃO QUE VERIFICA SE TEM UMA CONTA              
    def verifica_login(self):
                    
        with open('usuarios.txt','r') as arquivo:
            for linhas in arquivo:
                if linhas == ' ':
                    print('criando conta')
                    self.janela1.hide()
                    self.janela4 = self.menu_cadastrar()
                    
                    break
                if linhas != ' ':
                    print('contas ja criadas')
                    sg.popup('Já existe uma conta criada!!',button_color='red')
    #FUNÇÃO PARA VERIFICAR E RECUPERAR A SENHA        
    def recupera_senha(self):

        confirmar_email = self.values['confirmar_email']
        with open('usuarios.txt','r') as arquivo:
            for linhas in arquivo:
                if linhas == ' ':
                    sg.popup('Você não possui uma conta',button_color='red')
                    break
                self.linha=linhas.split(',')[2]
                
                if self.linha == confirmar_email:
                    sg.popup('Email confirmado!',button_color='green')
                    with open('usuarios.txt','r') as arquivo:
                        for linhas in arquivo:
                            self.senha = linhas.split(',')[1]
                            print(self.senha)
                            self.window['senharec'].update(value=self.senha)    
                if self.linha != confirmar_email:
                    sg.popup('Email não encontrado! \nInforme um Email válido',button_color='red')
    #FUNÇÃO DE INICIAR O PROGRAMA
    def start(self):
        self.janela1, self.janela2, self.janela3, self.janela4, self.janela5, self.janela6, self.janela7, self.janela8= self.menu(), None, None, None, None, None, None, None
        while True:
            self.window, event, self.values = sg.read_all_windows()
            #CONFIGURAÇÃO PARA FECHAR A JANELA NO BOTAO X OU CANCELAR
            if self.window == self.janela1 and event == sg.WIN_CLOSED or event == 'CANCELAR':
                break
            if self.window == self.janela2 and event == sg.WIN_CLOSED or event == 'CANCELAR':
                break
            if self.window == self.janela3 and event == sg.WIN_CLOSED or event == 'CANCELAR':
                break
            if self.window == self.janela4 and event == sg.WIN_CLOSED or event == 'CANCELAR':
                break
            if self.window == self.janela5 and event == sg.WIN_CLOSED :
                self.janela5.hide()
                continue
            if self.window == self.janela6 and event == sg.WIN_CLOSED :
                self.janela6.hide()
                continue
            if self.window == self.janela7 and event == sg.WIN_CLOSED :
                self.janela7.hide()
                continue
            if self.window == self.janela8 and event == sg.WIN_CLOSED :
                self.janela8.hide()
                continue
            #EVENTOS DA JANELA1
            if self.window == self.janela1 and event in "Login":
                
                self.login()
            if self.window == self.janela1 and event in "Cadastrar":
                self.verifica_login()
            if self.window == self.janela1 and event in "esqueci minha senha":
                self.janela1.hide()
                self.janela3 = self.recuperar_senha_menu()

            #EVENTOS DA JANELA2
            if self.window == self.janela2:
                if event in 'Mudar Senha':
                    self.janela5 = self.menu_mudar_senha()
                if event in 'Mudar E-mail':
                    self.janela6 = self.menu_mudar_email()
                if event in 'Mudar Usuário':
                    self.janela7 = self.menu_mudar_user()
                if event in 'Apagar Conta':
                    self.janela8 = self.menu_apagar_conta()

            #EVENTOS DA JANELA3
            if self.window == self.janela3 and event in 'Confirmar':
                self.recupera_senha()
            if self.window == self.janela3 and event in 'Voltar':
                self.janela3.hide()
                self.janela1.un_hide()  
            
            #EVENTOS DA JANELA4
            if self.window == self.janela4 and event in 'Confirmar':
                self.criarlogin()
            if self.window == self.janela4 and event in 'Voltar':
                self.janela4.hide()
                self.janela1.un_hide()
               
            #EVENTOS JANELA5 MUDAR SENHA
            if self.window == self.janela5:
                if event in 'Confirmar':
                    self.mudar_senha()
                if event in 'Cancelar':
                    self.janela5.hide()
                    self.janela2.un_hide()
            
            #EVENTOS JANELA6 MUDAR EMAIL
            if self.window == self.janela6:
                if event in 'Confirmar':
                    self.mudar_email()
                if event in 'Cancelar':
                    self.janela6.hide()
                    self.janela2.un_hide()

            #EVENTOS JANELA7 MUDAR USUARIO
            if self.window == self.janela7:
                if event in 'Confirmar':
                    self.mudar_usuario()
                if event in 'Cancelar':
                    self.janela7.hide()
                    self.janela2.un_hide()
            
            #EVENTOS JANELA8 APAGAR CONTA
            if self.window == self.janela8:
                if event in 'Confirmar':
                    self.apagar_conta()
                if event in 'Cancelar':
                    self.janela8.hide()
                    self.janela2.un_hide()
            
#INICIANDO A CLASS
syslogin().start()