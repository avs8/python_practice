import re
# Building url shortner
# i am building health site
# url is "myhealth.com"
# if "myhealth.com/?id=4" the url will be myhealth.com/hbp
# in database id is mapped to hbp


def url_shortner(url):
    """
    use rejex to find out everything after
    .com and replace value of id matched
    """
    match = re.search(r'\?(id=.+)', url).group()
    value = find_id(match[-1])
    return url.replace(match, value)


def find_id(id):
    """
    This function should match id in database
    """
    url_id = {4: 'hbp'}
    for key, value in url_id.items():
        if key == id:
            value = value
        return value


print url_shortner('www.myhealth.com/?id=4')
