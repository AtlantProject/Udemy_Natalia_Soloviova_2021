"""
Необходимо декодировать закодированную строку:
b'\xd0\xa3\xd1\x87\xd0\xb8\xd0\xbc\xd1\x81\xd1\x8f \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c \xd0\xb2\xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xb5'
"""

encoded_s = b'\xd0\xa3\xd1\x87\xd0\xb8\xd0\xbc\xd1\x81\xd1\x8f \xd0\xbf\xd1' \
            b'\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1' \
            b'\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c \xd0\xb2\xd0\xbc\xd0' \
            b'\xb5\xd1\x81\xd1\x82\xd0\xb5'

decoded_s = encoded_s.decode()
print(decoded_s)

