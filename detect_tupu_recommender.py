#!/usr/bin/python3
#-*-coding=utf8-*-

import requests
import time
import os,sys


loc_lst = ['djt', '1.djt', 'tc', 'gd', '1.gd', 'js']
port_lst = ['28026','28036']
word_lst = ['刘德华', '长安cs55', '海的故事']
q_from_lst =['web', 'wap']

def log_info(str):
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    sys.stdout.write('[%s] [info] %s\n' % (time_str, str))
    sys.stdout.flush()

def gen_url_prefix():
    url_list = []
    for loc in loc_lst:
        for port in port_lst:
            for id in range(1,6):
                url_prefix = 'http://tj' + ('%.2d' % id) + '.tupu.' + loc + '.ted:' + port
                url_list.append(url_prefix)
    return url_list

def gen_payload():    
    payload_lst = []
    for word in word_lst:
        for q_from in q_from_lst:
            payload = dict()
            payload['queryString'] = word.encode('utf16')
            payload['queryFrom'] = q_from.encode('utf16')
            payload_lst.append(payload) 
    return payload_lst

def main():

    url_list = gen_url_prefix()
    payload_lst = gen_payload()
       
    with open('./test_result', 'w') as f:        
        for url_prefix in url_list:
            for payload in  payload_lst:
                try:            
                    response = requests.get(url_prefix, params = payload)
                    url = response.url
                    status = response.status_code
                    result = response.text.encode('gbk').decode('unicode_escape')
                    log_info('%s\n' % url)
                    time.sleep(1)
                    
                    if status != 200:
                        f.write('http status:%s \t url:%s \n\n' % (status, url))
                        continue
                    if 'pvtype=\"21_73\"' not in result:
                        f.write('No Result. \t url:%s \n\n' % url)
                        
                except Exception as err:
                    f.write('%s \n\n' % err)    
        
        file_size = os.path.getsize('./test_result')
        if file_size > 0:
            cmd_sendmail = " mutt -s 'Tupu Recommender Detector' -i test_result -F ./mutt_config < /dev/null -- yinjingjing@sogou-inc.com xuhuanran@sogou-inc.com chenxi215725@sogou-inc.com hujixing@sogou-inc.com"
            os.system(cmd_sendmail)
   
 
if __name__ == '__main__':
    main()
    


