from celery import Celery

app = Celery('tasks', 
            broker='redis://localhost:6379/0',
            backend='redis://localhost:6379/1',
            broker_connection_retry_on_startup=True)


@app.task
def upscale_image():
    # result_filename = upscale('upscale.lama_300px.png', 'upscale.lama_300px.png', 'upscale.EDSR_x2.pb')

    return 'result_filename'
