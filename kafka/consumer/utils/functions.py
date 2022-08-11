# Python imports
import sys
import time
import asyncio
import logging
#Imports extras:
from kafka import KafkaConsumer
# Proyect Imports
from utils import constants as zconsts

# Initializations
logger = logging.getLogger("Functions")

# Our functions
def create_consumer():
    while True:#loop infinito waiting till kafka is online
        try:
            consumer = KafkaConsumer(
                zconsts.KAFKA_TOPIC,
                group_id=1,
                bootstrap_servers=[zconsts.KAFKA_URL],
                auto_offset_reset='beginning',
                enable_auto_commit=True,
                session_timeout_ms=zconsts.WAIT_TIME              
            )
            #if this succeed:
            logging.info("Begin reading Kafka Service in %s...", format(zconsts.KAFKA_URL))
            return consumer

        except:#If kafka not online
            time.sleep(5)#we wait one more second
            logging.warning("Waiting for Kafka Service in %s...", format(zconsts.KAFKA_URL))