# Author: Nam Nguyen Hoai
# coding: utf-8
import logging

from database import repos

sqla_logger = logging.getLogger('sqlalchemy.engine.base.Engine')
sqla_logger.disabled = True




TEST_NAME = 'name'


def main():
    while True:
        session2 = repos.get_session_2()
        records = repos.get_records(session2, TEST_NAME)
        print('number of rows database is: {}'.format(len(records)))


if __name__ == '__main__':
    main()
