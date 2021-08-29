#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ref: https://github.com/LiuYi0526/IPTV

import re

path="iptv.txt"
path2="wanuop_temp.m3u"

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

#--------------------------------------------------------------------------------------------------------

#自定义添加频道
channel_dict["CCTV5+-HD1"] = "http://117.148.179.50/hwltc.tv.cdn.zj.chinamobile.com/PLTV/88888888/224/3221228822/index.m3u8"
channel_dict["CCTV5+-HD-咪咕"] = "http://gslbserv.itv.cmvideo.cn/1.m3u8?channel-id=ystenlive&Contentid=1000000001000020505&livemode=1&stbId=00000250001B50800001B401420BC069"
channel_dict["CCTV5+-HD2"] = "http://117.169.124.46:6410/ysten-businessmobile/live/hdcctv05plus/1.m3u8"
channel_dict["4K超清-北京IPTV"] = "http://otttv.bj.chinamobile.com/TVOD/88888888/224/3221226550/1.m3u8"
channel_dict["凤凰中文"] = "http://223.110.235.3/ott.js.chinamobile.com/PLTV/3/224/3221228057/index.m3u8"
channel_dict["凤凰资讯"] = "http://223.110.235.13/ott.js.chinamobile.com/PLTV/3/224/3221228098/index.m3u8"
channel_dict["凤凰香港"] = "http://223.110.236.2/ott.js.chinamobile.com/PLTV/3/224/3221228060/index.m3u8"
channel_dict["CCTV13新闻-HD1"] = "http://hwrr.jx.chinamobile.com:8080/PLTV/88888888/224/3221225638/index.m3u8"
channel_dict["CCTV13新闻-HD-咪咕"] = "http://gslbserv.itv.cmvideo.cn/1.m3u8?channel-id=ystenlive&Contentid=1000000002000021303&livemode=1&stbId=00000250001B50800001B401420BC069"
channel_dict["CCTV11戏剧-HD1"] = "http://otttv.bj.chinamobile.com/TVOD/88888888/224/3221226463/1.m3u8"
channel_dict["CCTV11戏剧-HD-咪咕"] = "http://gslbserv.itv.cmvideo.cn/1.m3u8?channel-id=ystenlive&Contentid=1000000002000019789&livemode=1&stbId=00000250001B50800001B401420BC069"
channel_dict["CCTV15音乐-HD-咪咕"] = "http://gslbserv.itv.cmvideo.cn/1.m3u8?channel-id=ystenlive&Contentid=1000000002000008163&livemode=1&stbId=00000250001B50800001B401420BC069"
channel_dict["点掌财经"] = "http://cclive.aniu.tv/live/anzb.m3u8"
channel_dict["日本NHK华语"] = "https://nhkw-zh-hlscomp.akamaized.net/8thz5iufork8wjip/playlist.m3u8"
#--------------------------------------------------------------------------------------------------------


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
    elif "购物" in list0[i]:
        pass
    elif "高清导视频道" in list0[i]:
        pass
    else:
        list1.append(list0[i])
#print(list1)

f=open(path2, 'w',encoding='utf-8')
m3u_content=[]
m3u_content.append("#EXTM3U url-tvg=\"http://epg.51zmt.top:8000/e.xml.gz\"\n")
for i in list1:
    m3u_content.append("#EXTINF:-1 tvg-id=\"\"," + i + "\n")
    m3u_content.append(channel_dict[i] + "\n")
#print(m3u_content)
f.writelines(m3u_content)
f.close()