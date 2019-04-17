from forest_backend.database.sql_db import db
from forest_backend.database.models.tree_level_model import TreeLevel

#TODO: This needs to be added to the database so I can create new trees

seed = TreeLevel(0, "seed")
sprout = TreeLevel(1, "sprout")
seedling = TreeLevel(2, "seedling")
sapling = TreeLevel(3, "sapling")
mature = TreeLevel(4, "mature")
ancient = TreeLevel(5, "ancient")
snag = TreeLevel(6, "snag")

db.session.add(seed)
db.session.add(sprout)
db.session.add(seedling)
db.session.add(sapling)
db.session.add(mature)
db.session.add(ancient)
db.session.add(snag)

db.session.commit()
db.session.close()