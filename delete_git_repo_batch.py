from time import sleep
import requests
## 1. 批量获取所有的仓库列表
## 2. 调用GIT API删除仓库

#所需参数： 
# 1.你的github用户名;
# 2.token（需要设置有删除权限）

# 通过浏览器运行，获取内容，并粘贴到下方source_files : 
# https://api.github.com/users/你的github用户名/repos?page=1&per_page=100
source_files = [
  {
    "id": 166344216,
    "node_id": "MDEwOlJlcG9zaXRvcnkxNjYzNDQyMTY=",
    "name": "warp-ctc",
    "full_name": "liyupeng-ing/warp-ctc",
    "private": 1,
    "owner": "xxx"
  }
]

data = []
for context in source_files:
    data.append(context['full_name'])
print("-----")
print(data)

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token xxx", # XXX代表token
    "X-OAuth-Scopes": "repo"
}

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    name, repo = line.strip().split("/")
    urls.append(url.format(name, repo))

for l in urls:
    requests.delete(url=l, headers=headers)
    print(l)
    sleep(2)
