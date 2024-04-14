from functions import get_unique_filename
import shutil, os

def add_sections(db, Section):
    image_name = 'section1.png'
    source = os.path.join(os.getcwd(),'test_data','files','section',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','sections',file_name)
    shutil.copy(source,destiny)
    section1 = Section(
        name = 'Personality Devlopment',
        description = 'Discover your path to personal growth and fulfillment with our Personality Development section. From mastering communication skills to building confidence and resilience, our carefully curated collection offers essential resources for self-improvement. Explore a variety of topics including leadership, emotional intelligence, and mindfulness, and embark on a journey of self-discovery and empowerment. With expert guidance and practical advice, these books are your roadmap to unlocking your true potential and living a more fulfilling life.',
        img_path = '/static/images/sections/'+file_name,
    )
    db.session.add(section1)
    image_name = 'section2.png'
    source = os.path.join(os.getcwd(),'test_data','files','section',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','sections',file_name)
    shutil.copy(source,destiny)
    section2 = Section(
        name = 'Art',
        description = "Unleash your creativity and immerse yourself in the captivating world of art with our Art Section. Dive into a diverse collection of books that celebrate the beauty and power of artistic expression across various mediums and genres. From renowned masterpieces to contemporary works, our selection covers painting, sculpture, photography, drawing, and more. Whether you're an aspiring artist, an art enthusiast, or simply seeking inspiration, our books offer insight, techniques, and appreciation for the rich tapestry of artistic endeavors. Explore the depths of creativity and discover new perspectives within our Art Section.",
        img_path = '/static/images/sections/'+file_name,
    )
    db.session.add(section2)
    image_name = 'section3.png'
    source = os.path.join(os.getcwd(),'test_data','files','section',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','sections',file_name)
    shutil.copy(source,destiny)
    section3 = Section(
        name = 'Dating',
        description = "Explore the world of relationships and romance with our Dating Section. Dive into a diverse selection of books designed to navigate the complexities of modern dating, offering insights into building meaningful connections, fostering intimacy, and navigating the ups and downs of romantic relationships. Whether you're looking for expert advice on finding love, improving communication skills, or navigating the world of online dating, our collection provides invaluable resources to help you navigate the journey of love and companionship with confidence and clarity.",
        img_path = '/static/images/sections/'+file_name,
    )
    db.session.add(section3)
    image_name = 'section4.png'
    source = os.path.join(os.getcwd(),'test_data','files','section',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','sections',file_name)
    shutil.copy(source,destiny)
    section4 = Section(
        name = 'Programming',
        description = "Embark on a journey of coding mastery with our Programming section. Dive into a world of endless possibilities as you explore books covering a wide range of programming languages, concepts, and technologies. Whether you're a novice looking to learn the basics or an experienced developer seeking to expand your skills, our collection has something for everyone. From beginner-friendly guides to advanced tutorials, our books offer step-by-step instructions, practical examples, and real-world projects to help you sharpen your coding abilities and stay ahead in today's fast-paced tech landscape. Get ready to unleash your creativity and build the future with our Programming section.",
        img_path = '/static/images/sections/'+file_name,
    )
    db.session.add(section4)
    image_name = 'section5.png'
    source = os.path.join(os.getcwd(),'test_data','files','section',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','sections',file_name)
    shutil.copy(source,destiny)
    section5 = Section(
        name = 'Data Science',
        description = "Dive into the dynamic world of data science with our comprehensive collection of books. From beginner-friendly introductions to advanced topics, our curated selection covers the entire spectrum of data science disciplines, including machine learning, artificial intelligence, big data analytics, and more. Whether you're looking to enhance your programming skills, delve into statistical analysis, or explore the latest trends in data visualization, our books provide invaluable insights and practical guidance. With contributions from leading experts in the field, our data science section is your gateway to mastering the tools and techniques needed to extract actionable insights from data and drive innovation in your projects and endeavors.",
        img_path = '/static/images/sections/'+file_name,
    )
    db.session.add(section5)
    image_name = 'section6.png'
    source = os.path.join(os.getcwd(),'test_data','files','section',image_name)
    file_name = get_unique_filename(image_name)
    destiny = os.path.join(os.getcwd(),'static','images','sections',file_name)
    shutil.copy(source,destiny)
    section6 = Section(
        name = 'Religion',
        description = "Dive into the rich tapestry of spiritual wisdom and explore the diverse beliefs and practices of humanity with our Religion section. From ancient texts to contemporary reflections, our collection offers a comprehensive array of books covering major world religions, philosophical inquiries, and spiritual traditions. Delve into the scriptures, rituals, and teachings that have shaped cultures and civilizations for centuries, and gain insight into the profound questions of existence, morality, and the divine. Whether you seek to deepen your faith, broaden your understanding of different religious perspectives, or embark on a journey of spiritual exploration, our Religion section invites you to engage with the profound and timeless wisdom of humanity's spiritual heritage.",
        img_path = '/static/images/sections/'+file_name,
    )
    db.session.add(section6)
    db.session.commit