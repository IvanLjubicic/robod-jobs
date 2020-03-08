from .db import db

class Check(db.EmbeddedDocument):
    date = db.DateField(required=True)
    changed = db.BooleanField(required=True)

class Issue(db.EmbeddedDocument):
    sud = db.StringField(required=True, unique=True)
    upisnik = db.StringField(required=True, unique=True)
    predmet = db.StringField(required=True, unique=True)
    godina = db.StringField(required=True, unique=True)
    checks = db.ListField(db.EmbeddedDocumentField(Check), required=False)

class LawFirm(db.Document):
    username = db.StringField(required=True, unique=True)
    name = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    contacts = db.ListField(db.StringField(), required=False)
    issues = db.ListField(db.EmbeddedDocumentField(Issue), required=False)