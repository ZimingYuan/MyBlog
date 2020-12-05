import json
from bs4 import BeautifulSoup

perpage = 8

f = open('passages.json', 'r', encoding='utf-8')
data = json.loads(f.read())
f.close()
total = (len(data) + perpage - 1) // perpage
url = ['/index.html']
for i in range(1, total):
    url.append(f'/index/{i + 1}.html')
f = open('index.temp', 'r', encoding='utf-8')
soup = BeautifulSoup(f.read(), 'lxml')
f.close()
title = soup.find('title')
bloglist = soup.find('div', id='Bloglist')
for page in range(total):
    title.string = f'ZimingYuan的博客首页（第{page + 1}页）'
    slic = data[page * perpage:min((page + 1) * perpage, len(data))]
    bloglist.clear()
    for i in slic:
        card = BeautifulSoup('''
<div class="card shadow mb-4">
    <h5 class="card-header">
        <a href=""></a>
    </h5>
    <div class="card-body">
        <h5 class="card-title">摘要：</h5>
        <p class="card-text"></p>
        <h6 class="card-subtitle text-muted text-right"></h6>
    </div>
</div>
''', 'html.parser')
        a = card.find('a')
        a['href'] = f'/html/{i["name"]}.html'
        a.string = i['name']
        card.find('p').string = i['abstract']
        card.find('h6').string = i['date']
        bloglist.append(card)
    pagination = BeautifulSoup('''
<ul class="pagination justify-content-center">
    <li class="page-item" id="previous">
        <a class="page-link" href="">上一页</a>
    </li>
    <li class="page-item" id="next">
        <a class="page-link" href="">下一页</a>
    </li>
</ul>
''', 'html.parser');
    if page == 0:
        pagination.find('li', id='previous')['class'].append('disabled')
    else:
        pagination.find_all('a')[0]['href'] = url[page - 1]
    if page == total - 1:
        pagination.find('li', id='next')['class'].append('disabled')
    else:
        pagination.find_all('a')[1]['href'] = url[page + 1]
    nex = pagination.find('li', id='next')
    for i in range(total):
        li = soup.new_tag('li')
        li['class'] = ['page-item'] + ['active'] if i == page else []
        li.append(BeautifulSoup(f'<a class="page-link" href="{url[i]}">{i + 1}</a>', 'html.parser'))
        nex.insert_before(li)
    bloglist.append(pagination)
    f = open('..' + url[page], 'w', encoding='utf-8')
    f.write(str(soup))
    f.close()
