# 我的博客

使用Typora+Bootstrap+Python(Beautifulsoup)搭建的超轻量级博客平台，用于github.io，支持自动生成主页信息。目前已弃用（因为不支持文章分类和排序）。

## 添加文章：

1. 在Typora里使用Markdown写新文章，然后使用Typora的导出功能导出为html文件，放在html文件夹下。
2. 将py文件夹下common.py文件里html变量的内容改成html刚才导出的html文件的路径，然后运行该脚本，格式化文章网页。
3. 修改py文件夹下的passages.json文件，依照其他文章的格式添加刚才书写的新文章的文件名（不包括后缀）、日期、摘要。
4. 运行py文件夹下的index.py生成主页。

## 添加随笔：

在html文件夹里的随笔.html文件进行修改，对于一行两张随笔卡片，html标签是这样定义的：

```html
        <div class="row mx-5 my-4">
            <div class="col m-1">
                <div class="card shadow h-100">
                    <h5 class="card-header">第一列标题</h5>
                    <div class="card-body">
                        <p class="card-text text-monospace alert alert-info">
                            代码
                        </p>
                        <p class="card-text">
                        第一列文字
                        </p>
                    </div>
                </div>
            </div>
            <div class="col m-1">
                <div class="card shadow h-100">
                    <h5 class="card-header">第二列标题</h5>
                    <div class="card-body">
                        <p class="card-text text-monospace alert alert-info">
                            代码
                        </p>
                        <p class="card-text">
                        第二列文字
                        </p>
                    </div>
                </div>
            </div>
        </div>
```

添加随笔时可按该格式自行添加标签。