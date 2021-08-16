import random
import string

from pydantic import EmailStr


def random_lower_string(length: int = 20) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def random_email() -> EmailStr:
    return EmailStr(f"{random_lower_string()}@{random_lower_string()}.com")
