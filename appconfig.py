import random

chrome_versions = {
    120: [
        '120.0.6099.230',
        '120.0.6099.210',
        '120.0.6099.194',
        '120.0.6099.193',
        '120.0.6099.145',
        '120.0.6099.144',
        '120.0.6099.144',
        '120.0.6099.116',
        '120.0.6099.116',
        '120.0.6099.115',
        '120.0.6099.44',
        '120.0.6099.43'
    ],
    121: [
        '121.0.6167.178',
        '121.0.6167.165',
        '121.0.6167.164',
        '121.0.6167.164',
        '121.0.6167.144',
        '121.0.6167.143',
        '121.0.6167.101'
    ],
    122: [
        '122.0.6261.119',
        '122.0.6261.106',
        '122.0.6261.105',
        '122.0.6261.91',
        '122.0.6261.90',
        '122.0.6261.64',
        '122.0.6261.43'
    ],
    123: [
        '123.0.6312.121',
        '123.0.6312.120',
        '123.0.6312.119',
        '123.0.6312.118',
        '123.0.6312.99',
        '123.0.6312.80',
        '123.0.6312.41',
        '123.0.6312.40'
    ],
    124: [
        '124.0.6367.179',
        '124.0.6367.172',
        '124.0.6367.171',
        '124.0.6367.114',
        '124.0.6367.113',
        '124.0.6367.83',
        '124.0.6367.82',
        '124.0.6367.54'
    ],
    125: [
        '125.0.6422.165',
        '125.0.6422.164',
        '125.0.6422.147',
        '125.0.6422.146',
        '125.0.6422.113',
        '125.0.6422.72',
        '125.0.6422.72',
        '125.0.6422.53',
        '125.0.6422.52'
    ]
}
major_version = random.choice(list(chrome_versions.keys()))
browser_version = random.choice(chrome_versions[major_version])
android_versions = ['9.0', '10.0', '11.0', '12.0', '13.0', '14.0']
android_device = random.choice([
    'Pixel 5', 'Pixel 5a', 'Pixel 6', 'Pixel 6 Pro', 'Pixel 6 XL',
    'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Redmi Note 8',
    'Redmi Note 8 Pro', 'Redmi Note 9', 'Redmi Note 9 Pro', 'Redmi Note 10',
    'Redmi Note 10 Pro', 'Redmi Note 11', 'Redmi Note 11 Pro', 'Redmi Note 12',
    'Redmi Note 12 Pro', 'POCO F3', 'POCO F5', 'POCO F5 Pro', 'POCO M3', 'POCO M3 Pro'
])
android_version = random.choice(android_versions)
random_user_agent = (f"Mozilla/5.0 (Linux; Android {android_version}; {android_device}; wv) AppleWebKit/537.36 "
                     f"(KHTML, like Gecko) Version/4.0 Chrome/{browser_version} Mobile Safari/537.36")

user_agent = ("Mozilla/5.0 (Linux; Android 13; RMX3630 Build/TP1A.220905.001; wv) "
              "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.165 "
              "Mobile Safari/537.36")

request_headers = {
    'authority': 'api.simple.app',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'x-requested-with': 'org.telegram.messenger',
    'Content-Type': 'application/json',
    'Origin': 'https://simpletap.app',
    'Referer': 'https://simpletap.app/',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'User-Agent': random_user_agent  # or user_agent
}


class AppURLS:
    BASE_URL = 'https://api.simple.app/api/v1/public/'
    PROFILE_URL = f'{BASE_URL}telegram/profile/'
    ACTIVATE_URL = f'{BASE_URL}telegram/activate/'
    TAP_URL = f'{BASE_URL}telegram/tap/'
    CLAIM_URL = f'{BASE_URL}telegram/claim/'
    GET_TASK_LIST_URL = f'{BASE_URL}telegram/get-task-list-2/'
    START_TASK_URL = f'{BASE_URL}telegram/start-task-start-2/'
    CHECK_TASK_URL = f'{BASE_URL}telegram/check-task-check-2/'
    FRIENDS_URL = f'{BASE_URL}telegram/friends/'
    CLAIM_FRIENDS_URL = f'{BASE_URL}telegram/claim_friends/'
    GET_SPIN_WHEEL_URL = f'{BASE_URL}telegram/get-spin-wheel/'
    CLAIM_SPIN_URL = f'{BASE_URL}telegram/claim-spin/'
    GET_MINING_BLOCKS_URL = f'{BASE_URL}telegram/get-mining-blocks/'
    BUY_MINING_BLOCK_URL = f'{BASE_URL}telegram/buy-mining-block/'
    GET_COLLECTIONS_URL = f'{BASE_URL}telegram-collection/get-collections/'
    GET_COLLECTION_CARDS_URL = f'{BASE_URL}telegram-collection/get-collection-cards/'
    CARD_CLAIM_URL = f'{BASE_URL}telegram-collection/card-claim/'
    CARD_DESCRIPTION_URL = f'{BASE_URL}telegram-collection/card-description/'
