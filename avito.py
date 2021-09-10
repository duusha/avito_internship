import asyncio
import requests

async def get_matrix(url):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, url)
    res = await future
    # res = requests.get(url)
    if res.status_code in range(400, 600): # обработка ошибки response
        print('Error in response: Code', res.status_code)
        return []
    mas = res.text.split(" ")
    nums = []
    for elem in mas:
        if elem.isnumeric():
            nums.append(int(elem))
    # l = range(50)
    # nums = random.sample(l, 25)
    # nums = [1, 2, 3, 4, 5,
    #         6 , 7 ,8 ,9 ,10,
    #         11, 12, 13, 14, 15,
    #         16, 17, 18, 19 ,20,
    #         21, 22, 23, 24, 25]
    #print(nums)
    if not nums:
        return []
    n = int(len(nums) ** 0.5)
    result = []
    i = 0
    j = 0
    right = n - 1
    left = 0
    up = 0
    down = n - 1
    cou = 0
    go_down = 1
    go_right = 0
    go_up = 0
    go_left = 0
    while len(result) != len(nums) - 1:
        if (go_down and j < down):
            result.append(nums[i + j * n])
            j += 1
        elif (j == down and go_down):
            go_down = 0
            go_right = 1
            left += 1
        elif (go_right and i < right):
            result.append(nums[i + j * n])
            i += 1
        elif(i == right and go_right):
            go_right = 0
            go_up = 1
            down -= 1
        elif (go_up and j > up):
            result.append(nums[i + j * n])
            j -= 1
        elif (go_up and j == up):
            right -= 1
            go_up = 0
            go_left = 1
        elif (go_left and i > left):
            result.append(nums[i + j * n])
            i -= 1
        elif (go_left and i == left):
            go_left = 0
            go_down = 1
            up += 1
        cou += 1
    result.append(nums[i + j * n])
    # print(result)
    return result


        # if (i == left and j < down):
        #     result.append(nums[i + j * n])
        #     j += 1
        # elif (i == left and j == down):
        #     left += 1
        #     result.append(nums[i + j * n])
        #     i += 1
        # elif (i < right and j == down):
        #     result.append(nums[i + j * n])
        #     i += 1
        # elif (i == right and j == down):
        #     down -= 1
        #     result.append(nums[i + j * n])
        #     j -= 1
        # elif (j > up and i == right):
        #     result.append(nums[i + j * n])
        #     j -= 1
        # elif (j == up and i == right):
        #     right -= 1
        #     result.append(nums[i + j * n])
        #     i -= 1
        # elif (i > left and j == up):
        #     result.append(nums[i + j * n])
        #     i -= 1
        # elif (i == left and j == up):
        #     left += 1
        #     result.append(nums[i + j * n])
        #     j += 1
        # cou += 1

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
test_get_matrix()