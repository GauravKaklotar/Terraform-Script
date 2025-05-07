class Service:
    def get_data(self):
        return "Data from Service"

class Client:
    def __init__(self):
        self.service = Service() 

    def fetch_data(self):
        return self.service.get_data()

client = Client()
print(client.fetch_data())
