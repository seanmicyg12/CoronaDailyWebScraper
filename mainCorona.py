import requests
import json

API_KEY = "tUNy9hbU7rya"
PROJECT_TOKEN = "tpkQ8Nr2_zEU"
RUN_TOKEN = "tm_gF7PJ6H0X"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(response.text)
print(data['country'])

class Data:
    def _init_(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
        self.data = json.loads(response.text)

    def get_total_cases(self):
        data = self.data['total']['']

        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def get_country_data(self, country):
        data = self.data["country"]

        for content in data:
            if content['name'].lower() == country.lower():
                return content

        return "0"

data = Data(API_KEY, PROJECT_TOKEN)
print(data.get_total_cases("italy")['total_cases'])