from sys import platform

FB_BASE_URL = 'https://facebook.com/'
FB_W3_BASE_URL = 'https://www.facebook.com/'
FB_MOBILE_BASE_URL = 'https://mbasic.facebook.com/' if platform == "darwin" else 'https://m.facebook.com/'
FB_MBASIC_BASE_URL = 'https://mbasic.facebook.com/'

DEFAULT_REQUESTS_TIMEOUT = 30
DEFAULT_PAGE_LIMIT = 10

DEFAULT_COOKIES_FILE_PATH = '.fb-cookies.pckl'
