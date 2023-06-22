from __future__ import annotations
from pprint import pprint
from typing import List


class UserList(list):
    def search(self, name: str) -> list["User"]:
        matching_users: list["User"] = []
        for user in self:
            if name in user.all_users:
                matching_users.append(user)
        return matching_users

    def append(self, obj) -> None:
        if not isinstance(obj, User):
            raise TypeError('This list only accepts user')
        return super(UserList, self).append(obj)


class User:
    all_users: list["User"] = UserList()

    def __init__(self, name: str, email: str, pas: str, **kwargs) -> None:
        self.name = name
        self.email = email
        self.pas = pas
        User.all_users.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.email!r}, {self.pas!r})"

    def __str__(self):
        return f"{self.name}"


class Seller(User):
    def __init__(self, shaba, **kwargs) -> None:
        super().__init__(**kwargs)
        self.shaba = shaba

    def order(self, order: "Order") -> None:
        print(f'{self.name} from ur products "{order}" was sold')


class Buyer(User):
    def __init__(self, phone: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.phone = phone


class SellerBuyer(Seller, Buyer):
    def __init__(self, score, **kwargs):
        super().__init__(**kwargs)
        self.score = score


def main():
    obj = SellerBuyer(name='mmd', pas='123', email='gmail', phone='00908', shaba='009', score=9)
    print(User.all_users)


if __name__ == '__main__':
    main()

