import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
import random
import string
from Etpaly_Orders.models import *
from utils.generate_code import generate_code,generate_sku


# def seed_Customer(n):
#     fake=Faker()
#     # CAT=('Creative','Design','Marketing','Administration','Teaching' , 'Education','Engineering','Software','Web','Telemarketing')
#     for _ in range(n):
#         Customer.objects.create(
#             name=fake.name(),
#             phone=generate_code(),
#             location=fake.address(),
#         )
#     print(f"{n} seed_Customer ")
    
# seed_Customer(25)
# fake=Faker()
# username=fake.name()
# first_name = username.split()[0]
# last_name = username.split()[1]
# print(username,first_name,last_name)


# def seed_product(n):
#     fake = Faker()# 
#     # CAT=('Creative','Design','Marketing','Administration','Teaching' , 'Education','Engineering','Software','Web','Telemarketing')
#     for _ in range(n):
#         Product.objects.create(
#             name=f'product {fake.ean(length=8)}',
#             price=round(random.uniform(10.99,100.99),2) ,
#             sku=generate_sku(),
#             subtitle=fake.text(max_nb_chars=300),
#         )
#     print(f"{n} seed_Product ")
    
# seed_product(100)


def seed_Order(n):
    fake = Faker()# 
    status=('Created','Confirmed', 'Processed','Shipped','Delivered')  

    for _ in len(Order.objects.all()):
        Order.objects.create(
            status=status[random.randint(0,4)],
            customer=Customer.objects.get(id=random.randint(1,70)),
            delivery_date=fake.date_time_this_year(),
            discount=random.randint(1,10) ,
            Delivery_Fee=round(random.uniform(10,20),2) ,
        )
    print(f"{n} seed_Order ")
    
seed_Order(200)

# def seed_OrderDetail(n):
#     fake = Faker()# 
#     for _ in range(n):
#         OrderDetail.objects.create(
#             order=Order.objects.get(id=random.randint(1,230)),
#             product=Product.objects.get(id=random.randint(1,100)),
#             quantity=random.randint(1,50) ,
#             price=round(random.uniform(20.99,150.99),2) ,
#         )
#     print(f"{n} seed_OrderDetail ")
    
# seed_OrderDetail(200)


# def seed_Job_Company(n):
#     fake=Faker()
#     COMP=('Amazon','Apple'
#     'Microsoft'
#     ,'Google',
#     'Facebook',
#     'Tesla',
#     'Coca-Cola',
#     "McDonald's",
#     'Toyota',
#     'Samsung',
#     'Nike',
#     'Procter & Gamble',
#     'IBM',
#     'Intel',
#     'General Electric',
#     'PepsiCo',
#     'Visa',
#     'Mastercard',
#     'JPMorgan Chase',)
#     ICON=['1.svg','1.svg','3.svg','4.svg','5.svg']
#     for _ in range(n):
#         Job_Company.objects.create(
#         name=COMP[random.randint(0,18)],
#         icon=ICON[random.randint(0,4)],
#         Fb_link='https://www.facebook.com/',
#         Gm_link='https://www.gmail.com/',
#         Tw_link='https://www.twiter.com/',
#         Yb_link='https://www.youtub.com/',
#         )
#     print(f"{n} Job_Company seed ")
# seed_Job_Company(50)



# def seed_job(n):
#     fake=Faker()
#     IMAGE=['1.svg','1.svg','3.svg','4.svg','5.svg']
#     JOB_TYPE=['Full_Time','Part_Time','Remotely']
#     for _ in range(n):
#         Job.objects.create(
#             author=User.objects.get(id=1),
#             title=f'{fake.name()} JOB',
#             image=IMAGE[random.randint(0,4)],
#             location=fake.address(),
#             company=Job_Company.objects.get(id=random.randint(1,49)),
#             category=Category.objects.get(id=random.randint(1,23)),
#             job_type=JOB_TYPE[random.randint(0,2)],
#             vacancy=random.randint(1,10),
#             salary=random.randint(5000,25000),
#             description=fake.text(max_nb_chars=1000),
#             Qualification=fake.text(max_nb_chars=1000),
#             Responsibility=fake.text(max_nb_chars=1000),
#             Benefits=fake.text(max_nb_chars=1000),
#         )
#     print(f"{n} JOB seed ")

# seed_job(500)


# def seed_Candidates(n):
#     fake=Faker()
#     IMAGE=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
#     for _ in range(n):
#         Candidates.objects.create(
#         job=Job.objects.get(id=random.randint(1,499)),
#         name=fake.name(),
#         email= f"{fake.name()}_{str(random.randint(1975,2002))}@gmail.com".lower(),
#         image=f"Candidates/{IMAGE[random.randint(0,9)]}",
#         linkedin='https://www.linkedin.com/',
#         cv="Candidates/0911-learning-django.pdf",
#         cover=fake.text(max_nb_chars=1000),
#         )
#     print(f"{n} Candidates seed ")

# seed_Candidates(100)


# def seed_Post(n):
#     fake=Faker()
#     # IMAGE=['post_1.png','post_2.png','post_3.png','post_4.png','post_5.png','post_6.png','post_7.png','post_8.png','post_9.png','post_10.png']
#     for _ in range(n):
#         Post.objects.create(
#         # author=User.objects.get(id=1),
#         # title=f'{fake.name()} Post',
#         # subtitle=fake.text(max_nb_chars=150),
#         # article=fake.text(max_nb_chars=2500),
#         # image=f"posts/{IMAGE[random.randint(0,9)]}",
#         # category=Category.objects.get(id=random.randint(1,19)),
#         )
#     print(f"{n} Post seed ")

# seed_Post(100)


# def seed_Review(n):
#     fake=Faker()
#     for _ in range(n):
#         Review.objects.create(
#             post=Post.objects.get(id=random.randint(1,99)),            
#             author=User.objects.get(id=1),
#             review=fake.text(max_nb_chars=300),
#         )
#     print(f"{n} Review seed ")
    
# seed_Review(300)



