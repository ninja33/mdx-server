##MDX Server

MDX Server is a service used to read MDX/MDD dictionary data and provide a standard HTTP interface to external tools.

It is just a combination of [mdict-query](https://github.com/mmjang/mdict-query) and [PythonDictionaryOnline](https://github.com/amazon200code/PythonDictionaryOnline).

Usage:

1. Run `mdx_server.py` under Python 3.5 environment. When it shows a dialoge window to ask for mdx file, you may select a mdx file located in your disk. After it displayed `port:8000` in console window, the service is running at beackground.
2. Open your browser and input http://localhost:8000/{word} (the {word} is the English word you want to query.), then the definition of that word will be displayed accoding to which dictionary(mdx file) you selected in above step 1.

Please check with the [manual](manual/mdx-server%20manual.pdf) for more detail and screenshot



##MDX Server使用说明

目前流行的MDX词典文件只能在Mdict, GoldenDict, 欧路，深蓝等词典软件中使用，而不能将内容对外输出。MDX Server通过读取MDX、MDD格式的词典文件，对外部提供一个标准的HTTP服务接口。使得一些需要词典服务的软件，比如Kindlemate，Anki划词助手以及其他工具可以利用这个本地服务，灵活选取所需的MDX词典，批量或者单独获取单词的解释。

1. 在python环境下运行`mdx_server.py`，弹窗内选择本地mdx文件，console窗口内显示`port:8000` 表明服务器运行成功，等待外部请求。
2. 在浏览器地址栏输入 http://localhost:8000/{word}，其中{word} 部分为待查的单词，比如http://localhost:8000/test ，通过mdx-server查询，浏览器内将显示该单词在第1步所选词典内的解释。

MDX Server 核心功能由 [mdict-query](https://github.com/mmjang/mdict-query) 和 [PythonDictionaryOnline](https://github.com/amazon200code/PythonDictionaryOnline) 整合而成.

更多内容和屏幕截图，请查阅[手册](manual/mdx-server%20manual.pdf)

