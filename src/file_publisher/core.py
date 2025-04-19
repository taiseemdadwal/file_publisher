# Backend logic for file publishing

import os
import shutil
import datetime
from sqlalchemy.orm import Session
from .models import FileRecord, PublishedSite

def publish_file(
    session: Session,
    source_path: str,
    owner: str,
    published_site: PublishedSite,
    is_infrastructure: bool,
    storage_dir: str = "managed_files"
):
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file does not exist: {source_path}")
    os.makedirs(storage_dir, exist_ok=True)
    filename = os.path.basename(source_path)
    target_path = os.path.join(storage_dir, filename)
    shutil.copy2(source_path, target_path)
    size_in_bytes = os.path.getsize(target_path)
    size_in_mb = round(size_in_bytes / (1024 * 1024), 2)
    file_record = FileRecord(
        filename=filename,
        owner=owner,
        filepath=target_path,
        on_disk=True,
        published_site=published_site,
        size_in_mb=size_in_mb,
        is_infrastructure=is_infrastructure,
        published_at=datetime.datetime.utcnow()
    )
    session.add(file_record)
    session.commit()
    session.refresh(file_record)
    return file_record

def get_all_records(session: Session):
    return session.query(FileRecord).all()
