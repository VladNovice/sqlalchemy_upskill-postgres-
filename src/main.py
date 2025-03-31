import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import asyncio

from queries.orm import create_tables, insert_workers
from queries.core import SyncCore

create_tables()
insert_workers()


SyncCore.select_workers()