# from celery import Celery
# from upscale.upscale1 import upscale
# from app import app


# celery = Celery('tasks', 
#             broker='redis://localhost:6379/0',
#             backend='redis://localhost:6379/1',
#             broker_connection_retry_on_startup=True)


# class ContextTask(celery.Task):
#     def __call__(self, *args, **kwargs):
#         with app.app_context():
#             return self.run(*args, **kwargs)

# celery.Task = ContextTask

# @celery.task
# def upscale_image():
#     result_filename = upscale('upscale/lama_300px.png', 'upscale/lama_600px.png', 'upscale/EDSR_x2.pb')

#     return result_filename
