import uuid


class Job:
    def __init__(self, data):
        self.id = str(uuid.uuid4())
        self.modelType = data['modelType']
        self.created = data['created']
        self.createdBy = data['createdBy']

    def __repr__(self):
        return f'Job(id={self.id})'
