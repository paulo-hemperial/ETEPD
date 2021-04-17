#É vogal ou não é? Maoe hihi
def v(x):
  vogal = 'aáãàâäåæªéèêēęėëeiîíìīïįoõôòóºōøöœüúûùūu'
  consoante = ('bcdfghjklmnpqrstvwxyz')
  if x in vogal:
    return 'É uma vogal!'
  elif x in consoante:
    return 'É uma consoante!'
  else:
    return 'É um número ou caráctere especial.'
    
###########lixo acima favor ignorar#######
gal = input('Digite uma letra: ')
print(v(gal))
