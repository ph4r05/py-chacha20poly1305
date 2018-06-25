# Chacha20poly1305

Simple pure-python chacha20-poly1305 implementation based on [tlslite-ng] code.
Designed to be compatible with Cryptography API.


```python
import os
from chacha20poly1305 import ChaCha20Poly1305

key = os.urandom(32)
cip = ChaCha20Poly1305(key)

nonce = os.urandom(12)
ciphertext = cip.encrypt(nonce, b'test')

plaintext = cip.decrypt(nonce, ciphertext)
print(plaintext)
```

## Pip

```bash
pip install chacha20poly1305
```


[tlslite-ng]: https://github.com/tomato42/tlslite-ng

