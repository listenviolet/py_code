import subprocess 
print('$ nslookup www.python.org')
ret = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code', ret)

# $ nslookup www.python.org
# Server:		127.0.1.1
# Address:	127.0.1.1#53

# Non-authoritative answer:
# www.python.org	canonical name = dualstack.python.map.fastly.net.
# Name:	dualstack.python.map.fastly.net
# Address: 151.101.76.223

# Exit code 0
print('--------------------------')

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, 
					stdout = subprocess.PIPE,
					stderr = subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# $ nslookup
# Server:		127.0.1.1
# Address:	127.0.1.1#53

# Non-authoritative answer:
# python.org	mail exchanger = 50 mail.python.org.

# Authoritative answers can be found from:
# python.org	nameserver = ns3.p11.dynect.net.
# python.org	nameserver = ns1.p11.dynect.net.
# python.org	nameserver = ns4.p11.dynect.net.
# python.org	nameserver = ns2.p11.dynect.net.
# mail.python.org	internet address = 188.166.95.178
# mail.python.org	has AAAA address 2a03:b0c0:2:d0::71:1
# ns4.p11.dynect.net	internet address = 204.13.251.11
# ns2.p11.dynect.net	internet address = 204.13.250.11
# ns1.p11.dynect.net	internet address = 208.78.70.11
# ns3.p11.dynect.net	internet address = 208.78.71.11


# Exit code: 0
