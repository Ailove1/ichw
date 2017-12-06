def get_from(cufrom, cuto, amt):
    '''to fetch the imformation needed in exchanging'''
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(cufrom, cuto, amt))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return(jstr)
def num_extract(instr):
    '''to extract the needed numbers in the string'''
    numb = ''
    for i in range(instr.find('''"to"''') + 8, len(instr)):
        if ord(instr[i])>45 and ord(instr[i])<58:
            numb = numb + instr[i]
    return(numb)
def exchange(currency_from, currency_to, amt_from):
    '''exchange the currency'''
    amt_to = num_extract(get_from(currency_from, currency_to, amt_from))
    return(amt_to)

def test_get_from():
    assert("""{ "from" : "1 United States Dollar", "to" : "0.838095 Euros", "success" : true, "error" : "" }""" == get_from("USD", "EUR","1"))
def test_num_extract():
    assert(num_extract('''"to" : "21.124.124.25uccess"''') == '''21.124.124.25''')
def test_exchange():
    assert(exchange('USD', 'EUR', '1') == '0.838095')
def test_all():
    '''test all functions'''
    test_get_from()
    test_num_extract()
    test_exchange()
    print('all tests passed')
    
source = input("currency to be exchanged: ")
target = input("currency to exchange to: ")
amt = input("amount of currency to be exchanged: ")
print ("The amount exchanged to is {}".format(exchange(source, target, amt)))
test_all()
