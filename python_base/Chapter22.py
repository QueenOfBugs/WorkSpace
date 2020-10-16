# Fizz-3 Buzz-5 FizzBuzz-3,5

def fizz_buzz():
    fiz = "Fizz"
    buz = "Buzz"
    fiz_buz = "FizzBuzz"
    # for i in range(1, 101):
    #     if i % 3 == 0:
    #         if i % 5 == 0:
    #             print(fiz_buz)
    #             continue
    #         print(fiz)
    #     elif i % 5 == 0:
    #         if i % 3 == 0:
    #             print(fiz_buz)
    #             continue
    #         print(buz)
    #     else:
    #         print(i)
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(fiz_buz)
        elif i % 3 == 0:
            print(fiz)
        elif i % 5 == 0:
            print(buz)
        else:
            print(i)


# sequential search

def ss(num_list, n):
    found = False
    for i in num_list:
        if i == n:
            found = True
            break
    return found


# palindrome 回文词 单词正反顺序一致

def palindrome(word):
    word = word.lower()
    return word[::-1] == word


# anagram 变位词 单词组成一样的两个词

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


# 计算字母频数
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    return count_dict


# 递归 打印《99瓶啤酒》

def bottles_of_beer(bob):
    """
    Prints 99 Bottle
    of Beer on the Wall lyrics.
    :param bob: Must be a positive integer
    :return:
    """
    if bob < 1:
        print("""No more
        bottles
        of beer
        on the wall.
        No more
        bottles of
        beer.
        """)
        return
    tmp = bob
    bob -= 1
    print("""
{} bottles of beer on the wall. {} boottles of beer. take one down,\
pass it around, {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)


def ts():
    print("123")
    return


if __name__ == "__main__":
    fizz_buzz()

    numbers = [i for i in range(0, 101)]
    print(ss(numbers, 101))
    print(numbers)

    print(palindrome("Mom"))
    print(anagram("iceman", "cinema"))
    print(count_characters("asdasdasdasdasdasd"))
    print(ts())
    bottles_of_beer(99)
