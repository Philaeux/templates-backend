import uvicorn

if __name__ == '__main__':
    from projectname.projectname import app
    uvicorn.run(app, host="0.0.0.0", port=5000)
