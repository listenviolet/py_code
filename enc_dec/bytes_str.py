s = '中文'
print("str:",s)
print(type(s))
print("str.encode():", s.encode())


b = bytes(s, encoding = 'utf-8')  # str -> utf-8 -> bytes
print("bytes(s):", b)
print(type(b))
print("bytes decode:", b.decode())

c = str(b, encoding = 'utf-8') # bytes -> utf8 -> str
print("str(b):", c)

# encode: 从字符串向比特流的编码
# decode: 从比特流向字符串解码
# s.encode() == bytes(s, encoding = 'utf-8')
# b.decode() == str(b, encoding = 'utf-8')
# s: <class 'str'>
# b: <class 'bytes'>

# Tips:
# 1. 在将字符串存入磁盘和从磁盘读取字符串的过程中，
# Python自动地帮你完成了编码和解码的工作，你不需要关心它的过程。

# 2. 使用bytes类型，实质上是告诉Python，不需要它帮你自动地完成编码和解码的工作，
# 而是用户自己手动进行，并指定编码格式。

# 3. Python已经严格区分了bytes和str两种数据类型，
# 你不能在需要bytes类型参数的时候使用str参数，反之亦然。这点在读写磁盘文件时容易碰到
# https://www.cnblogs.com/chownjy/p/6625299.html