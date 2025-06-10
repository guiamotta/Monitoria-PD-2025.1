total = int(input())
cem = total//100
cinq = (total%100)//50
vinte = ((total%100)%50)//20
dez = (((total%100)%50)%20)//10
cinco = ((((total%100)%50)%20)%10)//5
dois = (((((total%100)%50)%20)%10)%5)//2
um = (((((total%100)%50)%20)%10)%5)%2
print(total)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinq} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")