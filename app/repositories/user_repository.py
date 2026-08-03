from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


class UserRepository:

    def get_by_email(
        self,
        db: Session,
        email: str
    ) -> User | None:

        return db.query(User).filter(
            User.email == email
        ).first()

    def create(
        self,
        db: Session,
        user_data: UserCreate
    ) -> User:

        user = User(
            email=user_data.email,
            hashed_password=hash_password(user_data.password)
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user