import requests

temp_problem = {"score" : 1}
path = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
headers = {"X-Auth-Token": "f1bfa75e8d144e323363a83ac16da527"}


def post_start(problem):
    data = {"problem": problem}
    response = requests.post(path + '/start', json=data, headers=headers)
    headers["Authorization"] = response.json().get("auth_key")
    global temp_problem
    temp_problem["score"] = problem
    print("시나리오", response.json().get("problem"), "시작")
    print("Authorization : ", response.json().get("auth_key"))
    return response.json()


def get_score():
    response = requests.get(path + '/score', headers=headers)
    print(">>>>>", "Problem", temp_problem["score"], "score \n>>>>> ", response.json(), "\n\n")
    return response.json()


def get_waiting_line():
    response = requests.get(path + '/waiting_line', headers=headers)
    # "waiting_line": [
    #     {"id": 1, "from": 3}, 매칭 기다리는 유저 아이디, 매칭 대기를 시작한 시간
    #     {"id": 2, "from": 14},
    #     ...
    # ]
    return response.json().get("waiting_line")


def get_game_result():
    response = requests.get(path + '/game_result', headers=headers)
    # "game_result": [
    #     {"win": 10, "lose": 2, "taken": 7},
    #     {"win": 7, "lose": 12, "taken": 33},
    #     ...
    # ]
    return response.json().get("game_result")

def get_user_info():
    response = requests.get(path + '/user_info', headers=headers)
    # "user_info": [
    #     {"id": 1, "grade": 2100}, 현재 등급
    #     {"id": 13, "grade": 1501},
    #     ...
    # ]
    return response.json().get("user_info")


def put_match(pairs):
    data = {"pairs": pairs}
    response = requests.put(path + '/match', json=data, headers=headers)
    return response.json()


def put_change_grade(commands):
    # "commands": [
    #     {"id": 1, "grade": 1900}
    #         ...
    # ]
    data = {"commands": commands}
    response = requests.put(path + '/change_grade', json=data, headers=headers)
    return response.json()


