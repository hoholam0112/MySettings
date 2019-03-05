import subprocess

def main():
    subprocess.call('sudo git config --global core.editor \'vim\'', shell=True)
    subprocess.call('sudo git config --global user.email \'hoholam0112@gmail.com\'', shell=True)
    subprocess.call('sudo git config --global user.name \'hoholam0112\'', shell=True)

if __name__ == '__main__':
    main()
