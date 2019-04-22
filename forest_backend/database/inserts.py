from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from forest_backend.database.models.tree_level_model import TreeLevel
from forest_backend.database.models.seed_model import Seed

# engine = create_engine("postgresql://jasons:password@localhost/forest")
# Session = sessionmaker(bind=engine)
# session = Session()

def populate(db):
    # Default values for TreeLevel
    seed = TreeLevel(0, "seed")
    sprout = TreeLevel(1, "sprout")
    seedling = TreeLevel(2, "seedling")
    sapling = TreeLevel(3, "sapling")
    mature = TreeLevel(4, "mature")
    ancient = TreeLevel(5, "ancient")
    snag = TreeLevel(6, "snag")

    db.session.merge(seed)
    db.session.merge(sprout)
    db.session.merge(seedling)
    db.session.merge(sapling)
    db.session.merge(mature)
    db.session.merge(ancient)
    db.session.merge(snag)
    # End default TreeLevel

    db.session.commit()
    db.session.close()

def populate_test_data(db):
    # Create Seeds
    seed1 = Seed(word="floral")
    seed2 = Seed(word="minimal")
    db.session.add(seed1)
    db.session.add(seed2)
    db.session.commit()