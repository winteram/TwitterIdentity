import base64

oauth_token = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
oauth_secret = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

def encode_salt(sData, sKey='xJp2BpRUSE'):
	sResult = ''
	sKey = sKey[len(sKey)-1:len(sKey)] + sKey[0:len(sKey)-1]
  	for i in range(len(sData)):
		sChar = sData[i:(i+1)]
		sKeyChar = sKey[(i % len(sKey)):(i % len(sKey))+1]
		sChar = chr(ord(sChar) + ord(sKeyChar))
		sResult += sChar
	hexed = base64.b64encode(sResult)
	return hexed.replace('+/', '-_').rstrip('=')

	
