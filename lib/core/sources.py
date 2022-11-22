import requests
import gevent
from lib.utils.dic_sort import dict_value_sort
import os
from shutil import copyfile

l_resp_time = {}

l_kali_apt_sources = {
    "# Offical": "http://http.kali.org/kali",
    "# USTC": "http://mirrors.ustc.edu.cn/kali",
    "# Aliyun": "http://mirrors.aliyun.com/kali",
    "# TSINGHUA": "http://mirrors.tuna.tsinghua.edu.cn/kali",
    "# ZJU": "http://mirrors.zju.edu.cn/kali"
}

l_modify_sources = {
    "http://http.kali.org/kali": ["# Offical", "deb http://http.kali.org/kali kali-rolling main no-free contrib", "deb-src http://http.kali.org/kali kali-rolling main non-free contrib"],

    "http://mirrors.ustc.edu.cn/kali": ["# USTC", "deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib", "deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib"],

    "http://mirrors.aliyun.com/kali": ["# Aliyun", "deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib", "deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib"],

    "http://mirrors.tuna.tsinghua.edu.cn/kali": ["# TSINGHUA", "deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free", "deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free"],

    "http://mirrors.zju.edu.cn/kali": ["# ZJU", "deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free", "deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free"]
}

# 从 l_kali_apt_sources 获取不同源 URL
l_sources = []
for key in l_kali_apt_sources:
    l_sources.append(l_kali_apt_sources[key])

# Return URL delay dictionary
def resp_time(url):
    global l_resp_time
    try:
        resp = requests.get(url)
        l_resp_time[url] = resp.elapsed.total_seconds()
    except UnboundLocalError:
        pass
    except requests.exceptions.ConnectionError:
        pass

def run_resp_time():
    global l_resp_time
    for e in l_sources:
        gevent.joinall([gevent.spawn(resp_time, f"{e}")])
    return l_resp_time

# Modify /etc/apt/sources.list
def modify_sources(url_list):
    sources_path = "/etc/apt/sources.list"
    try:
        assert os.path.exists(sources_path)
        # Backup sources.list
        if not os.path.exists("/etc/apt/sources.list.backup"):
            copyfile(sources_path, f"{sources_path}.backup")
            print('Back up the original file: "sources.list.backup"')
        # Detect already exists
        with open(sources_path, "w") as f:
            for url in url_list:
                if url in l_modify_sources:
                    for e in l_modify_sources[url]:
                        f.write(e+"\n")
    except AssertionError as e:
        raise FileNotFoundError