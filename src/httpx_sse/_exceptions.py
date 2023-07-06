import httpx
from typing import Optional

class SSEError(httpx.TransportError):
    def __init__(self, *args, response: Optional[httpx.Response] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.response = response
