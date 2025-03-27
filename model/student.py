from typing import List

from pydantic import BaseModel

from config.logger_cfg import logger


class Student(BaseModel):

    id: int
    firstname: str
    lastname: str
    age: int
    notes: List[float]

    def get_average(self):
        if not self._notes:
            return 0
        total = sum(self._notes)
        average = total / len(self._notes)
        logger.info(f"Average of student {self.firstname} {self.lastname} is: {average}")
        return average

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Notes : {self._notes}"

