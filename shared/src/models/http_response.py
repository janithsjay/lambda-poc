import json


class HTTPResponse:
    def __init__(self, status_code, response_body, error_code, error_message):
        self.status_code = status_code
        self.response_body = response_body
        self.error_code = error_code
        self.error_message = error_message

    def to_json(self):
        response = {
            "statusCode": self.status_code,
            "body": json.dumps(self.response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
