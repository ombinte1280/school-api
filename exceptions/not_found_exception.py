class NotFoundException(Exception):

    def __init__(self, resource):
        super().__init__(f"The resource : {resource} was not found.")