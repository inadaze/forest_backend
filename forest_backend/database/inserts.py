from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from forest_backend.database.models.tree_level_model import TreeLevel

engine = create_engine("postgresql://jasons:password@localhost/forest")
Session = sessionmaker(bind=engine)
session = Session()

 # Default values for TreeLevel
seed = TreeLevel(0, "seed")
sprout = TreeLevel(1, "sprout")
seedling = TreeLevel(2, "seedling")
sapling = TreeLevel(3, "sapling")
mature = TreeLevel(4, "mature")
ancient = TreeLevel(5, "ancient")
snag = TreeLevel(6, "snag")

session.merge(seed)
session.merge(sprout)
session.merge(seedling)
session.merge(sapling)
session.merge(mature)
session.merge(ancient)
session.merge(snag)
# End default TreeLevel

session.commit()
session.close()