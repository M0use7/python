"""__author__ = 唐宏进 """
import json


def write_json_file(file_name,content):
    """
    将内容写入json文件中
    :param file_name:文件名
    :param content:要写的内容
    :return:是否写入成功
    """
    try:
        with open('./files/'+file_name, 'w', encoding='utf-8') as f:
            json.dump(content,f,ensure_ascii=False,indent=4)
            return True
    except:
        return False


def read_json_file(file_name):
    """
    获取json文件的内容
    :param file_name: 文件名
    :return:
    """
    try:
        with open('./files/'+file_name, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('文件不存在！')
        return None
    except json.decoder.JSONDecodeError:
        return None

def read_text_file(file_name):
    """
    获取文本文件的内容
    :param file_name: 文件名
    :return:
    """
    try:
        with open('./files/'+file_name, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('文件不存在！')
        return None

