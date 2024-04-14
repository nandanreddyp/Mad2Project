from functions import get_unique_filename, convert_str_to_date
import shutil, os

def add_users(db, User):
    image_name = 'user1.png'
    source = os.path.join(os.getcwd(),'test_data','files','profile',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','profiles',file_name)
    shutil.copy(source,destiny)
    user1 = User(
            email='user1@example.com',
            f_name='Maya',
            l_name='Mahadevi',
            created_datetime=convert_str_to_date('2024-03-15 08:30:00'),
            last_login=convert_str_to_date('2024-03-31 08:30:00'),
            img_path='/static/images/profiles/'+file_name,
            
        )
    db.session.add(user1)
    user1.hash_password('12345678')
    user2 = User(
            email='user2@example.com',
            f_name='Jivraj Singh',
            l_name='Shekawat',
            created_datetime=convert_str_to_date('2024-02-28 15:45:00'),
            last_login=convert_str_to_date('2024-03-30 15:45:00'),
            
        )
    db.session.add(user2)
    user2.hash_password('12345678')
    image_name = 'user3.png'
    source = os.path.join(os.getcwd(),'test_data','files','profile',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','profiles',file_name)
    shutil.copy(source,destiny)
    user3 = User(
            email='user3@example.com',
            f_name='Ramanamma',
            l_name='Chakali',
            created_datetime=convert_str_to_date('2024-03-10 12:10:00'),
            last_login=convert_str_to_date('2024-03-29 12:10:00'),
            img_path='/static/images/profiles/'+file_name,
            
        )
    db.session.add(user3)
    user3.hash_password('12345678')
    image_name = 'user4.png'
    source = os.path.join(os.getcwd(),'test_data','files','profile',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','profiles',file_name)
    shutil.copy(source,destiny)
    user4 = User(
            email='user4@example.com',
            f_name='Mallamma',
            l_name='Posham',
            created_datetime=convert_str_to_date('2024-03-01 09:20:00'),
            last_login=convert_str_to_date('2024-03-28 09:20:00'),
            img_path='/static/images/profiles/'+file_name,
            
        )
    db.session.add(user4)
    user4.hash_password('12345678')
    user5 = User(
            email='user5@example.com',
            f_name='Urjaswi',
            l_name='Banerjee',
            created_datetime=convert_str_to_date('2024-02-14 14:50:00'),
            last_login=convert_str_to_date('2024-03-27 14:50:00'),
            img_path='/user_images/sophiawilliams.png',
            
        )
    db.session.add(user5)
    user5.hash_password('12345678')
    image_name = 'user6.png'
    source = os.path.join(os.getcwd(),'test_data','files','profile',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','profiles',file_name)
    shutil.copy(source,destiny)
    user6 = User(
            email='user6@example.com',
            f_name='Rohit',
            l_name='Mondal',
            created_datetime=convert_str_to_date('2024-03-05 11:30:00'),
            last_login=convert_str_to_date('2024-03-26 11:30:00'),
            img_path='/static/images/profiles/'+file_name,
            
        )
    db.session.add(user6)
    user6.hash_password('12345678')
    image_name = 'user7.png'
    source = os.path.join(os.getcwd(),'test_data','files','profile',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','profiles',file_name)
    shutil.copy(source,destiny)
    user7 = User(
            email='user7@example.com',
            f_name='Mohit Ali',
            l_name='Khan',
            created_datetime=convert_str_to_date('2024-02-29 17:15:00'),
            last_login=convert_str_to_date('2024-03-25 17:15:00'),
            img_path='/static/images/profiles/'+file_name,
            
        )
    db.session.add(user7)
    user7.hash_password('12345678')
    user8 = User(
            email='user8@example.com',
            f_name='Vamsi Krishna',
            l_name='Nayakal',
            created_datetime=convert_str_to_date('2024-03-20 10:40:00'),
            last_login=convert_str_to_date('2024-03-24 10:40:00'),
            img_path='/user_images/danielmartinez.png',
            
        )
    db.session.add(user8)
    user8.hash_password('12345678')
    image_name = 'user9.png'
    source = os.path.join(os.getcwd(),'test_data','files','profile',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','profiles',file_name)
    shutil.copy(source,destiny)
    user9 = User(
            email='user9@example.com',
            f_name='Eshwar',
            l_name='Reddy',
            created_datetime=convert_str_to_date('2024-02-29 13:20:00'),
            last_login=convert_str_to_date('2024-03-23 13:20:00'),
            img_path='/static/images/profiles/'+file_name,
            
        )
    db.session.add(user9)
    user9.hash_password('12345678')
    image_name = 'user10.png'
    source = os.path.join(os.getcwd(),'test_data','files','profile',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','profiles',file_name)
    shutil.copy(source,destiny)
    user10 = User(
            email='user10@example.com',
            f_name='Nandeesh',
            l_name='',
            created_datetime=convert_str_to_date('2024-02-27 16:55:00'),
            last_login=convert_str_to_date('2024-03-22 16:55:00'),
            img_path='/static/images/profiles/'+file_name,
            
        )
    db.session.add(user10)
    user10.hash_password('12345678')
    
    db.session.commit()