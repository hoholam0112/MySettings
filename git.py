import subprocess

def main():
    subprocess.call('sudo git config --global core.editor \'vim\'', shell=True)


if __name__ == '__main__':
    main()
