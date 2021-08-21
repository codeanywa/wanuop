#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

path="iptv.txt"
path2="wanuop.m3u"

f=open(path, 'r',encoding='utf-8')
content=f.readlines()
f.close()
channel_dict={}
channel_list_temp1=[]
channel_list_temp2=[]
for i in range(len(content)):
    if ("ChannelName=") in content[i]:
        #print(content[i])
        channel_list_temp1.append(content[i])
#print(len(channel_list_temp1))
pattern1 = "(ChannelName=\"([\u4E00-\u9FA5A-Za-z0-9_-]+)\").*?(ChannelURL=\"(http.*?index\.m3u8{1}))"
pattern2 = ""
for i in range(len(channel_list_temp1)):
    result = re.search(pattern1, channel_list_temp1[i])
    #print(result)
    if result:
        #print(result.group())
        result2=re.match(pattern1,result.group())
        #print(result2.group(2))
        #print(result2.group(4))
        channel_dict[result2.group(2)] = result2.group(4)
#print(channel_dict)
#channel_dict_data=list(channel_dict.keys()).sort(channel_dict.items(),key=lambda arr: (arr[:3],arr[3:]))
#print(list(channel_dict.keys()))
list0=list(channel_dict.keys())
#_nsre = re.compile('([0-9]+)')

def natural_sort_key(s):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(s, key = alphanum_key)

list0=natural_sort_key(list0)
#print(list0)
list1=[]
for i in range(len(list0)):
    if list0[i]+"HD" in list0:
        #print(list0[i])
        pass
    elif "年级" in list0[i]:
        pass
    elif "直播室" in list0[i]:
        pass
    else:
        list1.append(list0[i])
print(list1)

f=open(path2, 'w',encoding='utf-8')
m3u_content=[]
m3u_content.append("#EXTM3U\n")
for i in list1:
    m3u_content.append("#EXTINF:-1," + i + "\n")
    m3u_content.append(channel_dict[i] + "\n")
print(m3u_content)
f.writelines(m3u_content)
f.close()