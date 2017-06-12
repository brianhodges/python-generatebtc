import os
import sys
import time
import random
import string
from bitcoin import *

rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
filename = rand_str(10) + '.html'
br = '<br>'

# Generate Pub/Priv Key Pair
priv_key = random_key()
pub_key = privkey_to_pubkey(priv_key)
address = pubkey_to_address(pub_key)
address_compressed = pubkey_to_address(compress(pub_key))

# Write BTC info to File
f = open(filename,"w")
try:
    f.write('<html><body>')
    f.write('<strong>Address:</strong>' + br + address + br)
    f.write('<strong>Address (compressed):</strong>' + br + address_compressed + br + br)
    f.write('<strong>Public Key:</strong>' + br + pub_key + br)
    f.write('<strong>Public Key (compressed):</strong>' + br + compress(pub_key) + br + br)
    f.write('<strong>Private Key:</strong>' + br + priv_key + br)
    f.write('</body></html>')
    f.close()
    os.system("open "+filename)
    time.sleep(1)
    os.remove(filename)
except:
    e = sys.exc_info()[0]
    print(e)
    f.close()
    os.remove(filename)