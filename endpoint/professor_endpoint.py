from typing import List

from fastapi import FastAPI

from data_set import Dataset
from model.professor import Professor


class ProfessorEnpoint:

    def __init__(self, data_set: Dataset, app: FastAPI):
        self._data_set = data_set
        self._app = app
        self.register_routes()

    def register_routes(self):
        self._app.add_api_route("/professors/", self.create_professor, methods=["POST"], response_model=Professor)
        self._app.add_api_route("/professors/", self.get_all_professors, methods=["GET"], response_model=List[Professor])
        self._app.add_api_route("/professors/{professor_id}", self.get_professor, methods=["GET"], response_model=Professor)
        self._app.add_api_route("/professors/{professor_id}", self.update_professor, methods=["PUT"], response_model=Professor)
        self._app.add_api_route("/professors/{professor_id}", self.delete_professor, methods=["DELETE"])

    async def create_professor(self, professor: Professor):
        for p in self._data_set.professors:
            if p.id == professor.id:
                raise HTTPException(status_code=400, detail="Professor already exists!!")
        self._data_set.professors.append(professor)
        return professor

    async def get_all_professors(self):
        return self._data_set.professors

    async def get_professor(self, professor_id: int):
        for s in self._data_set.professors:
            if s.id == professor_id:
                return s
        raise HTTPException(status_code=404, detail="Professor not found")

    async def update_professor(self, professor_id: int, professor: Professor):
        for index, p in enumerate(self._data_set.professors()):
            if p.id == professor_id:
                self._data_set.professors[index] = professor
                return professor
        raise HTTPException(status_code=404, detail="Professor not found")

    async def delete_professor(self, professor_id: int):
        for index, p in enumerate(self._data_set.professors):
            if p.id == professor_id:
                del self._data_set.professors[index]
                return {"detail": "Professor deleted"}
        raise HTTPException(status_code=404, detail="Professor not found")
