def nearest_power_of_two(num):
    i = 2;
    nearestInteger = 0;
    while i <= num:
        nearestInteger = i;
        i *= 2;

    return nearestInteger;

print(nearest_power_of_two(10)) # output is 8
print(nearest_power_of_two(100))# output is 64
print(nearest_power_of_two(2))  # output is 2