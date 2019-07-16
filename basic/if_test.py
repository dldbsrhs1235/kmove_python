money=True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

score= int(input("점수를 입력하시오."))

if score>=90:
    print("A 입니다.")
elif score>=70:
    print("B 입니다.")
else:
    print("C 입니다.")

jumsu=int(input("점수를 입력하시오."))

total="f"
if jumsu>=90:
    total="a"
elif jumsu>=80:
    total="b"
elif jumsu>=70:
    total="c"
print("당신의 점수는 {} 입니다.".format(total))    
