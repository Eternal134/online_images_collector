class Response:
    
    def __init__(self, requestId: str, code: int=0, data=None, msg: str=""):
        self.requestId = requestId
        self.code = code
        self.data = data
        self.msg = msg
        
    def buildError(self, msg: str):
        self.code = -1
        self.msg = msg
        self.data = None