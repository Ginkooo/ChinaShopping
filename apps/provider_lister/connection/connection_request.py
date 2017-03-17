class ConnectionRequest:
   
    __headers = {
            
            }

    def add_url(self, url):
        self.__url = url

    def add_header(key, value):
      self.__headers[key] = value

    def get_headers(self):
        return self.__headers

    def get_url(self):
        return self.__url
