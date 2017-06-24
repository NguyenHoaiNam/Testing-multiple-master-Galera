from database import models
from database import repos

if __name__ == "__main__":
    engine = repos.get_engine()
    models.Base.metadata.create_all(engine)
