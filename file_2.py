from abc import update_abstractmethods
import requests
import json

# APP_ID = '837974821'
# QAUTH_BASE_URL = 'https://oauth.vk.com/authorize'
# params = {
#   'client_id': APP_ID,
#   'redirct_uri': 'https://oauth.vk.com/blank.html',
#   'display': 'page',
#   'scope': 'staatus,photos',
#   'response_type': 'token',
# }
# qauth_url = f'{QAUTH_BASE_URL}?{requests.compat.urlencode(params)}'
# print(qauth_url)

TOKEN = 'vk1.a.-JoIfPWTQzyYOiL4Xdma7zZ_ZLY6LaYHMs5-Wf41ByZ9UDHxHk2foQGWkLiuOKVbjR-PcRuP3nuBY6TuYzcxY5l0AXINnOdT5AOVu1Qqn4RgfXb_qwzruHNzK01xdLgDrmSluaEfeeAUZCxtgZ_IizpLa4qTaTOx1W0bNbeBtqhwJGEB2N15eG4kQWwSXoee'


class VKAPIClient:
  """Представляет собой клиент API ВКонтакте."""
  API_BAZE_URL = 'https://api.vk.com/method'

  def __init__(self, token, user_id):
    """Инициализирует клиент ВКонтакте с токеном доступа, идентификатором пользователя и версией."""
    self.token = token
    self.id = user_id

  def get_common_params(self):
    """Извлекает общие параметры для всех запросов к API ВКонтакте."""
    return {'access_token': self.token, 'v': '5.131'}

  def get_status(self):
    """Извлекает информацию о статусе пользователя из API ВКонтакте."""
    params = self.get_common_params()
    params.update({'user_id': self.id})
    respons = requests.get(f'{self.API_BAZE_URL}/status.get', params=params)
    return respons.json()


if __name__ == '__main__':
  vk_client = VKAPIClient(TOKEN, 837974821)
  print(vk_client.get_status())
