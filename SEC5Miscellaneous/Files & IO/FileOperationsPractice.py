# def get_logs_of_date(file_path, date):
#     logs = ''
    
#     try:
#         f = open(file_path, 'r')
#         for l in f.readlines():
#             if date in l:
#                 logs += l
#         f.close()
#     except FileNotFoundError as e:
#         return str(e)
#     if len(logs) > 0:
#         return logs
#     else:
#         return "No logs for: " + date


# # Example usage
# print(get_logs_of_date("log.txt", "2023-12-09"))





def csv_reader(filepath):
    fname_and_age = []
    try:
        f = open(filepath, 'r')
        ln = f.readline()
        while len(ln) > 0:
            lnlist = ln.strip().split(',')
            tpl = (lnlist[0], lnlist[-1])
            fname_and_age.append(tpl)
            ln = f.readline()
    except FileNotFoundError as e:
        return str(e)
    except ValueError as e:
        return str(e)
    f.close()
    return fname_and_age

print(csv_reader('SEC5Miscellaneous/Files & IO/namesheet.csv'))