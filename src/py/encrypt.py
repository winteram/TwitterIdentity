import base64

def get_tokens(username):
	tokens = {}
	if username == 'GroupID_Project':
		tokens['oauth_token'] = "625200110-OAgXw6qs3GlYxs4RKJLKv0S6SIMp9GzSAOpRXhmg"
		tokens['oauth_secret'] = "TOVaGhvptuQGl0TW0pXVwFmmW3QSsZvG4O4REaIBenc"
		tokens['CONSUMER_KEY'] = "IXChI2BWjZM7ZnjSdL5maw"
		tokens['CONSUMER_SECRET'] = "Jm3yFMEZ5XM1f8szrgGuzWRPfwiRHqINtlo0Eia88"
#	elif username == 'GroupIdentity':
	else:
		tokens['oauth_token'] = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
		tokens['oauth_secret'] = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
		tokens['CONSUMER_KEY'] = "PCMmY6ERIWJM9tgjIiQRwA"
		tokens['CONSUMER_SECRET'] = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"
	return tokens

def encode_salt(sData, sKey='xJp2BpRUSE'):
	sResult = ''
	# sKey = sKey[len(sKey)-1:len(sKey)] + sKey[0:len(sKey)-1]
  	for i in range(len(sData)):
		sChar = sData[i:(i+1)]
		sKeyChar = sKey[(i % len(sKey)):(i % len(sKey))+1]
		sChar = chr(ord(sChar) ^ ord(sKeyChar))
		sResult += sChar
	hexed = base64.b64encode(sResult)
	return hexed
	# return hexed.replace('+/', '-_').rstrip('=')
	
def decode_salt(sData, sKey='xJp2BpRUSE'):
	sResult = ''
	# sData.replace('-_','+/')
	sData = base64.b64decode(sData)
	# sKey = sKey[len(sKey)-1:len(sKey)] + sKey[0:len(sKey)-1]
  	for i in range(len(sData)):
		sChar = sData[i:(i+1)]
		sKeyChar = sKey[(i % len(sKey)):(i % len(sKey))+1]
		sChar = chr(ord(sChar) ^ ord(sKeyChar))
		sResult += sChar
	return sResult

if __name__ == '__main__':
	print 'Testing: "winteram"'
	print 'Encoded:'
	print encode_salt('winteram')
	print 'Decoded:'
	print decode_salt(encode_salt('winteram'))
	print 'Testing: "winteraaronmason"'
	print 'Encoded:'
	print encode_salt('winteraaronmason')
	print 'Decoded:'
	print decode_salt(encode_salt('winteraaronmason'))