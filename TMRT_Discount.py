"""
2020/01/24
Author: Bassalt
"""

def Discount(num):
    dis=0;
    if(num<=10):
        dis=0;
    elif(num>=11 & num<=50):
        dis=int((num-1)/10)*5+5
    else:
        dis=30
    print("回饋：{}%".format(dis));
    return dis;

def TotalCost(cost,num):
    totalNum=sum(num);
    totalCost=0;
    for i in range(len(cost)):
        totalCost=totalCost+cost[i]*num[i];
    return totalCost,totalNum;


print("北捷優惠計算");

while(1):
    money=[];
    time=[];
    try:
        while(1):
            money.append(int(input("請輸入金額：")));
            print("你輸入過的金額：{}".format(money));
            time.append(int(input("請輸入次數：")));
            print("你輸入過的次數：{}".format(time));
            print("\n按CTRL+C結束輸入");
    except KeyboardInterrupt:
        totalMoney,totalTime=TotalCost(money,time);
        print("====\n")
        print("總花費：{}，總次數：{}".format(totalMoney,totalTime));
        discount=Discount(totalTime);
        disMoney=int(discount*totalMoney/100);
        print("回饋金：{}".format(disMoney));
    print("\n\n◝(　ﾟ∀ ﾟ )◟◝(　ﾟ∀ ﾟ )◟◝(　ﾟ∀ ﾟ )◟")
    print("====重新計算的分隔線====")

