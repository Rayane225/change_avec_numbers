# بسم الله الرحمن الرحيم
# projet de 
# => décimile 
# => bainire
# => octal
# => héxadécinal

# la list des nomber 




def system_héxadécimal_d_h(num):
    """
    number ==> hexadécimal
    """
    ri = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 :'D',
        14 :'E',
        15 :'F',
    }

    return ri[num]


def system_héxadécimal_h_d(num):
    """
    hexadécimal ==> number
    """
    ri = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    return ri[num]

def number_décimale(num_octal, forme):
    """
    number ==> décimile
    """
    # la list des nomber 
    number_héxadicimale = ["A","B","C","D","E","F"]


    number = []
    for i in str(num_octal) : 
        number.append(i)

    # fait la stuce 
    number = number[::-1]

    décimil_number = []
    for i in range(len(number)) :

        number_int = number[i]

        # quand il donner un nomber héxadiscimal 
        if forme == 16 and number_int in number_héxadicimale :
            number_int = system_héxadécimal_h_d(number_int)
        else:
            number_int = int(number[i])

        un_number = number_int * forme**i


        décimil_number.append(un_number)
        
    return sum(décimil_number)





# --------------------------------------------------------------------------------------------------------------



def décimale_number(num_decimile, forme_changement):
    """
    décimale ==> number 
    """

    les_num = []

    while True:
        some_qui_re = num_decimile // forme_changement
        le_number = num_decimile % forme_changement

        les_num.append(le_number)

        num_decimile = some_qui_re

        if some_qui_re == 0:
            break
    les_num = les_num[::-1]

    resultat = ''.join(map(str, les_num))

    return resultat


# ----------------------------------------------------------------------------------

