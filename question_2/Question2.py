
import json

booking = []


                
def set_value(s, n):
    if s>=0 and s<24 :
        booking.append({"slot":s, "name":n})
        # if (i["slot"]==s for i in booking):
        #     names=[booking[s]["name"],n]
        #     booking.append({"slot":s, "name":names})
            
                
    return booking

def cancel(s, n):
    for i in booking:
        if i["slot"]==s and i["name"]==n:
            booking.remove(i)
            return True
        else:
            return False
n=1
while(n!=0):
    choice=str(input("POST /booking - B\nPOST /cancel - C\nGET /booking - G\nChoice - "))
    if choice.lower() =='b':
        slot=int(input())
        name=str(input())
        set_value(slot, name)
        display={"status":"confirmed booking for "+name+" in slot "+str(slot)}
        d = json.dumps(display)
        print(d)

    if choice.lower()=='g':
        for i in booking:
            print(json.dumps(i, indent=2))

    if choice.lower()=='c':
        for i in booking:
            slot=int(input())
            name=str(input())
            flag = cancel(slot, name)
            if flag == True:
                display={"status": "canceled booking for "+name+" in slot "+str(slot)}
                print(json.dumps(display))
            else:
                display={"status": "no booking for the name "+name+" in slot "+str(slot)}
                print(json.dumps(display))




