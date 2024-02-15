from sqlalchemy.orm import Mapped, mapped_column

from template.database.base import Base


class User(Base):
    """User ORM example"""
    __tablename__ = "template_user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
