from .models import Category
from .schemas import CategoryCreate
from app.database.base_repository import BaseRepository
from sqlalchemy import select


class CategoryRepository(BaseRepository):

    async def create(self, category: CategoryCreate) -> Category:
        db_category = Category(**category.model_dump())

        self.db.add(db_category)

        await self.db.flush()

        await self.db.refresh(db_category)

        return db_category

    async def get_by_id(self, category_id: int) -> Category | None:
        stmt = select(Category).where(Category.id == category_id)

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_name(self, name: str) -> Category | None:
        stmt = select(Category).where(Category.name == name)

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all(self) -> list[Category]:
        stmt = select(Category).order_by(Category.id)

        result = await self.db.execute(stmt)

        return result.scalars().all()
