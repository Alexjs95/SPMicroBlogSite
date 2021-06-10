Creation of a simple static blog site using Django. The site will later be used to apply Snowplow tracking libraries.

Useage:
in SPMicroBlog execute  'python manage.py makemigrations'
			'python manage.py makemigrations'
			'python manage.py runserver'

Navigate to localhost:8000/admin
Login with superuser, create with command 'python manage.py createsuperuser'
Should see two models under BLOG - Categorys and posts
Create a couple of categories then create some fake posts and assign category.

Navigate to localhost:8000/blog
Posts should be displayed if created.

Snowplow tracking implemented in \SPMicroBlogSite\blog\views.py