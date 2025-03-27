from typing import List

from fastapi import FastAPI

from data_set import Dataset
from model.class_room import ClassRoom


class ClassRoomEndpoint:
    def __init__(self, data_set: Dataset, app: FastAPI):
        self._data_set = data_set
        self._app = app
        self.register_routes()


    def register_routes(self):
        self._app.add_api_route("/classes/", self.create_class, methods=["POST"], response_model=ClassRoom)
        self._app.add_api_route("/classes/", self.get_all_classrooms, methods=["GET"], response_model=List[ClassRoom])
        self._app.add_api_route("/classes/{class_id}", self.get_class_room, methods=["GET"], response_model=ClassRoom)
        self._app.add_api_route("/classes/{class_id}", self.update_class_room, methods=["PUT"], response_model=ClassRoom)
        self._app.add_api_route("/classes/{class_id}", self.delete_class_room, methods=["DELETE"])

    async def create_class(self, class_room: ClassRoom):
        for c in self._data_set.classes:
            if c.id == class_room.id:
                raise HTTPException(status_code=400, detail="class already exists!!")
        self._data_set.classes.append(class_room)
        return class_room

    async def get_all_classrooms(self):
        return self._data_set.classes

    async def get_class_room(self, classe_id: int):
        for c in self._data_set.classes:
            if c.id == classe_id:
                return c
        raise HTTPException(status_code=404, detail="classe not found")

    async def update_class_room(self, class_id: int, class_room: ClassRoom):
        for index, c in enumerate(self._data_set.classes):
            if c.id == class_id:
                self._data_set.classes[index] = class_room
                return class_room
        raise HTTPException(status_code=404, detail="classe not found")

    async def delete_class_room(self, class_id: int):
        for index, c in enumerate(self._data_set.classes):
            if c.id == class_id:
                del self._data_set.classes[index]
                return {"detail": "classe deleted"}
        raise HTTPException(status_code=404, detail="class not found")