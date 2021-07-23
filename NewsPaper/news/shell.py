'''                        #terminal
manage.py makemigrations
manage.py migrate
manage.py shell

from news.models import *

user1 = User.objects.create_user(username='Light')
user2 = User.objects.create_user(username='Dark')

Author.objects.create(authorUser=user1) #4
Author.objects.create(authorUser=user2) #5

Category.objects.create(name='Space')  #5
Category.objects.create(name='Science')  #6
Category.objects.create(name='WorldNews')  #7
Category.objects.create(name='IT')  #8

author = Author.objects.get(id=4)  #4
author2 = Author.objects.get(id=5)  #5

Post.objects.create(author=author, categoryType='NW', title='Earth', text='Planet Earth')  #4
Post.objects.create(author=author, categoryType='AR', title='Moon', text='Moon is Moon')  #5
Post.objects.create(author=author2, categoryType='AR', title='Mars', text='Mars is alive')  #6

Post.objects.get(id=4).postCategory.add(Category.objects.get(id=5))
Post.objects.get(id=4).postCategory.add(Category.objects.get(id=6))
Post.objects.get(id=5).postCategory.add(Category.objects.get(id=5))
Post.objects.get(id=5).postCategory.add(Category.objects.get(id=6))
Post.objects.get(id=6).postCategory.add(Category.objects.get(id=5))
Post.objects.get(id=6).postCategory.add(Category.objects.get(id=7))

Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=4).authorUser, text='Nice')  #5
Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=5).authorUser, text='thumb up!')  #6
Comment.objects.create(commentPost=Post.objects.get(id=5), commentUser=Author.objects.get(id=4).authorUser, text='Good!')  #7
Comment.objects.create(commentPost=Post.objects.get(id=6), commentUser=Author.objects.get(id=4).authorUser, text='Good news')  #8

Comment.objects.get(id=5).like()
Comment.objects.get(id=6).like()
Comment.objects.get(id=7).dislike()
Comment.objects.get(id=8).like()
Comment.objects.get(id=8).like()
Post.objects.get(id=4).like()
Post.objects.get(id=5).dislike()
Post.objects.get(id=6).like()

Comment.objects.get(id=7).rating  #-1
Post.objects.get(id=6).rating  #1

a = Author.objects.get(id=4)
a.update_rating()
a.ratingAuthor #2

b = Author.objects.get(id=5)
b.update_rating()
b.ratingAuthor #4

best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
best
Post.objects.all().order_by('-rating').values()[0]
Author.objects.get(id=4).authorUser
Comment.objects.filter(commentPost = Post.objects.get(id = 4)).values('dateCreation', 'commentUser', 'rating', 'text')
'''