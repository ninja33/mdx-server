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
            str_content += c.replace("\r\n","").replace("entry:/","").replace("sound:/","")

    injection = []
    injection_html = ''

    resource_path = os.path.join(sys.path[0], 'mdx')
    file_util_get_files(resource_path, injection)

    for p in injection:
        if file_util_is_ext(p, 'html'):
            injection_html += file_util_read_text(p)

    return [bytes(str_content + injection_html, encoding='utf-8')]


def get_definition_mdd(word, builder):
    """根据关键字得到MDX词典的媒体"""
    word = word.replace("/","\\")
    content = builder.mdd_lookup(word)
    if len(content) > 0:
        return [content[0]]
    else:
        return []