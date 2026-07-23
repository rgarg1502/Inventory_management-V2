from fastapi import APIRouter,status, Depends
from .schemas import CategoryCreate, CategoryResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from .service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags = ["Categories"]    
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
async def create_category(category:CategoryCreate,db:AsyncSession=Depends(get_db)):
    service = CategoryService(db)

    return await service.create(category)

@router.get("/{category_id}",response_model=CategoryResponse)
async def get_category(category_id:int,db:AsyncSession=Depends(get_db)):

    service = CategoryService(db)

    return await service.get_by_id(category_id)

@router.get("",response_model=list[CategoryResponse])
async def get_categories(db:AsyncSession=Depends(get_db)):

    service = CategoryService(db)

    return await service.get_all()