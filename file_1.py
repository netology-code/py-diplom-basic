import os
import requests
from pprint import pprint


class VK:
    """Представляет собой клиент API ВКонтакте."""

    def __init__(self, access_token, user_id, version='5.131'):
        """Инициализирует клиент ВКонтакте с токеном доступа, идентификатором пользователя и версией."""
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        """Извлекает информацию о пользователе из API ВКонтакте."""
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        try:
            response = requests.get(url, params={**self.params, **params})
            response.raise_for_status(
            )  # Вызвать исключение для неверных кодов статуса
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении информации о пользователе: {e}")
            return None


access_token = (
    'vk1.a.-JoIfPWTQzyYOiL4Xdma7zZ_ZLY6LaYHMs5-Wf41ByZ9UDHxHk2foQGWkLiuOKVbjR'
    '-PcRuP3nuBY6TuYzcxY5l0AXINnOdT5AOVu1Qqn4RgfXb_qwzruHNzK01xdLgDrmSluaEfeeAUZCxtgZ_IizpLa4qTaTOx1W0bNbeBtqhwJGEB2N15eG4kQWwSXoee'
)
user_id = '837974821'
vk = VK(access_token, user_id)

pprint(vk.users_info())
