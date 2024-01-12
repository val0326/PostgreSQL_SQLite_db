from fastapi import APIRouter, HTTPException
from fastapi import Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, RequestBook, Response
import crud


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield
    finally:
        db.close()


@router.post('/create')
async def create(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(code=200,
                    status="Ok",
                    message="Book created successfully").dict(exclude_none=True)


@router.get("/")
async def get_books(skip: int = 0, limit=100, db: Session = Depends(get_db)):
    crud.get_book(db, skip, limit)
    return Response(code=200,
                    status="Ok", message="Success fetch all data", result=_book)


# @router.get("/{id}")
# async def get_by_id(id: int, db: Session = Depends(get_db)):
#     _book = crud.get_book_by_id(db, id)
#     return Response(code=200, status="Ok", message="Success get data", result=_book).dict(exclude_none=True)


@router.post("/update")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(db, book_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(code=200, status="Ok", message="Success update data", result=_book)


@router.delete("/delete")
async def delete_book(request: RequestBook, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=request.parameter.id)
    return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)
