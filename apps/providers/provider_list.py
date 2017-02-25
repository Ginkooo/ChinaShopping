class ProviderList:
    import apps.providers.aliexpress.allieexpress_crawler as aliexpress
    LIST = [
        aliexpress.AliExpressCrawler()
    ]

    @classmethod
    def get(self):
        return self.LIST
