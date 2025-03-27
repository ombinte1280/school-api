from typing import List

from pydantic import BaseModel

from config.logger_cfg import logger
from exceptions.already_present_exception import AlReadyPresentException
from exceptions.not_found_exception import NotFoundException
from model.student import Student


class ClassRoom(BaseModel):

    id: int
    name: str
    head_teacher: int
    students: List[Student]

    def change_head_teacher(self, new_head_teacher):
        if self.__head_teacher == new_head_teacher:
            logger.warn(f"The professor with id {new_head_teacher} he is already the head teacher.")
        else:
            self.__head_teacher = new_head_teacher

    def add_student(self, student: Student):
        if self.__students.__contains__(self, new_student):
            raise AlReadyPresentException(self, studend_id=student.id, class_room_id=self.__id)
        self.__students.append(self, student)
        logger.info(f"the student {student} was added")

    def remove_student(self, student):
        if self.__students.__contains__(self, student):
            raise NotFoundException(self, student)
        self.__students.remove(self, student)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Students : {self.students}"
