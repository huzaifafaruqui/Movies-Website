# Movies-Website
Open source website for movie reviews. This website is being built as our DBMS project in fifth semester, Computer Engineering, Jamia Millia Islamia.


### Built With

This website uses a number of open source projects to work properly:

* [Django] - High-level Python Web framework
* [Bootstrap] - great UI boilerplate for modern web apps



And of course this website itself is open source with a [public repository][dill]
 on GitHub.
### Local Development / Testing
1. Open terminal
2. sudo pip install pip --upgrade
3. pip install virtualenv
4. mkdir movieweb
5. cd movieweb
6. virtualenv .
7. source bin/activate
8. pip install django==1.9
11. Clone/Download this repo
12. cd Movies-Website/lmdb
13. sudo rm -rf home/migrations/*
14. sudo rm db.sqlite3
15. python manage.py makemigrations home
16. python manage.py migrate
17. python manage.py createsuperuser (optional)
18. python manage.py runserver
19. Visit 127.0.0.1:8000/ 


  	
### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

1. Fork the repo
2. Create a new branch (`git checkout -b improve-feature`)
3. Make the appropriate changes in the files
4. Add changes to reflect the changes made
5. Commit your changes (`git commit -am 'Improve feature'`)
6. Push to the branch (`git push origin improve-feature`)
7. Create a Pull Request 

### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave irrelevant results), kindly open an issue [here](https://github.com/huzaifafaruqui/Movies-Website/issues/new) by including your search query and the expected result.

If you'd like to request a new functionality, feel free to do so by opening an issue [here](https://github.com/huzaifafaruqui/Movies-Website/issues/new) including some sample queries and their corresponding results.


### Todos

 - Write Tests
 - Add Code Comments
 - Backend

## Contributors
1. [Tafseer Ahmed](https://github.com/tafseerahmed)
2. [Mohd Huzaifa Faruqui](https://github.com/huzaifafaruqui)
3. [Gaurav Arora](https://github.com/gaurav61)

License
----

MIT



   [dill]: <https://github.com/huzaifafaruqui/Movies-Website>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Django]:<https://code.djangoproject.com/>
   [Bootstrap]: <http://getbootstrap.com/getting-started/>
  

