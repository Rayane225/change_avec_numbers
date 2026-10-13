# بسم الله الرحمن الرحيم
# projet de 
# => décimile 
# => bainire
# => octal
# => héxadécinal



def number_décimale(num_octal, forme):
    """
    number ==> décimile
    """

    number = []
    for i in str(num_octal) : 
        number.append(i)

    # fait la stuce 
    number = number[::-1]

    décimil_number = []
    for i in range(len(number)) :
        un_number = int(number[i]) * forme**i

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

def system_héxadécimal(num):
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

