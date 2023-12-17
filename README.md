
Clone the repository (it is public no token required)

1- Clone the git repository

git clone https://github.com/SunnyChugh99/coding_assignment.git


2- Activate the virtualenv (which is already created and present in repo)
cd coding_assignment/
source env/bin/activate

3 - Run the python application
cd coding_solution
python app.py 

4 - Once the server is up, we can play around with all api's

Open another terminal and hit all these curl requests(except /process_video) once the application is up in below manner:
The /process_video API should only be accessed using Postman or another API integration tool since it returns a file, which may lead to response issues when accessed via the terminal.

A- HELLO FLASK API:
api-endpoint - curl http://127.0.0.1:5000/

B - GET MOVIES LIST:
api-endpoint - curl http://127.0.0.1:5000/movies


POST MOVIES LIST:
api-endpoint - curl -X POST -H "Content-Type: application/json" -d '{"title": "Tiger3", "genre": "Action", "lead_actor": "Salman Khan"}' http://127.0.0.1:5000/movies

UPDATE MOVIES LIST: (it updates based on title name of movie)
api-endpoint - curl -X PUT -H "Content-Type: application/json" -d '{"genre": "Action", "lead_actor": "SRK"}' "http://127.0.0.1:5000/movies?title=Tiger3"

LOGIN: (don't change the username and password have hardcoded it as your_username, your_password in code)

We have to extract the access token from the output of /login api should replace the YOUR_ACCESS in the /protected api

api-endpoint - curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://127.0.0.1:5000/login  

api-endpoint - curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://127.0.0.1:5000/protected


PROCESS VIDEO:(The /process_video API should only be accessed using Postman or another API integration tool since it returns a file, which may lead to response issues when accessed via the terminal.
)

api-endpoint - curl -v -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/10683796/Desktop/EVERYTHING/project/coding_assignment/test.mp4" http://localhost:5000/process_video

