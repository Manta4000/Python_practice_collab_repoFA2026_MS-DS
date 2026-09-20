"Williams_Timothy_TPW_1.7.19"
###Heat Capacity problem
##Solved! In roughly 2 fewer lines of code than the solutions. 
# Included a way to tell the difference between a small, medium, and large cups of tea!
spec_heat_water = 4.186
m = int(input("What is the mass of water (in grams)?: "))
m_vol_ounces = 0.033814*m
av_water_temp = 10 #Average temperature of tap water in temperate climate zones
tea_cup = (8, 10, 12) ##Typical range of sizes of a cup of tea in ounces
del_T = int(input("What is the desired temp. for this amount of water (in deg. Celcius)?: ")) - av_water_temp

q = m*spec_heat_water*del_T # Energy calculation

electricity_conv = q*2.7778e-7
cost_ = electricity_conv*8.9
if m_vol_ounces/tea_cup[0] <= 1:
    print("This amount of water makes a small cup of tea, at a cost of roughly ", round(cost_, 2), " cents.")
    print("This amount of water makes roughly, ", round(m_vol_ounces/tea_cup[0], 2), " small cups of tea.")

elif m_vol_ounces/tea_cup[2] >= 1:
    print("This amount of water makes a large cup of tea, at a cost of roughly ", round(cost_, 2), " cents.")
    print("This amount of water makes roughly, ", round(m_vol_ounces/tea_cup[2], 2), " large cups of tea.")

else:
    print("This amount of water makes a mid-sized cup of tea, at a cost of roughly ", round(cost_, 2), " cents.")
    print("This amount of water makes roughly, ", round(m_vol_ounces/tea_cup[1], 2), " mid-sized cups of tea.")