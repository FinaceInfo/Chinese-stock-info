"""获取各个股票的基本数据
属性包括：

code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数
"""

__all__ = ["StocksBasicCsv"]
from .stock_basic_info import *
from flask.views import MethodView
from flask import make_response

class StocksBasicCsv(MethodView):

    def get(self):
        response = make_response(get_stock_basics_csv())
        response.headers[
            "Content-Disposition"] = "attachment; filename=stocks_basic.csv;"
        return response
