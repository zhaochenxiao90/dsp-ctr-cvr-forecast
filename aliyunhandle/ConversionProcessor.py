import os
from aliyun.log.consumer import ConsumerProcessorBase
class ConversionProcessor(ConsumerProcessorBase):
    def initialize(self, shard):
        pass
    def process(self, log_groups, check_point_tracker):
        for log_group in log_groups.LogGroups:
            items = []
            for log in log_group.Logs:
                item = dict()
                item['time'] = log.Time
                for content in log.Contents:
                    content.Value
                    print(content.Key, content.Value)
                    print("\n")
            # 打印日志
            os._exit(0)
        # check_point_tracker.save_check_point(True)

    def shutdown(self, check_point_tracker):
        check_point_tracker.save_check_point(True)