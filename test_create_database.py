# Author: Nam Nguyen Hoai
# coding: utf-8
import logging

from database import models
from database import repos

sqla_logger = logging.getLogger('sqlalchemy.engine.base.Engine')
sqla_logger.disabled = True
TEST_NAME = 'name'


def main():
    session = repos.get_session()
    for i in range(10000):
        test_table = models.TestTable(name='{}_{}'.format(TEST_NAME, i))
        session.add(test_table)
    session.commit()
    # Start query to Database with the name
    # session2 = repos.get_session_2()
    # records = repos.get_records(session2, TEST_NAME)
    # print('Name after query database is: {}'.format(records))


if __name__ == '__main__':
    main()
