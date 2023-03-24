# recommendations/recommendations.py
from concurrent import futures
import grpc
import account_pb2
import account_pb2_grpc

mock_data = [
    {
        "id": "54a6ezr",
        "name": "GUest",
        "email": "habib.jlejla@supcom.tn",
        "age": 25
    },
    {
        "id": "54a6r",
        "name": "Guest2",
        "email": "habib.jlejla@supcom.com",
        "age": 28
    },
    {
        "id": "azera",
        "name": "Guest23",
        "email": "habib.jlejla@supcom.net",
        "age": 89
    }
]

class AccountService(account_pb2_grpc.AccountServiceServicer):
    def CreateUser(self, request, context):
        print(request)
        payload = {
            "id": "aezkjlazrjlez",
            "name": "Habib Jlejla",
            "email": "Jlejla@supcom.tn",
            "age": 53
        }
        return account_pb2.CreateUserResponse(payload)
    
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_pb2_grpc.add_AccountServiceServicer_to_server(AccountService,server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()