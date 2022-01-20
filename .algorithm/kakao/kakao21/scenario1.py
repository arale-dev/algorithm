import request_api as api
import collections


# 시나리오 1(problem = 1)
# 서비스 지역의 크기: 5X5
# 자전거 대여 요청 빈도: 분당 요청 수 평균 2건
# 자전거 수: 100대. 각 자전거 대여소에는 초기에 자전거가 4대씩 있음
# 트럭 수: 5대


def main():
    start = api.post_start(1)
    location = api.get_location()
    trucks = api.get_trucks()
    print(location)
    print(trucks)
    for truck in trucks:
        truck["distances"] = get_distance_truck2locations(truck["location_id"])
        truck["remain_commands"] = collections.deque()
        truck["destination"] = 0
    print(trucks)


    commands = [{"truck_id": t.get("id"), "command": []} for t in trucks]
    commands = []

    for _ in range(720):
        simulate = api.put_simulate(commands)
        print(simulate.get("status") + ",", str(simulate.get("time")) + "/720,",
              "failed " + str(simulate.get("failed_requests_count")) + ",", "distance " +
              str(simulate.get("distance")))

    api.get_score()


def get_distance(i, j):
    row, col = divmod(abs(i - j), 5)
    return row + col


def get_distance_truck2locations(i):
    return [get_distance(i, j) for j in range(25)]


def get_nearest_truck():
    pass
