def solution(phone_book):
    for i in phone_book:
        temp = phone_book.copy()
        temp.remove(i)
        for oneNumber in temp:
            if i in oneNumber[:len(i)]:
                return False
    return True