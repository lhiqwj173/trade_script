"""
20231229
更新交易日历

休市数据获取:
https://www.tdx.com.cn/url/holiday/

"""

import os
from datetime import datetime, timedelta

def produce_trade_date(year:str):
    """
    生成交易日历
    :param year: 年份
    :return: 该年交易日列表
    """
    # 休市数据路径
    rest_path = os.path.join(os.path.dirname(__file__), f'{year}.txt')
    date_path = os.path.join(os.path.dirname(__file__), f'trade_{year}.txt')

    # 检查rest_path
    if not os.path.exists(rest_path):
        print(f'{year}年休市数据不存在\n请先下载休市数据: https://www.tdx.com.cn/url/holiday/')
        return

    # 读取休市数据
    rest_dates = []
    with open(rest_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            rest_dates.append(line[:10].replace('.', '-'))

    trade_dates = []

    # 遍历该年的所有日期
    start_date = datetime(int(year), 1, 1)
    end_date = datetime(int(year) + 1, 1, 1)
    current_date = start_date
    while current_date < end_date:
        # 跳过周末
        if current_date.weekday() in [5, 6]:
            pass
        else:
            date_str = current_date.strftime('%Y-%m-%d')

            # 跳过休市日
            if date_str in rest_dates:
                pass
            else:
                # 交易日
                trade_dates.append(date_str)
                print(date_str)

        # 下一天
        current_date += timedelta(days=1)

    # 写入文件
    with open(date_path, 'w', encoding='utf-8') as f:
        for date in trade_dates:
            f.write(date + '\n')

    print(f'{year}年交易日历生成完毕')
    return trade_dates


if __name__ == '__main__':
    produce_trade_date('2024')