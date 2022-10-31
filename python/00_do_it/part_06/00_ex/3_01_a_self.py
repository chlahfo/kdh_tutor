def pageNum(total_num, page_num):
    pages = total_num // page_num
    if total_num % page_num != 0:
        pages= pages +1
    return pages
print(pageNum(5, 10))
print(pageNum(15, 10))
print(pageNum(25, 10))
print(pageNum(30, 10))