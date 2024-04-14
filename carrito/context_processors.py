import epaycosdk.epayco as epayco


def cart(request):

    # apiKey = "1cee1cc84a86f853b8c5477af818d513"
    # privateKey = "5ecb99fd93d8448e134eb3ba5546541b"
    # lenguage = "ES"
    # test = True
    # options={"apiKey":apiKey,"privateKey":privateKey,"test":test,"lenguage":lenguage}

    # objepayco=epayco.Epayco(options)

    # credit_info = {
    #     "card[number]": "4093550016110334",
    #     "card[exp_year]": "2027",
    #     "card[exp_month]": "05",
    #     "card[cvc]": "686",
    #     "hasCvv": True,
    # }

    # token = objepayco.token.create(credit_info)
    # customer_info = {
    #     "token_card": token.get("id"),
    #     "name": "Luis Felipe",
    #     "last_name": "Echeverry",
    #     "email": "daluz0221@gmail.com",
    #     "phone": "3004837614",
    #     "default": True,
    # }

    # customer = objepayco.customer.create(customer_info)
    # update_customer_info = {
    #     "name": "Julian David"
    # }
    # customer = objepayco.customer.get("61b4dfaa1b8f1e255039ae2")
    # customer =objepayco.customer.update("61b4dfaa1b8f1e255039ae2",update_customer_info)

    print("=====================================")
    # print(objepayco.customer.getlist())
    # print(customer)
    print("=====================================")
    return {'cart': 'pruebas'}