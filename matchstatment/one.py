#similar to switch statement in c/c++
def http_error(status):
    match status:
        case 400:
            return "Bad Request"
            

