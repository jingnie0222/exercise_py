#!/usr/bin/python
#encoding=utf-8

import urllib
import sys
import requests
import codecs

MANUAL_QUERY_FILENAME = "/search/yinjingjing/manual_db/manual_query_file"

#add % for log,transfer to unicode

def translate_key_to_query(key_string):
    parse_string = ""
    key_len = len(key_string)

    while (key_len > 0):
        parse_string += "%" + key_string[0:2]
        key_string = key_string[2:]
        key_len = key_len - 2

    #transfer to chinese query
    query = urllib.unquote(parse_string)
    return query

def get_key_from_log(logfile):
    lists = []

    with open(logfile, 'r') as f:
        for line in f.readlines():
            if "cmd=PUT" not in line:
                continue
            line = line.rstrip('\n')
            #extract key from line
            line = line.split(',')[7][4:-1]
            lists.append(line)

    f_query = open(MANUAL_QUERY_FILENAME, 'w')
    for i in range(len(lists)):
        temp_key = translate_key_to_query(lists[i])
        if "SELECT" in temp_key:
            continue
        f_query.write("%s\n" % temp_key.decode('gbk').encode('utf-8'))

    f_query.close()

if __name__ == '__main__':
    get_key_from_log(sys.argv[1])
