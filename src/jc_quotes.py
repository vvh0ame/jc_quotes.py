from requests import get

class JCQuotes:
	def __init__(self) -> None:
		self.api = "https://www.jcquotes.com/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36"
		}

	def get_random_quote(self) -> dict:
		return get(
			f"{self.api}/quotes/random",
			headers=self.headers).json()
