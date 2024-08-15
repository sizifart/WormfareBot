from utilities.wormfare import WormfareBot
from asyncio import sleep
from random import uniform
from data import config
from utilities.core import logger
import asyncio
from aiohttp.client_exceptions import ContentTypeError
from utilities.telegram import Accounts
import datetime
import pandas as pd
import os


async def wormfareStart(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    wormfare = await WormfareBot.create(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'

    await sleep(uniform(config.DELAYS['ACCOUNT'][0], config.DELAYS['ACCOUNT'][1]))

    while True:
        try:
            
            await wormfare.login()

            await sleep(30)

        except ContentTypeError as e:
            logger.error(f"Wormfare | Thread {thread} | {account} | Error: {e}")
            await asyncio.sleep(120)

        except Exception as e:
            logger.error(f"Wormfare | Thread {thread} | {account} | Error: {e}")

async def wormfareStats():
    # accounts = await Accounts().get_accounts()
    # tasks = []
    # for thread, account in enumerate(accounts):
    #     session_name, phone_number, proxy = account.values()
    #     # Создаем экземпляр Vertus, используя метод create
    #     vertus_instance = await Vertus.create(thread=thread, session_name=session_name, phone_number=phone_number, proxy=proxy)
    #     # Добавляем задачу вызова stats() для созданного экземпляра
    #     tasks.append(asyncio.create_task(vertus_instance.stats()))
    
    # data = await asyncio.gather(*tasks)
    # path = f"statistics/statistics_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
    # columns = ['Registered', 'Phone number', 'Name', 'Balance', 'Referrals', 'Referral link', 'Wallet', 'Proxy (login:password@ip:port)']
    # if not os.path.exists('statistics'): os.mkdir('statistics')
    # df = pd.DataFrame(data, columns=columns)
    # df.to_csv(path, index=False, encoding='utf-8-sig')
    # logger.success(f"Saved statistics to {path}")
    pass