# -*- coding: utf-8 -*-
# version: python 3.5
import os
import io

def file_util_readlines_text(path):
    """读取文本文件返回各行list"""
    with io.open(path, 'r', -1, 'utf-8') as f:
        file_rst = f.readlines()
    return file_rst


def file_util_readlines_text_strip(path):
    """读取文本文件并去除空白返回各行list"""
    with io.open(path, 'r', -1, 'utf-8') as f:
        file_rst = []
        for line in f:
            file_rst.append(line.strip())
    return file_rst


def file_util_read_text(path):
    """读取文本文件返回str"""
    with io.open(path, 'r', -1, 'utf-8') as f:
        file_rst = ''
        for line in f:
            file_rst += line
    return file_rst


def file_util_write_text(path, text):
    """写入文本文件"""
    with io.open(path, 'w', -1, 'utf-8') as f:
        f.write(text)


def file_util_read_byte(path):
    """读取二进制文件（byte）"""
    with io.open(path, 'br') as f:
        rst_bytes = b''
        for line in f:
            rst_bytes += line
    return rst_bytes


def file_util_get_ext(path):
    """得到文件后缀（不包含点）"""
    return os.path.splitext(path)[1][1:]


def file_util_get_filename(path):
    """得到路径文件名字"""
    return os.path.basename(path)


def file_util_is_ext(path, ext):
    """判断是否指定后缀文件,ext不包含点"""
    if file_util_get_ext(path) == ext:
        return True
    else:
        return False


def file_util_get_files(root_dir, result_list):
    """得到指定路径所有文件"""
    #print(root_dir)
    if file_util_is_exists(root_dir):
        for lists in os.listdir(root_dir):
            path = os.path.join(root_dir, lists)
            if os.path.isdir(path):
                file_util_get_files(path, result_list)
            if os.path.isfile(path):
                result_list.append(path)
    else:
        print("path [ "+ root_dir +" ] does not exist")

def file_util_is_exists(path):
    """判断文件或目录是否存在"""
    return os.path.exists(path)


def file_util_del_file(path):
    """删除文件"""
    if file_util_is_exists(path):
        os.remove(path)


def file_util_del_dir_ext_file(path, ext):
    """删除所有指定目录下指定后缀（不加点）文件"""
    if (path is None) or (len(path.strip()) <= 0):
        return
    if (ext is None) or (len(ext.strip()) <= 0):
        return
    all_file = []
    file_util_get_files(path, all_file)
    for f in all_file:
        if file_util_is_ext(f, ext):
            file_util_del_file(f)
