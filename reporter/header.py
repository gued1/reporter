import warnings
import datetime

def header(authors, place='Paris'):
    """Create the header text on the authors list
    Parameters
    ----------
    authors : A list of dictionnaries and each dictionnary have "firstname" & "lastname" keys
    place : To add dynamic city
    
    Returns
    -------
    liste : str which is the header text
    
    Note 
    ----
    
    Date is updated at the function execution time
    
    """
    ##Definition of date
    today = datetime.date.today()
    date = today.strftime("%d/%m/%y")
    liste = []
    liste.append(f"{place}, le {date}\n {len(authors)} auteurs:\n")
    ##Get the author names
    for element in authors:
        try:
            nom = element["firstname"]
        except KeyError:
            nom = 'XXX'
            warnings.warn('Firstname is missing')
        
        prenom = element.get('lastname', 'XXX')
    ##print("\n".join(liste))
    return("\n".join(liste))