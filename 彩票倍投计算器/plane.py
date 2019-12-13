"""
倍投计算器

使用说明：
实例化Plane类，传参（几个码，赔率）
类属性可以进行修改
实例属性需要用时传参
"""



class Plane:
    # 起投金额
    start_price = 10
    # 倍投倍率
    bt_num = 3

    def __init__(self, ma_no, pv):
        # ---基本---
        # 几码
        self.ma_no = ma_no
        # 赔率
        self.pv = pv
        # ---临时数据---
        # 总成本
        self.coast = 0
        # 投注倍数
        self.current = None

    def get_plane(self, n_times):
        """获取N次的投注金额"""
        # li = [i*6 for i in range(1,n_times+1)]
        # print(li)
        for i in range(n_times):
            # 本次投注所需
            one_ball = self.current = self.start_price if self.current == None else round(self.current*self.bt_num)
            now_coast = self.ma_no*one_ball
            # 总的成本
            self.coast += now_coast
            # 如果中奖
            now_win = self.pv*one_ball
            # 净赚
            res_win = now_win - self.coast
            print(f'第{i+1}期，每球投注{one_ball}，收益{res_win:.2f}元:当前成本{now_coast}-总成本{self.coast}')

obj = Plane(6,9.95)
obj.get_plane(10)
print('...')
obj = Plane(6,9.8)
obj.get_plane(10)
