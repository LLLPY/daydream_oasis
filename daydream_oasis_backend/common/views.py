from rest_framework.decorators import action


class FrontConfigViewSet:
    '''前端的配置接口'''

    @action(methods=['get', ], detail=False)
    def get_nav_config(self):
        pass

    @action(methods=['get', ], detail=False)
    def get_sidebar_config(self):
        pass
