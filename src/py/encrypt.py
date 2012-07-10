import base64

def encode_salt(sData, sKey='xJp2BpRUSE'):
	sResult = ''
	sKey = sKey[len(sKey)-1:len(sKey)] + sKey[0:len(sKey)-1]
  	for i in range(len(sData)):
		sChar = sData[i:(i+1)]
		sKeyChar = sKey[(i % len(sKey)):(i % len(sKey))+1]
		sChar = chr(ord(sChar) + ord(sKeyChar))
		sResult += sChar
	hexed = base64.b64encode(sResult)
	return hexed.replace('+/', '-_')

	
