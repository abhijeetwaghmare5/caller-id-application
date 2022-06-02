import paramiko
import sys

paramiko.util.log_to_file('logfile.log')
host=sys.argv[1]
port=22
transport= paramiko.Transport((host, port))
password=sys.argv[2]
username=sys.argv[3]

sftp=paramiko.SFTPClient.from_transport(transport)

filepath1='~ /.ssh/known_hosts'
filepath2='~/.ssh/authorized_keys '
remotepath1='~ /.ssh/known_hosts'
remotepath2='~/.ssh/authorized_keys '

sftp.get(remotepath1,filepath1)
sftp.get(remotepath2,filepath2)