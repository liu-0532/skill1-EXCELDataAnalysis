DEBUG = True
HOST = 'localhost'
PORT = 5000
DATABASE_URL = 'sqlite:///database.db'
CORS_ORIGINS = ['http://localhost:3000']
SKILLS_DIR = '/path/to/skills'
UPLOAD_SETTINGS = {
    'UPLOAD_FOLDER': '/path/to/uploads',
    'MAX_CONTENT_LENGTH': 16 * 1024 * 1024,  # 16 MB
    'ALLOWED_EXTENSIONS': {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
}