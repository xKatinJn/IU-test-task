from app import db


class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    patronymic = db.Column(db.String(64))
    works_from_date = db.Column(db.DateTime)
    salary = db.Column(db.Integer)
    is_chief = db.Column(db.Boolean)

    def __repr__(self):
        fields = vars(self)
        representation = [f' {key} = {fields[key]} ' for key in fields.keys()]
        return f'<Worker:{representation}>'


class ChiefWorkerRelations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chief_id = db.Column(db.Integer)
    worker_id = db.Column(db.Integer, unique=True)

    def get_chief_workers(self) -> list:
        return [Worker.query.filter_by(id=row.worker_id).first()
                for row in ChiefWorkerRelations.query.filter_by(chief_id=self.chief_id).all()]

    def __repr__(self):
        fields = vars(self)
        representation = [f' {key} = {fields[key]} ' for key in fields.keys()]
        return f'<ChiefWorkerRelations:{representation}>'
