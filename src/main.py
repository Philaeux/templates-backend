import logging

import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s")

# Entrypoint
if __name__ == '__main__':
    from template.backend import app
    uvicorn.run(app, host="0.0.0.0", port=5000)
