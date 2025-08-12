class post():
    def __init__(self,*args,**kwargs):
        self.userId = kwargs['userId']
        self.id = kwargs['id']
        self.title = kwargs['title']
        self.body = kwargs['body']

    def to_dict(self):
        return {
            'userId': self.userId,
            'id': self.id,
            'title': self.title,
            'body': self.body
        }
