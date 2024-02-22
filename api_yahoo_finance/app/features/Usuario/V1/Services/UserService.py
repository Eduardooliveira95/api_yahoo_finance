from typing import List
#from app.daos.user_dao import UserDAO
from app.features.Usuario.V1.Models.DTO.User import UserCreate, UserUpdate

class UserService:
    #def __init__(self):
    #   self.user_dao = UserDAO()

    def get_users(self, skip: int = 0, limit: int = 10) -> List[UserUpdate]:

        usuarios = UserUpdate(username="Eduardo", email="teste@gmail.com")

        items_list = []

        items_list.append(usuarios)

        return items_list

        #return self.user_dao.get_users(skip=skip, limit=limit)

    def get_user(self, user_id: int) -> UserCreate:
        return self.user_dao.get_user(user_id=user_id)
