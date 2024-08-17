class MinMax(object):
    """
    最小と最大を求める
    """
    def __init__(self):
        """
        初期化
        """
        self.tl1 = None
        self.tl0 = None
        self.list = [[10, 123], [20, 136], [30, 143], [25, 150], [15, 100]]
        print("list=%s" % list(self.list))

    def create_variables(self):
        """
        変数に代入する
        """
        _d = dict()
        for _i, _v in enumerate(self.list):
            _d[_i] = _v
        _range = _d.keys()
        self.tl0 = list(map(lambda i: _d[i][0], _range))
        self.tl1 = list(map(lambda i: _d[i][1], _range))

    def min_max(self):
        """
        最小と最大を求める
        :return:
        """
        _min_0 = min(self.tl0)
        _max_0 = max(self.tl0)
        _min_1 = min(self.tl1)
        _max_1 = max(self.tl1)
        _min_max = [(_min_0, _max_0), (_min_1, _max_1)]
        print("Minimum and Maximum values:", _min_max)


if __name__ == "__main__":
    mm = MinMax()
    mm.create_variables()
    mm.min_max()
