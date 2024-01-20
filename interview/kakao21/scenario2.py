import request_api as api


# 시나리오 2(problem = 2)
# 서비스 지역의 크기: 60X60
# 자전거 대여 요청 빈도: 분당 요청 수 평균 15건
# 자전거 수: 10,800대. 각 자전거 대여소에는 초기에 자전거가 3대씩 있음
# 트럭 수: 10대

def main():
    start = api.post_start(2)
    location = api.get_location()
    trucks = api.get_trucks()
    print(location)
    print(trucks)

    commands = [{"truck_id": t.get("id"), "command": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]} for t in trucks]

    # first 4 hours
    for _ in range(720):
        simulate = api.put_simulate(commands)
        print(simulate.get("status") + ",", str(simulate.get("time")) + "/720,",
              "failed " + str(simulate.get("failed_requests_count")) + ",", "distance " +
              str(simulate.get("distance")))
        status = simulate.get("status")


    # # first 4 hours
    # for _ in range(240):
    #     simulate = api.put_simulate(commands)
    #     print(simulate.get("status") + ",", str(simulate.get("time")) + "/720,",
    #           "failed " + str(simulate.get("failed_requests_count")) + ",", "distance " +
    #           str(simulate.get("distance")))
    #     status = simulate.get("status")
    #
    #
    # # first 4 hours
    # for _ in range(240):
    #     simulate = api.put_simulate(commands)
    #     print(simulate.get("status") + ",", str(simulate.get("time")) + "/720,",
    #           "failed " + str(simulate.get("failed_requests_count")) + ",", "distance " +
    #           str(simulate.get("distance")))
    #     status = simulate.get("status")

    api.get_score()
