from functions import get_unique_filename
import shutil, os

def add_authors(db, Author):
    image_name = 'author1.png'
    source = os.path.join(os.getcwd(),'test_data','files','author',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','authors',file_name)
    shutil.copy(source,destiny)
    author1 = Author(
        name = 'Robert Kiyosaki', # personality dev
        description = "Robert Kiyosaki is an entrepreneur, investor, and author best known for his book \"Rich Dad Poor Dad,\" which has become one of the bestselling personal finance books of all time. Kiyosaki advocates for financial education and literacy, emphasizing the importance of investing, entrepreneurship, and financial independence. Through his books, seminars, and educational materials, he encourages individuals to adopt a mindset of wealth-building and to take control of their financial futures. Kiyosaki's teachings often challenge conventional wisdom about money and provide alternative perspectives on achieving financial success.",
        img_path = '/static/images/authors/'+file_name,
    )
    db.session.add(author1)
    image_name = 'author2.png'
    source = os.path.join(os.getcwd(),'test_data','files','author',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','authors',file_name)
    shutil.copy(source,destiny)
    author2 = Author(
        name = 'Sharon Lechter', # personality dev
        description = "Sharon Lechter is a prominent author, entrepreneur, and advocate for financial literacy. She is best known for co-authoring the renowned \"Rich Dad Poor Dad\" book series with Robert Kiyosaki. Through her work, Lechter has empowered countless individuals to take control of their financial futures and achieve success. She continues to inspire audiences worldwide through her books, speaking engagements, and efforts to promote financial education.",
        img_path = '/static/images/authors/'+file_name,
    )
    db.session.add(author2)
    image_name = 'author3.png'
    source = os.path.join(os.getcwd(),'test_data','files','author',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','authors',file_name)
    shutil.copy(source,destiny)
    author3 = Author(
        name = 'Robert Greene', # personality dev
        description = "Robert Greene is a renowned author celebrated for his insightful writings on power, strategy, and human behavior. His books, including \"The 48 Laws of Power\" and \"The Art of Seduction,\" delve into the dynamics of influence and manipulation, drawing from historical examples to provide practical advice for navigating social interactions. Greene's works have earned him a reputation as a leading authority on interpersonal relationships and the pursuit of mastery in various fields.",
        img_path = '/static/images/authors/'+file_name,
    )
    db.session.add(author3)
    image_name = 'author4.png'
    source = os.path.join(os.getcwd(),'test_data','files','author',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','authors',file_name)
    shutil.copy(source,destiny)
    author4 = Author(
        name = 'Brian Tracy', # personality dev
        description = "Brian Tracy is a highly respected author, speaker, and success coach known for his expertise in personal and professional development. His bestselling books, such as \"Eat That Frog!\" and \"Maximum Achievement,\" offer practical strategies for achieving goals and unlocking one's full potential. Through his motivational speeches and seminars, Tracy has inspired millions worldwide to take control of their lives and achieve success.",
        img_path = '/static/images/authors/'+file_name,
    )
    db.session.add(author4)
    image_name = 'author5.png'
    source = os.path.join(os.getcwd(),'test_data','files','author',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','authors',file_name)
    shutil.copy(source,destiny)
    author5 = Author(
        name = 'For Dummies', # multiple
        description = "The \"For Dummies\" series is a collection of instructional books covering a wide range of topics, written in a clear and accessible style. These books provide practical guidance and information on various subjects, making complex topics easier to understand for readers of all levels.",
        img_path = '/static/images/authors/'+file_name,
    )
    db.session.add(author5)
    image_name = 'author6.png'
    source = os.path.join(os.getcwd(),'test_data','files','author',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','authors',file_name)
    shutil.copy(source,destiny)
    author6 = Author(
        name = 'Dale Carnegle', # personality dev
        description = "Dale Carnegie was a renowned writer and lecturer best known for his influential self-help book \"How to Win Friends and Influence People.\" Published in 1936, this timeless classic offers practical advice on interpersonal skills, communication, and leadership. Carnegie's principles emphasize the importance of empathy, kindness, and understanding in building successful relationships, both professionally and personally. His teachings continue to inspire millions worldwide to improve their social interactions, enhance their communication skills, and achieve greater success in life.",
        img_path = '/static/images/authors/'+file_name,
    )
    db.session.add(author6)
    image_name = 'author7.png'
    source = os.path.join(os.getcwd(),'test_data','files','author',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','authors',file_name)
    shutil.copy(source,destiny)
    author7 = Author(
        name = 'Leli Lowndes',
        description = "Leil Lowndes is an author and communication expert known for her expertise in interpersonal skills and social interactions. Her books, such as \"How to Talk to Anyone\" and \"How to Make Anyone Like You,\" provide practical strategies and techniques for improving communication, building rapport, and creating positive connections with others. Lowndes' work often focuses on body language, conversational skills, and social dynamics, offering readers valuable insights into the art of effective communication. Her books have gained widespread popularity and have helped countless individuals improve their interpersonal relationships and social confidence.",
        img_path = '/static/images/authors/'+file_name,
    )
    db.session.add(author7)
    db.session.commit()