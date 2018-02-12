from Util.LRUCache import LRUCache
from Util.singleton import singleton


@singleton
class DataHandle():
    def __init__(self):
        self.Dic_App_Id = LRUCache(1 << 28)
        self.Dic_Ad_Unit_Id = LRUCache(1 << 28)
        self.Dic_Ad_Type = LRUCache(1 << 28)
        self.Dic_Os = LRUCache(1 << 28)
        self.Dic_Region = LRUCache(1 << 28)
        self.Dic_Advertiser_id = LRUCache(1 << 28)
        self.Impressions = LRUCache(1 << 28)
        self.Click = LRUCache(1 << 18)
    def handle(self, LogModel):
        app_id = self.GetDicValue(self.Dic_App_Id, LogModel.request_app_id)
        ad_unit_id = self.GetDicValue(self.Dic_Ad_Unit_Id, LogModel.request_ad_unit_id)
        ad_type = self.GetDicValue(self.Dic_Ad_Type, LogModel.request_ad_type)
        os = self.GetDicValue(self.Dic_Os, LogModel.request_os)
        region = self.GetDicValue(self.Dic_Region, LogModel.request_region)
        advertiser_id = self.GetDicValue(self.Dic_Advertiser_id, LogModel.response_advertiser_id)
        if LogModel.tracking_type == "impression":
            self.Impressions.set(LogModel.request_bid_id, [app_id, ad_unit_id, ad_type, os, region, advertiser_id])
        else:
            self.Click.set(LogModel.request_bid_id, 1)
    def GetDicValue(self, dict, key):
        if dict.get(key, "") == "":
            dict[key] = len(dict) + 1
            return dict[key]
        else:
            return dict.get(key)
