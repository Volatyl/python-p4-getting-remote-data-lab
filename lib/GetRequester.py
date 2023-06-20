import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        people = self.get_response_body()
        data = json.loads(people)
        return data
 

url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

site = GetRequester(url)
print(site.load_json())
