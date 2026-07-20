from sqlalchemy.ext.asyncio import AsyncSession
from .models import Category
from .schemas import CategoryCreate


class CategoryRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, category: CategoryCreate) -> Category:
        db_category = Category(**category.model_dump())

        self.db.add(db_category)

        await self.db.commit()

        await self.db.refresh(db_category)

        return db_category
