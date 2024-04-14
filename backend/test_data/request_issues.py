import random

from functions import convert_str_to_date

def add_IssueRequests(db, Request, Issue):
    # request = Request(
    #     user_id = '',
    #     book_id = '',
    #     created_datetime = convert_str_to_date(''),
    #     return_datetime = convert_str_to_date(''),
    #     status = '',
    #     read = '',
    # )
    requests= [
        {'user_id': 6, 'book_id': 13,'created_datetime': convert_str_to_date('2024-03-28 17:22:12'), 'end_datetime': convert_str_to_date('2024-04-23 14:08:47'), 'status': 'denied', 'read': True},
        {'user_id': 2, 'book_id': 4, 'created_datetime': convert_str_to_date('2024-03-20 04:11:59'), 'end_datetime': convert_str_to_date('2024-04-07 11:39:21'), 'status': 'issued', 'read': False},
        {'user_id': 1, 'book_id': 9, 'created_datetime': convert_str_to_date('2024-03-25 15:37:02'), 'end_datetime': convert_str_to_date('2024-04-19 03:32:29'), 'status': 'issued', 'read': True},
        {'user_id': 5, 'book_id': 2, 'created_datetime': convert_str_to_date('2024-03-26 21:44:54'), 'end_datetime': convert_str_to_date('2024-04-16 12:17:14'), 'status': 'issued', 'read': True},
        {'user_id': 9, 'book_id': 3, 'created_datetime': convert_str_to_date('2024-03-23 19:59:45'), 'end_datetime': convert_str_to_date('2024-04-22 04:24:52'), 'status': 'issued', 'read': False},
        {'user_id': 8, 'book_id': 7, 'created_datetime': convert_str_to_date('2024-03-21 09:27:32'), 'end_datetime': convert_str_to_date('2024-04-05 19:13:50'), 'status': 'issued', 'read': False},
        {'user_id': 10,'book_id': 1, 'created_datetime': convert_str_to_date('2024-03-24 08:49:32'), 'end_datetime': convert_str_to_date('2024-04-16 23:03:42'), 'status': 'pending', 'read': True},
        {'user_id': 7, 'book_id': 12,'created_datetime': convert_str_to_date('2024-03-27 13:55:41'), 'end_datetime': convert_str_to_date('2024-04-10 18:31:57'), 'status': 'denied', 'read': True},
        {'user_id': 11,'book_id': 5, 'created_datetime': convert_str_to_date('2024-03-22 12:04:55'), 'end_datetime': convert_str_to_date('2024-04-19 08:27:44'), 'status': 'pending', 'read': False},
        {'user_id': 3, 'book_id': 11,'created_datetime': convert_str_to_date('2024-03-19 06:30:21'), 'end_datetime': convert_str_to_date('2024-04-06 10:59:05'), 'status': 'issued', 'read': False},
    ]
    for request in requests:
        db.session.add(Request(**request))
    db.session.commit()


    # issue = Issue(
    #     user_id = '',
    #     book_id = '',
    #     created_datetime = '',
    #     return_datetime = '',
    #     status = '',
    # )
    issues = [ # 2, 3, 4, 5, 6, 9, 10
        {'user_id':2, 'book_id':14,'created_datetime':convert_str_to_date('2024-03-20 04:11:59'), 'revoke_datetime':convert_str_to_date('2024-04-07 11:39:21'),},
        {'user_id':1, 'book_id':9, 'created_datetime':convert_str_to_date('2024-03-25 15:37:02'), 'revoke_datetime':convert_str_to_date('2024-04-19 03:32:29'),},
        {'user_id':5, 'book_id':2, 'created_datetime':convert_str_to_date('2024-03-26 21:44:54'), 'revoke_datetime':convert_str_to_date('2024-04-16 12:17:14'),},
        {'user_id':9, 'book_id':3, 'created_datetime':convert_str_to_date('2024-03-23 19:59:45'), 'revoke_datetime':convert_str_to_date('2024-04-22 04:24:52'),},
        {'user_id':8, 'book_id':7, 'created_datetime':convert_str_to_date('2024-03-21 09:27:32'), 'revoke_datetime':convert_str_to_date('2024-04-05 19:13:50'),},
        {'user_id':10,'book_id':16,'created_datetime':convert_str_to_date('2024-03-22 12:04:55'), 'revoke_datetime':convert_str_to_date('2024-04-19 08:27:44'),},
        {'user_id':3, 'book_id':11,'created_datetime':convert_str_to_date('2024-03-19 06:30:21'), 'revoke_datetime':convert_str_to_date('2024-04-06 10:59:05'),},
    ]
    for issue in issues:
        db.session.add(Issue(**issue))
    db.session.commit()