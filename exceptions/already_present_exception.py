class AlReadyPresentException(Exception):

    def __init__(self, studend_id: int, class_room_id: int):
        super().__init__(f"The student with id {studend_id} is already assigne to the class {class_room_id}")