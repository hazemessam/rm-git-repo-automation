from github import Github
from dotenv import load_dotenv
from os import getenv

load_dotenv()
username =  getenv('gitusername')
password =  getenv('gitpassword')

file = open('reposlist.txt', 'a')

gitCon = Github(username, password)
gitUser = gitCon.get_user()
gitRepos = gitUser.get_repos()
for repo in gitRepos:
    file.write(f'{repo.full_name}\n')
