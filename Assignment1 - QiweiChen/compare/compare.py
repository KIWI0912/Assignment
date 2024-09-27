import difflib

def calculate_similarity(text1, text2):
    # Create a SequenceMatcher object
    matcher = difflib.SequenceMatcher(None, text1, text2)
    
    # Computational similarity
    similarity_ratio = matcher.ratio()
    
    # Convert to percentage format
    similarity_percentage = similarity_ratio * 100
    return similarity_percentage

def remove_spaces(string):
    return string.replace(" ", "")

# orignial text and test text
text1 = '''
bhttps//mrsinvoice.com
Lp
I |
Your Company LLC Address 123, State, My Country P 111-222-333, F 111-222-334
BILL TO:
P: 111-222-333, F: 111-222-334 m .
dlent@ccomplent
Contact Phone 101-102-103
john Doe office ayment Terms ash on Delivery
Office Road 38
P: 111-833-222, F: 122-222-334 Amount Due: $4,170
office@example.net
NO PRODUCTS / SERVICE QUANTITY / RATE / UNIT AMOUNT
HOURS, PRICE
1 | tyre 2 $20 $40
2 | Steering Wheet 5 $10 $50
3 | Engine ol 40 $15 $150
4 | Brake Pad 2a $1000 $2,400
Subtotal $275
Tax (10%) $275
Grand Total $302.5
‘THANK YOU FOR YOUR BUSINESS'''

text2 = '''
http://mrsinvoice.com
Invoice
Your Company LLC Address 123, State, My Country P 111-222-333,F111-222-334
BILL TO:
John Doe	Invoice #	00001	
Alpha Bravo Road 33	Invoice Date	12/12/2001	
client@example.net	P:111-222-333,F:111-222-334	Name of Rep.	Bob	
Contact Phone	101-102-103	
SHIPPING TO:
John Doe Office	Payment Terms	Cash on Delivery	
Office Road 38
P:111-333-222.F:122-222-334	Amount Due: $4,170	
office@example.net
NO	PRODUCTS / SERVICE	QUANTITY /	RATE/UNIT	AMOUNT	
HOURS	PRICE	
1   Tyre	2	$20	$40	
2	Steering Wheel	5	$10	$50	
3	Engine Oil	10	$15	$150	
4	Brake Pad	24	$1000	$2,400	
Subtotal	$275	
Tax(10%)	$27.5	
Grand Total	$302.5	
THANK YOU FOR YOUR BUSINESS'''

text1 = remove_spaces(text1)
# print(text1)
text2 = remove_spaces(text2)

# calculate the similarity
similarity = calculate_similarity(text1, text2)
print(f"similarity: {similarity:.2f}%")


