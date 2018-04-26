import requests
import pprint
request = requests.get('https://aetna-uat.assurecare.com/mc/auth/token?', auth =('default', 'P@ssw0rd!'))
pp = pprint.PrettyPrinter(indent=8)

def test_MedCompass360(memberID):
    """This function tests the Medcompass ASD API which returns
    the medcompass member360 URL"""
    session = requests.Session()
    req = session.get('https://aetna-uat.assurecare.com/mcapi/auth/token?password=P%40ssw0rd&username=default&password=P%40ssw0rd&securityUserContextId=94aa741d-eedc-4e35-9a34-2823a970f4ea')
    jar = req.cookies.get_dict()

    member = requests.get('https://aetna-uat.assurecare.com/mcapi/Member360/'+ memberID, cookies = jar)
    print(member.content.decode('utf-8'))

def test_MedCompassRows(memberID):
    """The function tests the Medcompass ASD API which specifies the rows needed for a given
    MemberID"""
    session = requests.Session()
    req = session.get('https://aetna-uat.assurecare.com/mcapi/auth/token?password=P%40ssw0rd&username=default&password=P%40ssw0rd&securityUserContextId=94aa741d-eedc-4e35-9a34-2823a970f4ea')
    jar = req.cookies.get_dict()

    member = requests.get('https://aetna-uat.assurecare.com/mcapi/MemberEvents/MEBC6T9Z/10',cookies = jar)
    print(member.json())


def run_tests():
    test_MedCompass360(memberID = 'MEBC6T9Z')
    test_MedCompassRows(memberID = 'MEBC6T9Z')

if __name__ == '__main__':
    run_tests()
