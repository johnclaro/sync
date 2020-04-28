import os
import subprocess
from shutil import copyfile

from github import Github

USERNAME = ''
PASSWORD = ''

g = Github(USERNAME, PASSWORD)
for repo in g.get_user().get_repos():
    domain = f'https://github.com/{USERNAME}/{repo.name}.git'
    subprocess.run(['git', 'clone', '--bare', domain])
    copyfile('emailChanger.sh', f'{repo.name}.git/emailChanger.sh')
    os.chmod(f'{repo.name}.git/emailChanger.sh', 777)
    subprocess.call('sh emailChanger.sh', cwd=f'{repo.name}.git', shell=True)
    subprocess.call(["git push --force --tags origin 'refs/heads/*'"], cwd=f'{repo.name}.git', shell=True)
    subprocess.run(['rm', '-rf', f'{repo.name}.git'])
