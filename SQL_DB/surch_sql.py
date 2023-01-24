import os
import sqlite3
from typing import List, Set


def execute_query(query_sql: str) -> List:
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def unwrapper(records: List) -> None:
    for record in records:
        print(*record)


def get_customers() -> None:
    query_sql = f'''
        SELECT customers.FirstName, max(LastName), max(Country), count(*) FROM customers
GROUP BY customers.FirstName;
    '''
    return unwrapper(execute_query(query_sql))


#get_customers()


def get_sum() -> None:
    query_sql = f'''
        SELECT *, sum(UnitPrice * Quantity) FROM invoice_items;
    '''
    return unwrapper(execute_query(query_sql))

#get_sum()


def main():
    get_customers()
    get_sum()

if __name__ == '__main__':
    main()
