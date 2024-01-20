import requests

temp_problem = 1
path = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
headers = {"X-Auth-Token": "26fe0c04cec8daaf9cf7e9db73007c96"}


def post_start(problem):
    data = {"problem": problem}
    response = requests.post(path + '/start', json=data, headers=headers)
    headers["Authorization"] = response.json().get("auth_key")
    global temp_problem
    temp_problem = problem
    return response.json()


def get_score():
    response = requests.get(path + '/score', headers=headers)
    print(">>>>>", "Problem", temp_problem, ">>>>> ", response.json(), "\n\n")
    return response.json()


def get_location():
    response = requests.get(path + '/locations', headers=headers)
    return response.json().get("locations")


def get_trucks():
    response = requests.get(path + '/trucks', headers=headers)
    return response.json().get("trucks")


def put_simulate(commands):
    data = {"commands": commands}
    response = requests.put(path + '/simulate', json=data, headers=headers)
    return response.json()
