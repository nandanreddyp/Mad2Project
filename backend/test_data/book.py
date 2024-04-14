from functions import convert_str_to_date, get_unique_filename, extract_first_page_as_png
import os, shutil

def add_books(db, Book, Section, Author):
    print('Adding books, may take some while')
    pdf_name = 'book1.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book1 = Book(
        name='Rich Dad Poor Dad: What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!',
        description='Rich Dad Poor Dad is Robert Kiyosaki\'s story of growing up with two influential figures in his life: his "rich dad" - his best friend\'s father, who became his mentor - and his "poor dad" - his biological father, who was well-educated but struggled financially. The book contrasts the financial philosophies and practices of these two men, offering valuable lessons on wealth accumulation, investing, and financial independence.',
        page_count=336,
        publication_date=convert_str_to_date('1997-4-1'),
        isbn='978-1612680194',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book1)
    pdf_name = 'book2.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book2 = Book(
        name='Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time',
        description='Eat That Frog! is a time management and productivity book by Brian Tracy. It provides practical strategies and techniques to overcome procrastination, prioritize tasks effectively, and achieve greater productivity. The book offers 21 actionable principles to help readers tackle their most challenging tasks and accomplish more in less time.',
        page_count=144,
        publication_date=convert_str_to_date('2001-1-1'),
        isbn='978-1576754221',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book2)
    pdf_name = 'book3.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book3 = Book(
        name='The 48 Laws of Power',
        description='The 48 Laws of Power is a book by Robert Greene that explores the dynamics of power and how it can be acquired, maintained, and utilized. Greene distills timeless lessons from historical figures and their strategies for attaining and wielding power. The book offers practical advice on navigating power dynamics, understanding human nature, and achieving success in various spheres of life.',
        page_count=452,
        publication_date=convert_str_to_date('1998-09-01'),
        isbn='978-0140280197',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book3)
    pdf_name = 'book4.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book4 = Book(
        name='How to Win Friends and Influence People',
        description='How to Win Friends and Influence People is a self-help book by Dale Carnegie that offers practical advice on improving interpersonal relationships, communication skills, and influencing others. Carnegie\'s timeless principles focus on building rapport, showing genuine interest in others, and fostering positive interactions. The book provides actionable strategies for success in both personal and professional life, emphasizing the importance of empathy, kindness, and understanding in achieving one\'s goals.',
        page_count=288,
        publication_date=convert_str_to_date('1936-10-24'),
        isbn='978-0671027032',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book4)
    pdf_name = 'book5.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book5 = Book(
        name='Oil Painting For Dummies',
        description='Oil Painting For Dummies is a comprehensive guide to oil painting techniques and practices for beginners and enthusiasts alike. The book covers essential topics such as materials and tools, color theory, composition, brushwork, and more. With step-by-step instructions and helpful tips, it offers practical advice for creating stunning oil paintings, whether you\'re a novice or experienced artist. Whether you want to learn the basics or refine your skills, this book provides the knowledge and inspiration you need to unleash your creativity on canvas.',
        page_count=384,
        publication_date=convert_str_to_date('2008-07-28'),
        isbn='978-0470182308',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book5)
    pdf_name = 'book6.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book6 = Book(
        name='Data Structures and Algorithms in Java',
        description='Data Structures and Algorithms in Java is a comprehensive textbook that covers fundamental concepts of data structures and algorithms using the Java programming language. The book provides in-depth explanations of various data structures such as arrays, linked lists, trees, graphs, and algorithms such as sorting, searching, and recursion. With clear explanations, examples, and exercises, it is suitable for students, programmers, and anyone interested in mastering data structures and algorithms with Java.',
        page_count=736,
        publication_date=convert_str_to_date('2017-02-21'),
        isbn='978-1118771334',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book6)
    pdf_name = 'book7.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book7 = Book(
        name='Hacking For Dummies',
        description='Hacking For Dummies is a beginner-friendly guide to the world of hacking and cybersecurity. The book covers various topics such as computer security, penetration testing, ethical hacking, and common hacking techniques. With practical examples, step-by-step instructions, and tips for staying safe online, it offers readers insight into the world of cybersecurity and how hackers operate. Whether you\'re a curious beginner or an aspiring cybersecurity professional, this book provides a comprehensive introduction to hacking and cybersecurity concepts.',
        page_count=408,
        publication_date=convert_str_to_date('2013-04-22'),
        isbn='978-1118380932',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book7)
    pdf_name = 'book8.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book8 = Book(
        name="The Man's Guide to Women: Scientifically Proven Secrets from the 'Love Lab' About What Women Really Want",
        description="The Man's Guide to Women is a relationship guide written by John Gottman, Ph.D., and Julie Schwartz Gottman, Ph.D. Based on research conducted at the renowned 'Love Lab,' the book offers scientifically proven insights into what women truly want in relationships. It covers topics such as communication, understanding emotions, building trust, and maintaining intimacy. With practical advice and actionable strategies, it helps men understand and navigate the complexities of relationships with women.",
        page_count=224,
        publication_date=convert_str_to_date('2016-02-02'),
        isbn='978-1623361846',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book8)
    pdf_name = 'book9.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book9 = Book(
        name="What Women Want in a Man: How to Become the Alpha Male Women Respect, Desire, and Want to Submit To",
        description="What Women Want in a Man is a relationship guide written by Bruce Bryans. The book provides insights into what women desire in a partner and offers strategies for men to become the type of man that women respect, desire, and want to submit to. It covers topics such as confidence, masculinity, emotional intelligence, and understanding female psychology. With practical advice and actionable tips, it aims to help men improve their dating and relationship success.",
        page_count=156,
        publication_date=convert_str_to_date('2013-05-01'),
        isbn='978-1482304479',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book9)
    pdf_name = 'book10.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book10 = Book(
        name="How to Make Anyone Like You: Proven Ways to Become a People Magnet",
        description="How to Make Anyone Like You is a book by Leil Lowndes that offers practical strategies and techniques for improving interpersonal relationships and making a positive impression on others. The book covers topics such as communication skills, body language, rapport-building, and charisma. With actionable advice and real-life examples, it provides readers with the tools they need to become more likable and influential in various social situations.",
        page_count=336,
        publication_date=convert_str_to_date('2005-06-07'),
        isbn='978-0809229897',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book10)
    pdf_name = 'book11.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book11 = Book(
        name="Machine Learning For Dummies",
        description="Machine Learning For Dummies is a beginner-friendly guide to the field of machine learning written by John Paul Mueller and Luca Massaron. The book covers fundamental concepts of machine learning, including supervised and unsupervised learning, neural networks, deep learning, and practical applications. With clear explanations, hands-on examples, and real-world case studies, it offers readers a comprehensive introduction to machine learning concepts and techniques.",
        page_count=432,
        publication_date=convert_str_to_date('2016-05-31'),
        isbn='978-1119245513',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book11)
    pdf_name = 'book12.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book12 = Book(
        name="Data Science For Dummies",
        description="Data Science For Dummies is a comprehensive guide to the field of data science written by Lillian Pierson. The book covers essential concepts of data science, including data analysis, machine learning, big data, and data visualization. With practical examples and hands-on exercises, it provides readers with the knowledge and skills needed to succeed in the field of data science.",
        page_count=384,
        publication_date=convert_str_to_date('2015-04-13'),
        isbn='978-1118841556',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book12)
    pdf_name = 'book13.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book13 = Book(
        name="AI For Dummies",
        description="AI For Dummies is an introductory guide to artificial intelligence written by John Paul Mueller and Luca Massaron. The book covers basic concepts of AI, including machine learning, neural networks, natural language processing, and robotics. With easy-to-understand explanations and practical examples, it offers readers an accessible introduction to the field of artificial intelligence.",
        page_count=352,
        publication_date=convert_str_to_date('2018-05-01'),
        isbn='978-1119467656',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book13)
    pdf_name = 'book14.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book14 = Book(
        name="Srimad Bhagavad Gita",
        description="Srimad Bhagavad Gita, often referred to as the Gita, is a sacred Hindu scripture that is part of the Indian epic Mahabharata. It consists of a conversation between Prince Arjuna and the god Krishna, who serves as his charioteer. The Gita addresses the moral and philosophical dilemmas faced by Arjuna on the battlefield of Kurukshetra and provides guidance on duty, righteousness, and the path to spiritual liberation. It is considered one of the most important texts in Hindu philosophy and is revered by millions of people around the world.",
        page_count=700,
        # publication_date=convert_str_to_date('2018-05-01'),
        # isbn='978-1119467656',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book14)
    pdf_name = 'book15.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book15 = Book(
        name="Holy Bible",
        description="The Holy Bible is the sacred scripture of Christianity, consisting of the Old Testament and the New Testament. It is divided into various books, including historical accounts, poetry, prophecy, teachings, and letters. The Bible is considered the inspired word of God by Christians and serves as a guide for faith and practice. It contains religious teachings, moral guidelines, and accounts of the life and teachings of Jesus Christ.",
        page_count=700,
        # publication_date=convert_str_to_date('2018-05-01'),
        # isbn='978-1119467656',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book15)
    pdf_name = 'book16.pdf'
    source = os.path.join(os.getcwd(),'test_data','files','book','pdf',pdf_name)
    file_name = get_unique_filename(pdf_name)
    destiny = os.path.join(os.getcwd(),'static','pdfs',file_name)
    shutil.copy(source,destiny)
    image_path = os.path.join(os.getcwd(),'static','images','books',file_name.split('.')[0]+'.png')
    extract_first_page_as_png(destiny,image_path)
    book16 = Book(
        name="Quran",
        description="The Quran is the central religious text of Islam, considered by Muslims to be the literal word of God as revealed to the Prophet Muhammad. It is divided into chapters called surahs, which are further divided into verses called ayahs. The Quran covers a wide range of topics, including theology, morality, law, guidance for personal conduct, and stories of previous prophets. It serves as the primary source of Islamic teachings and is revered by Muslims worldwide.",
        page_count=700,
        # publication_date=convert_str_to_date('2018-05-01'),
        # isbn='978-1119467656',
        img_path = '/static/images/books/'+file_name.split('.')[0]+'.png',
        pdf_path = '/static/pdfs/'+file_name
    ); db.session.add(book16)

    db.session.commit()

    ## add book_section associations

    #  Personality devlopment
    section1 = db.session.get(Section,1)
    section1.books.extend([book1,book2,book3,book4])
        # rich dad poor dad ~
        # eat that frog ~
        # 48 laws of power ~
        # how to win friends and influence people ~
    # Art
    section2 = db.session.get(Section,2)
    section2.books.extend([book5])
        # oil painintng for dummies ~
    # Programming
    section3 = db.session.get(Section,3)
    section3.books.extend([book6,book7])
        # data structres and algorithms java ~
        # hacking for dummies ~
    # Dating
    section4 = db.session.get(Section,4)
    section4.books.extend([book8,book9,book10])
        # The man's guide to women ~
        # What women want in a man ~
        # How to make anyone like you ~
    # Data Science
    section5 = db.session.get(Section,5)
    section5.books.extend([book11,book12,book13])
        # Machine learning for dummies ~
        # Data science for dummies ~
        # ai for dummies ~
    # Religion
    section6 = db.session.get(Section,6)
    section6.books.extend([book14,book15,book16])
        # srimad bhagavad gita
        # holy bible
        # quran arabic english
    
    db.session.commit()

    ## add book_authro association 
    author1 = db.session.get(Author,1)
    author1.books.extend([book1])

    author2 = db.session.get(Author,2)
    author2.books.extend([book1])

    author3 = db.session.get(Author,3)
    author3.books.extend([book3])

    author4 = db.session.get(Author,4)
    author4.books.extend([book2])

    author5 = db.session.get(Author,5)
    author5.books.extend([book5,book11,book12,book13])

    author6 = db.session.get(Author,6)
    author6.books.extend([book4,book7])

    author7 = db.session.get(Author,7)
    author7.books.extend([book10])

    db.session.commit()

