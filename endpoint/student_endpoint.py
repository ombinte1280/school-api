from http.client import HTTPException
from typing import List

from fastapi import FastAPI
from starlette.responses import StreamingResponse

from data_set import Dataset
from model.student import Student


class StudentEndpoint:

    def __init__(self, data_set: Dataset, app: FastAPI):
        self._data_set = data_set
        self._app = app
        self.register_routes()

    def register_routes(self):
        self._app.add_api_route("/students/", self.create_student, methods=["POST"], response_model=Student)
        self._app.add_api_route("/students/", self.get_all_students, methods=["GET"], response_model=List[Student])
        self._app.add_api_route("/students-stream", self.stream_students, methods=["GET"])
        self._app.add_api_route("/students/{student_id}", self.get_student, methods=["GET"], response_model=Student)
        self._app.add_api_route("/students/{student_id}", self.update_student, methods=["PUT"], response_model=Student)
        self._app.add_api_route("/students/{student_id}", self.delete_student, methods=["DELETE"])


    async def create_student(self, student: Student):
        for s in self._data_set.students:
            if s.id == student.id:
                raise HTTPException(status_code=400, detail="Student already exists!!")
        student.id =  len(self._data_set.students) + 1
        self._data_set.students.append(student)
        return student

    async def get_all_students(self):
        return self._data_set.students

    async def get_student(self, student_id: int):
        for s in self._data_set.students:
            if s.id == student_id:
                return s
        raise HTTPException(status_code=404, detail="Student not found")

    async def update_student(self, student_id: int, student: Student):
        for index, s in enumerate(student):
            if s.id == student_id:
                self._data_set.students.students[index] = student
                return student
        raise HTTPException(status_code=404, detail="Student not found")

    async def delete_student(self, student_id: int):
        for index, e in enumerate(self.data_set.students):
            if e.id == student_id:
                del self._data_set.students.students[index]
                return {"detail": "Student deleted"}
        raise HTTPException(status_code=404, detail="Student not found")

    def generate_students(self):
        for student in self._data_set.students:
            yield student.json() + "\n"

    async def stream_students(self):
        return StreamingResponse(self.generate_students(), media_type="application/json")
