# #  фейковые данные нужны на
# #  Soft 10
# #  OrderTopic 10
# #  Customer 20
# #  News 20
# from faker import Faker
# from random import randint, choice
#
# from .models import Soft
#
#
# fake = Faker(['ru_RU'])
#
#
# def create_data_soft():
#     for _ in range(2):
#         # print(fake.word())
#         title = fake.word()
#         Soft.objects.crete(
#             title=f'ПК "{title.capitalize()}"',
#             description=fake.text(max_nb_chars=300)
#         )
#         # text = fake.text(max_nb_chars=300)
#         # print(text)
#
#
# # create_data_soft()
#
# def create_data_topic():
#     for _ in range(10):
#         print(fake.word())
#
# # create_data_topic()
# def create_data_customer():
#     for _ in range(10):
#         print(randint(1000000000, 9999999999))
#         print(fake.words())
#         print(fake.company())
#
# # create_data_customer()
# def create_data_news():
#     for _ in range(10):
#         # print(choice(['news', 'update']))
#         # print(fake.date_time())
#         print(fake.name())
#         # print(fake.text(max_nb_chars=50))
#         # print(fake.text(max_nb_chars=300))
#         # print(fake.text(max_nb_chars=1000))
#
#
# # create_data_news()
# '''
# faker.providers
# faker.providers.address
# faker.providers.automotive
# faker.providers.bank
# faker.providers.barcode
# faker.providers.color
# faker.providers.company
# faker.providers.credit_card
# faker.providers.currency
# faker.providers.date_time
# faker.providers.emoji
# faker.providers.file
# faker.providers.geo
# faker.providers.internet
# faker.providers.isbn
# faker.providers.job
# faker.providers.lorem
# faker.providers.misc
# faker.providers.passport
# faker.providers.person
# faker.providers.phone_number
# faker.providers.profile
# faker.providers.python
# faker.providers.sbn
# faker.providers.ssn
# faker.providers.user_agent
# '''