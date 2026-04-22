from enum import Enum


class HttpStatus(Enum):
    OK = (200, "OK")
    BAD_REQUEST = (400, "Bad Request")
    NOT_FOUND = (404, "Not Found")
    INTERNAL_SERVER_ERROR = (500, "Internal Server Error")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def is_success(self) -> bool:
        return self.code < 400

    def display(self) -> None:
        print(f"{self.code} {self.message}")

    @staticmethod
    def from_code(code: int):
        for status in HttpStatus:
            if status.code == code:
                return status
        return None


if __name__ == "__main__":
    HttpStatus.OK.display()
    HttpStatus.NOT_FOUND.display()

    print(f"Is 200 success? {str(HttpStatus.OK.is_success()).lower()}")
    print(f"Is 404 success? {str(HttpStatus.NOT_FOUND.is_success()).lower()}")

    found = HttpStatus.from_code(500)
    if found is not None:
        print("Found by code 500: ", end="")
        found.display()
