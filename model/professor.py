from pydantic import BaseModel


class Professor(BaseModel):

    id: int
    firstname: str
    lastname: str
    age: int
    subject: str

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Subject : {self.get_subject}"

