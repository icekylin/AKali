# AKali
Armed Kali Linux - Automate some configurations of kali

**使用方法**

```bash
git clone https://github.com/icekylin/AKali.git
cd AKali
sudo python3 -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
sudo python3 akali.py
```

**主要功能**

- [x] Optimize Kali apt sources - 根据网络延迟优化源
  - 判断不同延迟时间, 优化 `/etc/apt/sources.list` 文件内容
  - 备份的文件名称为 `sources.list.backup`
  - 目前包含 `Office`、`浙大`、`阿里云`、`科大`