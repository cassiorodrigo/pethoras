import os

import MySQLdb
import sshtunnel
senhadb = os.getenv('SENHADB')

class Conexao:
    def connectar(self):
        sshtunnel.SSH_TIMEOUT = 5.0
        sshtunnel.TUNNEL_TIMEOUT = 5.0

        with sshtunnel.SSHTunnelForwarder(
            ('ssh.pythonanywhere.com'),
            ssh_username='PetPark', ssh_password=senhadb,
            remote_bind_address=('PetPark.mysql.pythonanywhere-services.com', 3306)
        ) as tunnel:
            connection = MySQLdb.connect(
                user='PetPark',
                passwd=senhadb,
                host='127.0.0.1', port=tunnel.local_bind_port,
                db='PetPark$horas_trabalhadas',
            )
            connection.close()
            return True

    def CREATEDB(self):
        criar_comando = '''
        CREATE TABLE IF NOT EXISTS horas(
        _ID PRIMARY KEY AUTOINCREMENT,
        firstname VARCHAR(100),
        lastname VARCHAR(100),
        entrada DATETIME(6),
        saida DATETIME(6),
        UNIQUE KEY (firstname, lastname, entrada));
        
        CREATE TABLE IF NOT EXISTS usuario(
        _ID PRIMARY KEY AUTOINCREMENT,
        firstname VARCHAR(100),
        lastname VARCHAR(100),
        email VARCHAR(255),
        UNIQUE KEY(email));
        
        CREATE TABLE IF NOT EXISTS senha(
        _ID PRIMARY KEY AUTOINCREMENT,
        senha VARCHAR(255) NOT NULL);
        '''
        return criar_comando

    def ENTRADA(self, usuario, senha, horaentrada):
        pass

    def UPDATE_SAIDA(self, usuario, senha, horasaida):
        pass


if __name__ == "__main__":
    conexao = Conexao()
    conn = conexao.connectar()