from sqlalchemy.orm import Mapped, mapped_column

from template.database.base import Base


class A(Base):
    """User ORM example"""
    # Don't name your table "users" or postgresql is not gonna be happy
    __tablename__ = "template_users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
