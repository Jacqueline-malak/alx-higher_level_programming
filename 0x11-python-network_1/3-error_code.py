#!/usr/bin/python3
"""
have to manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code
display the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
