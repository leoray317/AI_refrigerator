from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
"""
# add_user(userName, pwd, home dir, permissions)
#
# Read permissions:
#                   "e" = change directory (CWD, CDUP commands)
#                   "l" = list files (LIST, NLST, STAT, MLSD, MLST, SIZE commands)
#                   "r" = retrieve file from the server (RETR command)
# Write permissions:
#                   "a":append, "d": delete file or directory, 
#                   "f": rename file or directory (RNFR, RNTO commands)
#                   "m" = create directory (MKD command)
#                   "w" = store a file to the server (STOR, STOU commands)
#                   "M" = change file mode / permission (SITE CHMOD command) New in 0.7.0
#                   "T" = change file modification time (SITE MFMT command) New in 1.5.3
"""
authorizer.add_user(r"user", r"12345", r"./home", perm=r"elradfmwMT") # opened all permissions
authorizer.add_anonymous(r"./home/nobody")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer((r"127.0.0.1", 21), handler)
server.serve_forever()