import os
import pandas as pd
import paramiko


# create ssh client
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "host adress"
username = "username"
password = "password"
port = 22

# paths
path_download = "path in my server"
path_remote = "path in remote server"
archivo_completo = "completo.csv"
archivo_download = "jornadas.csv"


def download_file():
    """
    executes connection and download csv file
    """
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    ftp = ssh_client.open_sftp()
    files = ftp.get(remotepath=path_remote, localpath=path_download + archivo_download)

    # close the connection
    ftp.close()
    ssh_client.close()


def copy_file():
    """
    copy jornadas file to complete csv file
    """
    os.chdir(path_download)
    datos_a_copiar = pd.read_csv(archivo_download, on_bad_lines='skip')
    datos_a_copiar.to_csv(archivo_completo, index=None, mode="a",header=not os.path.isfile(archivo_completo))


if __name__ == '__main__':
    download_file()
    copy_file()
