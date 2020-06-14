from github import Github
from getpass import getpass
from os import remove, system

username = input('> Username: ')
password = getpass('> Password: ')

file = open('reposlist.txt', 'w')

try:    
    gitCon = Github(username, password)
    gitUser = gitCon.get_user()
    gitRepos = gitUser.get_repos()
    for repo in gitRepos:
        file.write(f'{repo.full_name}\n')
    file.close()
    system('reposlist.txt')
except Exception as e:
    print(e)
    file.close()
    remove('reposlist.txt')
    

