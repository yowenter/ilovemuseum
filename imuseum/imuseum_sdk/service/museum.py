from base_service import BaseService

from imuseum_sdk import models


class Museum(BaseService):
    @property
    def resource_class(self):
        return models.Museum
