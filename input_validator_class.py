from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, input: str) -> bool:
        pass


class EmailValidator(Validator):
    def validate(self, input: str) -> bool:
        return "@" in input


class PasswordValidator(Validator):
    def validate(self, input: str) -> bool:
        return "@" in input


class RegistrationService:
    def __init__(self, validators: list[Validator]):
        self._validators = validators

    def register(self, input: str) -> None:
        all_passed = all(v.validate(input) for v in self._validators)
        result = "PASSED" if all_passed else "FAILED"
        print(f'"{input}" - {result}')


if __name__ == "__main__":
    email_reg = RegistrationService([EmailValidator()])
    email_reg.register("user@example.com")  # Should pass
    email_reg.register("invalid-email")  # Should fail

    pass_reg = RegistrationService([PasswordValidator()])
    pass_reg.register("strongpassword")  # Should pass
    pass_reg.register("short")  # Should fail
