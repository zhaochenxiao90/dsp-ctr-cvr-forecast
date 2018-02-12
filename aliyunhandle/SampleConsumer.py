import json

from aliyun.log.consumer import ConsumerProcessorBase

# 实现读取sls日志数据
from GbdtLrTrain.DataHandle import DataHandle
from model.LogModel import LogModel


class SampleConsumer(ConsumerProcessorBase):
    def initialize(self, shard):
        pass

    def process(self, log_groups, check_point_tracker):
        dataHandle = DataHandle()
        for log_group in log_groups.LogGroups:
            for log in log_group.Logs:
                item = dict()
                item['time'] = log.Time
                for content in log.Contents:
                    item[content.Key] = content.Value
                    if "click" in content.Value or "impression" in content.Value:
                        datas = json.loads(content.Value)
                        logModel = LogModel()
                        logModel.__dict__ = datas
                        dataHandle.handle(logModel)

    def shutdown(self, check_point_tracker):
        pass
