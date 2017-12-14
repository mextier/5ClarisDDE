#https://github.com/indranilsinharoy/PyZDDE/blob/master/pyzdde/ddeclient.py
#https://www.youtube.com/watch?v=TlroLaxCk9E

#Task:0x1c84 Time:14339736 hwndTo=0x2005e Message(Sent)=Initiate:
	#hwndFrom=0x250ad0, App=0xc080("ClarionWin")
	#Topic=*
#Task:0x1c84 Time:14339767 hwndTo=0xd07ae Message(Posted)=Execute:
	#hwndFrom=0x250ad0,
	#Execute command="[ExecuteProject"
#Task:0x1934 Time:14339799 hwndTo=0x250ad0 Message(Posted)=Ack:
	#hwndFrom=0xd07ae, App=0x8000("#32768")status=8000(fAck )
	#Topic=Item=0x28e004c("#76")


from ddeclient import DDEClient
from ctypes import *

import win32ui
import dde

CLARIS_SERVICENAME = "ClarionWin"

c = DDEClient(CLARIS_SERVICENAME,"")
#CommandLine=b'[ExecuteProject(D:\5Claris\source\z.app)]'
#CommandLine=create_string_buffer(b"abc")
CommandLine=b'zzz'
try:
	res = c.execute(CommandLine)
except Exception as e:
	print(e)
else:
	pass
finally:
	pass
