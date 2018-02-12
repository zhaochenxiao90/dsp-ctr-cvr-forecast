import os
from aliyun.log.consumer import LogHubConfig, CursorPosition, ConsumerWorker
from apscheduler.schedulers.tornado import TornadoScheduler
from tornado import ioloop
from tornado.httpserver import HTTPServer
from tornado.web import Application, url

from GbdtLrTrain.BuildLibSvm import Buildlibsvm
from GbdtLrTrain.Predict import PredictHandler, Predict
from Util.singleton import singleton
from aliyunhandle.SampleConsumer import SampleConsumer


@singleton
class AliyunClient():
    def __init__(self):
        endpoint = 'cn-beijing-intranet.log.aliyuncs.com'
        accessKeyId = os.getenv("accessKeyId")
        accessKey = os.getenv("accessKey")
        self.config = LogHubConfig(endpoint,
                                   accessKeyId,
                                   accessKey,
                                   'yumi-dsp',
                                   'dsp_tracking_logs',
                                   "dsp-ctr-cvr-prediction-conversion-log-group",
                                   "consumer A",
                                   CursorPosition.BEGIN_CURSOR,
                                   )
        self.worker = ConsumerWorker(SampleConsumer, self.config)

    def start_work(self):
        self.worker.start()

    def stop_work(self):
        self.worker.shutdown()

    def restart_work(self):
        self.worker = ConsumerWorker(SampleConsumer, self.config)
        self.worker.start()


def InitConfig():
    client = AliyunClient()
    client.worker.start()
    sched = TornadoScheduler()
    sched.add_job(InitModel, 'interval', seconds=60, id="1")
    sched.start()
    ioloop.IOLoop.instance().start()


def InitModel():
    Train_tab, Train_libsvm = Buildlibsvm().Buildlibsvm()
    if len(Train_tab) == 0:
        return

    predict = Predict()
    predict.gbdt_lr_train(Train_tab, Train_libsvm)


if __name__ == '__main__':
    app = Application(
        [
            url(r"/predict", PredictHandler, name="predict"),
        ]
    )
    http_server = HTTPServer(app)
    http_server.listen(8000)
    InitConfig()
