# -*- coding: utf-8 -*-
# version: python 3.5

import sys
from file_util import *

def get_definition_mdx(word, builder):
    """根据关键字得到MDX词典的解释"""
    content = builder.mdx_lookup(word)
    str_content = ""
    if len(content) > 0:
        for c in content:
            str_content += c.replace("\r\n","").replace("entry:/","")

    injection = []
    injection_html = ''
    output_html = ''

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        # base_path = sys._MEIPASS
        base_path = os.path.dirname(sys.executable)
    except Exception:
        base_path = os.path.abspath(".")
            
    resource_path = os.path.join(base_path, 'mdx')

    file_util_get_files(resource_path, injection)

    for p in injection:
        if file_util_is_ext(p, 'html'):
            injection_html += file_util_read_text(p)

    #return [bytes(str_content, encoding='utf-8')]
    output_html = str_content
    return [output_html.encode('utf-8')]

def get_definition_mdd(word, builder):
    """根据关键字得到MDX词典的媒体"""
    word = word.replace("/","\\")
    content = builder.mdd_lookup(word)
    if len(content) > 0:
        return [content[0]]
    else:
        return []
