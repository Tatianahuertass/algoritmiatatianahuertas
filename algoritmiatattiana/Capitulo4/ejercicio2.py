can_fly=bool(int(input("¿digite si puede volar? 1:si 0=no: ")))
is_human=bool(int(input("digite si es humano: ")))
has_mask=bool(int(input("digite si tiene mascara: ")))
if ((can_fly=="true") and (is_human=="true")) and (has_mask=="true"):
    print("ironman")
elif ((can_fly=="true") and (is_human=="true") and (has_mask=="no")):
    print("capitan marvel")        
elif ((can_fly=="true") and (is_human=="false") and (has_mask=="true")):
    print("ronan accuser")
elif ((can_fly=="true") and (is_human=="false") and (has_mask=="no")):
    print("Vision")
elif ((can_fly=="no") and (is_human=="true") and (has_mask=="true")):
    print("Spiderman")
elif ((can_fly=="no") and (is_human=="true") and (has_mask=="no")):
    print("hulk")
elif ((can_fly=="no") and (is_human=="true") and (has_mask=="true")):
    print("black bolt")
elif ((can_fly=="no") and (is_human=="true") and (has_mask=="no")):
    print("thanos")
    
