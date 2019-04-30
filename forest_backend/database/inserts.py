""" Module to insert some default data in database as well as some test data """
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from .models.tree_level_model import TreeLevel
from .models.seed_model import Seed
from .models.tree_model import Tree
from .models.branch_model import Branch

# engine = create_engine("postgresql://jasons:password@localhost/forest")
# Session = sessionmaker(bind=engine)
# session = Session()

# pylint: disable=C0103
def populate(db):
    """ Default data for database """
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
    """ Test data for test database """
    # Create Seeds
    seed1 = Seed(word="floral")
    seed2 = Seed(word="minimal")
    seed3 = Seed(word="temptation")
    db.session.add(seed1)
    db.session.add(seed2)
    db.session.add(seed3)
    db.session.flush()
    db.session.refresh(seed1)
    db.session.refresh(seed2)

    # Create Trees
    tree1 = Tree(seed1.id)
    tree2 = Tree(seed2.id)
    tree2.level_id = 1
    db.session.add(tree1)
    db.session.add(tree2)
    db.session.commit()

    # Create Branches
    branch1 = Branch('kitten', 1)
    branch2 = Branch('molten', 2)
    db.session.add(branch1)
    db.session.add(branch2)
    db.session.commit()
