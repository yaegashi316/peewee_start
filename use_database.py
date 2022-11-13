from database import Thread

Thread.create(name="Mina", title="Title", body="Body")

thread01 = Thread(name="Mina01", title="Title01", body="Body01")
thread01.save()
