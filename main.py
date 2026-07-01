from fastapi import FastAPI
from schemas import CourseCreate, CourseResponse
from typing import Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from models import Course
from database import get_db, create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(
    title="Course Management API",
    version="1.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "API Running"}

@app.post("/api/courses/", response_model=CourseResponse)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(**course.model_dump())

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    return new_course

@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):
    return {"course_id": course_id}

@app.get("/api/courses/", response_model=list[CourseResponse])
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    if department_id is not None:
        query = query.where(Course.department_id == department_id)

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()