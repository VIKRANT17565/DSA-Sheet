def printLargest(arr):
    n = len(arr)
    arr.sort()
    # arr.reverse()
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] < arr[j] + arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return ''.join(arr)

print(printLargest(['664', '948', '25', '544', '855', '9', '982', '553', '289', '164', '360', '20', '380', '357', '462', '488', '354', '900', '789', '245', '881', '467', '284', '275', '237', '910', '568', '835', '940', '685', '652', '550', '267', '468', '111', '590', '328', '774', '582', '296', '937', '875', '436', '232', '973', '29', '799', '71', '588', '298', '90', '647', '91', '112', '613', '464', '113', '782', '952', '231', '322', '214', '129', '951', '601', '960', '755', '993', '195', '331', '633']))

print(printLargest(['0', '0', '0', '0', '0']))

# print(printLargest(['3', '30', '34', '5', '9']))
# print(printLargest(['54', '546', '548', '60']))
# print(printLargest(['1', '34', '3', '98', '9', '76', '45', '4']))