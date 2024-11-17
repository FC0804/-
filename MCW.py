
def nagative_calculate(vx, vy, vw, r, La, Lb):
    # 计算轮子的角速度
    common_factor = (La + Lb) * vw
    w1 = (-vx + vy + common_factor) / r
    w2 = (vx + vy - common_factor) / r
    w3 = (-vx + vy - common_factor) / r
    w4 = (vx + vy + common_factor) / r
    return w1, w2, w3, w4

def positive_calculate(w1, w2, w3, w4, r, La, Lb):
    # 计算底盘速度
    vx = r * (-w1 + w2 - w3 + w4) / 4
    vy = r * (w1 + w2 + w3 + w4) / 4
    vw = r * (w1 - w2 - w3 + w4) / (4 * (La + Lb))
    return vx, vy, vw

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("输入无效，请输入一个数字。")

def main():
    while True:
        print("选择运算类型:")
        print("1. 正向运动学计算")
        print("2. 逆向运动学计算")
        print("3. 退出")
        choice = input("请输入选择 (1、2 或 3): ")

        if choice == '3':
            print("退出程序。")
            break
        
        La = get_float_input("请输入底盘的宽度 (m): ") / 2
        Lb = get_float_input("请输入底盘的长度 (m): ") / 2
        r = get_float_input("请输入轮子的半径 (m): ")
        
        if choice == '1':
            # 正向运动学计算
            vx = get_float_input("请输入底盘的x方向速度 (m/s): ")
            vy = get_float_input("请输入底盘的y方向速度 (m/s): ")
            vw = get_float_input("请输入底盘的角速度 (rad/s): ")
            
            # 计算轮子速度
            w1, w2, w3, w4 = nagative_calculate(vx, vy, vw, r, La, Lb)
            print(f"轮子角速度: w1 = {w1} rad/s, w2 = {w2} rad/s, w3 = {w3} rad/s, w4 = {w4} rad/s")  # 添加单位
        
        elif choice == '2':
            # 逆向运动学计算
            w1 = get_float_input("请输入轮子1的角速度 (w1): ")
            w2 = get_float_input("请输入轮子2的角速度 (w2): ")
            w3 = get_float_input("请输入轮子3的角速度 (w3): ")
            w4 = get_float_input("请输入轮子4的角速度 (w4): ")
            
            # 计算底盘速度
            vx, vy, vw = positive_calculate(w1, w2, w3, w4, r, La, Lb)
            print(f"底盘速度: vx = {vx} m/s, vy = {vy} m/s, vw = {vw} rad/s")  # 添加单位
        else:
            print("无效选择，请重新输入！")

# 调用主函数
if __name__ == "__main__":
    main()

