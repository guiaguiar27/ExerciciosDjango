# ManaPro  
This project aims to provide a platform of users management

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)

> The project has only educational purposes 

### Tasks
The project is still under development
- [x] Setup Django project
- [x] Setup django main aplication
- [x] Setup docker container for running the project
- [x] Setup the templates using the inheritance scheme in Django and bootstrap
- [ ] Setup the pipeline
- [ ] CI/CD
- [ ] 

## 💻 Requirements

All packages and libraries can be accessed in the requirements.txt  


## ☕ Using ManaPro Virtual environment

To use with the virtual environment
```
source venv/bin/activate
``` 

To run the development environment - Make sure that every migration is prepared
``` 
python manage.py runserver
```

## ☕ Using ManaPro Container 
- Make sure to have Docker installed in your machine  
Run the following command: 

```
docker build -t manapro .
``` 
To run the server in development mode: 
``` 
docker run -p 8000:8000 manapro
```

## 🤝 Author
Guilherme 
