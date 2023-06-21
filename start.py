def payset(usn,dd,mm,yy):
    payload = {'username': usn ,'dd': str(dd), 'mm': str(mm),
    'yyyy': str(yy),
    'passwd': f'{str(yy)}-{str(mm)}-{str(dd)}',
    'remember': 'No',
    'option': 'com_user',
    'task': 'login',
    'return':{ 
    '9e86fa64b9132a81db6c9db4b1b1340b': '1'}
    }
    return payload