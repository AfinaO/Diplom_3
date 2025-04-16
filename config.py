# Configuration data

MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
ORDER_HISTORY_PAGE = MAIN_PAGE + 'account/order-history'
API_CREATE_USER = MAIN_PAGE + 'api/auth/register'
API_DELETE_USER = MAIN_PAGE + 'api/auth/user'


class Resolution:
    FHD = 1200, 800


BROWSERS = {
    'Chrome': ['--window-size={},{}'.format(*Resolution.FHD)],
    'Firefox': '--width={} --height={}'.format(*Resolution.FHD).split()
}
