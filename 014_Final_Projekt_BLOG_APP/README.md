# Session-13

 ## Topic:  Auth - 2

  - Learning Outcomes:

        - Setup custom user authentications
        - Use user permissions 
        - Implement login, logout, and registration


  - Topics to be Covered:

        - Extending builtin User Model to add additional fields such as portfolio url, image, etc.
            - Creating a new model for Profile and setting OneToOneField with User Model
            - Creating a form for this model
            - Checking authentication with template by using {% if request.user.is_authenticated %}
            - Code Views
                - Using both forms
                - Making one to one mapping both models with commit=False 
                - Using authenticate, login, logout (from django.contrib.auth import authenticate, login, logout)
                - Using @login_required decorator
        - Changing default authentication from username to email address with BaseUserManager, AbstractBaseUser, PermissionsMixin
        - Adding settings for AUTH_USER_MODEL
            - Creating a brand new CustomUser Model and CustomUserManager Model
            - Creating UserCreationForm, and UserChangeForm for this new user model
            - Creating a custom UserAdmin class for admin page operations in admin.py
        - Additional Features
            - Pillow package for image uploading
                - Installing
                - MEDIA_ROOT, MEDIA_URL settings
                - ImageField(upload_to='profile_pics', blank=True)
                - <form action="" method="post" enctype="multipart/form-data">
            - Crispy Forms
            - Displaying User Messages
            - Deleting User Messages after 5 sec with js
            - Using Bootstrap, including Navbar


    
      
    
  







