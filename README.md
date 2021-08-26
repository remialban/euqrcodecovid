# euqrcodecovid
Python file to retrieve the contents of the qr code of the European health passport

```get_content(code)``` :
- **code** : contains the content of the qr code. Begin often by "HC1:..."
- **return** a dictionnary object that contains the informations related to vaccination

Clone the ```euqrcodecovid.py``` file and add the ```get_content(code)``` function to your code :

```python
from euqrcodecovid import get_content

data = get_content("HC1:......")

print(data)

```
