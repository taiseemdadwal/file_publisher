import os
import tempfile
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from file_publisher.models import Base, PublishedSite
from file_publisher.core import publish_file, get_all_records

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        yield session

def test_publish_and_retrieve(session):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"testdata")
        f.flush()
        path = f.name
    rec = publish_file(
        session,
        source_path=path,
        owner="testuser",
        published_site=PublishedSite.van,
        is_infrastructure=False
    )
    records = get_all_records(session)
    assert len(records) == 1
    assert records[0].filename == os.path.basename(path)
    os.remove(path)
