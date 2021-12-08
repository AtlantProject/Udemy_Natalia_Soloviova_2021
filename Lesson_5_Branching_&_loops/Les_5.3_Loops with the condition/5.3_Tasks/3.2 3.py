"""
Вычислить сумму натуральных четных чисел, не превышающих заданное число N.
2, 4, 6, 8, 10, ….

--------------------
Тестовые значения:

N       sum
10      30
14      56
20      110
"""
N = 20

sum = 0
i = 2

while i<=N:
    sum += i
    i += 2

print(sum)
# {"threads":[{"position":0,"start":0,"end":171,"connection":"open"},{"position":172,"start":172,"end":341,"connection":"idle"}],"url":"https://att-b.udemycdn.com/2021-04-14_14-36-44-a05ba469b9dc1d083dc86912ec7a4885/original.py?secure=AEzE97cbyKfBZoucLClciA%3D%3D%2C1620281771&filename=3.py","method":"GET","port":443,"downloadSize":341,"headers":{"date":"Thu, 06 May 2021 01:56:11 GMT","content-type":"text/x-python-script","content-length":"341","connection":"close","x-amz-id-2":"Io0mISwOZiO9Uip3km5/hDRNny7RPZwVRNqGG9SDIO7WGTreyC5PxljuLcMXgvsyiReFJU06qNE=","x-amz-request-id":"PQ5P0A40BKQ6R4EA","last-modified":"Wed, 14 Apr 2021 14:36:47 GMT","etag":"\"910a3f01ff97fe299e656dac4ae2f4a3\"","x-amz-server-side-encryption":"AES256","x-amz-meta-qqfilename":"3.py","x-amz-version-id":"e96B3y_PWcZLQsEUWdDdAlBHXEYY7hUK","x-77-nzt":"A7k73AE9ySSxubQOp/uGKrGP9DqB16q4wQ==","x-77-nzt-ray":"V+TUlTLyvm8=","x-77-cache":"MISS","cache-control":"max-age=31536000","content-disposition":"attachment; filename=\"3.py\"","x-cache-lb":"MISS, MISS","server":"CDN77-Turbo","x-77-pop":"frankfurtDE","accept-ranges":"bytes"}}