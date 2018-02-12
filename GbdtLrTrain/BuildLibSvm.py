from GbdtLrTrain.DataHandle import DataHandle


class Buildlibsvm:
    def __init__(self):
        self.ok = True
        pass

    def Buildlibsvm(self):

        if self.ok == False:
            return 0, 0

        self.ok = False
        handle = DataHandle()
        Train_tab = []
        Train_libsvm = []

        for key, values in handle.Impressions.items():
            if handle.Click.has_key(key):
                Train_tab.append(1)
            else:
                Train_tab.append(0)
            Train_libsvm.append(values)

        self.ok = True
        return Train_tab, Train_libsvm
