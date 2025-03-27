from fastapi import FastAPI

from data_set import Dataset
from endpoint.class_room_endpoint import ClassRoomEndpoint
from endpoint.professor_endpoint import ProfessorEnpoint
from endpoint.student_endpoint import StudentEndpoint

app = FastAPI()
data_set = Dataset()
student_endpoint = StudentEndpoint(data_set, app)
professor_endpoint = ProfessorEnpoint(data_set, app)
class_room_endpoint = ClassRoomEndpoint(data_set, app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)