
def calc_uptime(total, down):
    uptime = total - down
    return f"The uptime percentage is: {float(uptime/total * 100):.2f}%"

print(calc_uptime(24, 3))