from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import verify_password, create_access_token
from app.core.exceptions import BadRequestException, NotFoundException
from fastapi import HTTPException


class AuthService:

    def __init__(self):
        self.repository = UserRepository()

    def register_user(
        self,
        db: Session,
        user_data: UserCreate
    ):
        existing_user = self.repository.get_by_email(
            db=db,
            email=user_data.email
        )

        if existing_user is not None:
            raise BadRequestException(
                detail="Email already registered"
            )

        return self.repository.create(
            db=db,
            user_data=user_data
        )

    def authenticate_user(
        self,
        db: Session,
        email: str,
        password: str
    ):
        user = self.repository.get_by_email(
            db=db,
            email=email
        )

        if user is None or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Incorrect email or password"
            )

        return user

    def login(
        self,
        db: Session,
        email: str,
        password: str
    ):
        user = self.authenticate_user(
            db=db,
            email=email,
            password=password
        )

        access_token = create_access_token(
            data={"sub": user.email}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }