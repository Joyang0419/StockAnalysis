from app import db


class ModelAbstract(db.Model):
    __abstract__ = True

    def update_attr(self, attr: dict):
        """動態調整欄位"""
        for key, item in attr.items():
            setattr(self, key, item)
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(cls, **kwargs):
        """新增"""
        obj = cls(**kwargs)
        print(obj)
        db.session.add(obj)
        db.session.commit()
        return obj
