from apscheduler.schedulers.background import BackgroundScheduler
import time
from django.core.cache import cache
from log.logger import logger
from log.models import Action
from article.models import Blog

# 创建异步调度器对象
scheduler = BackgroundScheduler()


# 更新排行榜
def update_top_k():
    logger.info('开始更新排行榜...')
    # 刷新排行榜
    RequestRecord.stat_top()
    logger.info('排行榜更新完成...')


# 更新用户行为数据
def update_action_data():
    action_data = Action.summary()
    cache.set('action_data', action_data)
    logger.info(f'对用户的行为数据进行了统计更新...')


# 更新推荐列表
def update_recommend_list():
    action_data = cache.get('action_data') or {}

    # 更新推荐列表
    user_recommend_queue = cache.get('user_recommend_queue')
    logger.info(f'待计算的用户推荐列表:[大小:{len(user_recommend_queue)}]:{user_recommend_queue}')
    t1 = time.time()
    while user_recommend_queue:
        t2 = time.time()
        if t2 - t1 > 150:
            logger.info(f'当前计算耗时超过150s,退出计算...')
            break
        user = user_recommend_queue.pop()
        recommend_list = Blog.recommend(user, action_data)
        t3 = time.time()
        logger.info(f'为用户[{user}]计算推荐列表耗时:{t3 - t2}...')
        cache.set(f'{user}_recommend_list', recommend_list)
        cache.set('user_recommend_queue', user_recommend_queue)
    logger.info(f'当前计算推荐列表结束，剩余{len(user_recommend_queue)}条待计算...')


scheduler.add_job(update_top_k, trigger='interval', seconds=3600, max_instances=10)
#scheduler.add_job(update_action_data, trigger='interval', seconds=1800, max_instances=10)
#scheduler.add_job(update_recommend_list, trigger='interval', seconds=300, max_instances=10)

scheduler.start()
