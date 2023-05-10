from abc import ABC
from typing import Optional, List

from domain.user import User as DomainUser
from models.user import User as ModelUser


class ABCUserRepository(ABC):
    def get_user_by_id(self, id: str) -> Optional[DomainUser]:
        pass

    def get_all_user(self, id: str) -> Optional[List[DomainUser]]:
        pass

    def reset_password_by_id(self, id: str) -> str:
        pass

    def give_staff_rule_by_id(self, id: str) -> bool:
        pass


class UserRepository(ABCUserRepository):
    @classmethod
    def DomainToModel(cls, user: DomainUser) -> ModelUser:
        return ModelUser(
            id=user.id,
            email=user.email,
            nickname=user.nickname,
            name=user.name,
            is_active=user.is_active,
            is_staff=user.is_staff,
            joined_date=user.joined_date,
            expired_date=user.expired_date,
            password=user.password,
            ethereum_address=user.ethereum_address,
        )

    @classmethod
    def ModelToDomain(cls, user: ModelUser) -> DomainUser:
        return DomainUser(
            id=user.id,
            email=user.email,
            nickname=user.nickname,
            name=user.name,
            is_active=user.is_active,
            is_staff=user.is_staff,
            joined_date=user.joined_date,
            expired_date=user.expired_date,
            password=user.password,
            ethereum_address=user.ethereum_address,
        )

    def get_user_by_id(self, id: str) -> Optional[DomainUser]:
        result = ModelUser.objects.get(id=id)

        if not result:
            return None

        return self.ModelToDomain(result)

    def get_all_user(self, id: str) -> Optional[List[DomainUser]]:
        results = ModelUser.objects.all()

        if not results:
            return None

        return [self.ModelToDomain(result) for result in results]
