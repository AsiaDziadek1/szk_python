# / oddziela argumenty, które musza byc podane po pozycji od argumentów, które mogą byc podane po nazwie
def allparams(a,b,/, c=42,*args, d=256,**kwargs):
    print("a,b",a,b)
    print("c,d",c,d)
    print("args",args)
    print("kwargs",kwargs)

allparams(1,2)
allparams(1,2,3)
allparams(1,2,3,4)  #args (4,)
allparams(1,2,3,4,5)  #args (4, 5)
allparams(1,2,3,4,5,6,d=100) #c,d 3 100
allparams(1,2,3,4,5,6,d=100, e=5456, name='radek')  #kwargs {'e': 5456, 'name': 'radek'}
# allparams(a=1, b=2)  #TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - powoduje że a i b muszą byc przekazane jako pozycyjne
allparams(1,2)
allparams(1,2, c=9)  # c jest za / więc może byc w odróznieniu od a i b po nazwie
allparams(1,2,a=5,b=9)  #kwargs {'a': 5, 'b': 9}



