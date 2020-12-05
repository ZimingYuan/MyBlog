from bs4 import BeautifulSoup

html = '..\\html\\快速生成网络mp4视频缩略图技术.html'
f = open(html, 'r', encoding='utf-8')
soup = BeautifulSoup(f.read(), 'lxml')
f.close()
head = soup.find('title')
head.insert_before(BeautifulSoup('''
<link rel="stylesheet" href="https://cdn.bootcss.com/twitter-bootstrap/4.1.0/css/bootstrap.min.css">
<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
<script src="https://cdn.bootcss.com/popper.js/1.12.9/popper.min.js" ></script>
<script src="https://cdn.bootcss.com/twitter-bootstrap/4.1.0/js/bootstrap.min.js" ></script>
<link rel="icon" href="/img/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" href="/img/favicon.ico" type="image/x-icon" />
''', 'html.parser'))
body = soup.find('body')
del body['class']
body.insert(0, BeautifulSoup('''
<nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
    <div class="container">
        <a class="navbar-brand" href="#">ZimingYuan的博客</a>
        <div class="navbar-collapse">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="/index.html">首页</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="/html/随笔.html">随笔</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="https://github.com/ZimingYuan" target="_Blank">GitHub</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
''', 'html.parser'))
body.append(BeautifulSoup('''
<span class="bg-light text-muted border boder-primary d-block p-2 text-center">
    转载请注明出处<br></br>
    © 2020 ZimingYuan的博客
</span>
<div style="background-color: #ebd5a1; position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999; pointer-events: none; opacity: 0.2;">
</div>
''', 'html.parser'))
f = open(html, 'w', encoding='utf-8')
f.write(str(soup))
f.close()
