""" Module to insert some default data in database as well as some test data """
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from .models.tree_level_model import TreeLevel
from .models.seed_model import Seed
from .models.tree_model import Tree
from .models.branch_model import Branch

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

def resetDatabase(engine):
   base = declarative_base()
   metadata = MetaData(engine, reflect=True)
   table = metadata.tables.get('branches')
   if table is not None:
        base.metadata.drop_all(engine, [table], checkfirst=True)
   table = metadata.tables.get('trees')
   if table is not None:
       base.metadata.drop_all(engine, [table], checkfirst=True)
   table = metadata.tables.get('seeds')
   if table is not None:
       base.metadata.drop_all(engine, [table], checkfirst=True)

def populate_test_data(db):
    """ Test data for test database """
    # Create Seeds
    seed1 = Seed("floral", "1,2,3")
    seed2 = Seed("minimal", '4,5,6')
    seed3 = Seed("temptation", '1,0,2')
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
