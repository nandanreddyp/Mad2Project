from sqlalchemy import event

@event.listens_for(User,'')