
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


Open another terminal and hit all these curl requests once the application is up in below manner:

Only the /process_video api must be hit through postman or any other api integration tool (it returns file which may cause problems in response when hitting through terminal)


HELLO FLASK API:
curl http://127.0.0.1:5000/

GET MOVIES LIST:
curl http://127.0.0.1:5000/movies


POST MOVIES LIST:
curl -X POST -H "Content-Type: application/json" -d '{"title": "Tiger3", "genre": "Action", "lead_actor": "Salman Khan"}' http://127.0.0.1:5000/movies

UPDATE MOVIES LIST:
curl -X PUT -H "Content-Type: application/json" -d '{"genre": "Action", "lead_actor": "SRK"}' "http://127.0.0.1:5000/movies?title=Tiger3"

LOGIN: (don't change the username and password have hardcoded it as your_username, your_password in code)


We have to extract the access token from the output of /login api should replace the YOUR_ACCESS in the /protected api

curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://127.0.0.1:5000/login  

curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://127.0.0.1:5000/protected


PROCESS VIDEO:
curl -v -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/10683796/Desktop/EVERYTHING/project/coding_assignment/test.mp4" http://localhost:5000/process_video

