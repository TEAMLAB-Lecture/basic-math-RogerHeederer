#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):

    return max(number_list)



def get_smallest(number_list):
    return min(number_list)

def get_mean(number_list):
    sum = 0
    for num in number_list:
        sum += num
    
    return (sum/len(number_list))


def get_median(number_list):
    
    number_list.sort()

    if len(number_list) % 2 == 0: # 짝수라면
        half_len = int(len(number_list) / 2)
        sum = number_list[half_len - 1] + number_list[half_len]
        median = sum/2
        return median
    else: #홀수라면
        half_len = int(len(number_list) / 2 - 0.5)
        print(half_len)
        print(number_list)
        print(number_list[half_len])
        median = number_list[half_len]
        return median

