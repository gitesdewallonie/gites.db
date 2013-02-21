# -*- coding: utf-8 -*-
import sys
from alembic import config
import os.path


def main(argv=None, prog=None, **kwargs):
    current_path = os.path.dirname(__file__)
    gdw_alembic_config_file = os.path.join(current_path, 'alembic.ini')
    argv = ['-c', gdw_alembic_config_file]
    argv.extend(sys.argv[1:])
    config.main(argv, prog, **kwargs)
    return 0
