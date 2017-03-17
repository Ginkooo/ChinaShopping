from urllib import request
from apps.provider_lister.connection.connection_response import ConnectionResponse


class ConnectionService:
    def execute(self, connection_request):
        self.__connection_request = connection_request
        req = request.Request(self.__connection_request.get_url())
        for key, value in self.__connection_request.get_headers().items():
            req.add_header(key, value)
        response = request.urlopen(req)
        connection_response = ConnectionResponse(response)
        return connection_response
