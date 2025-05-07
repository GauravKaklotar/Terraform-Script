class Service:
    def get_data(self):
        return "Data from Service"

class Client:
    def __init__(self, service):
        self.service = service  

    def fetch_data(self):
        return self.service.get_data()

service = Service()
client = Client(service)
print(client.fetch_data())
