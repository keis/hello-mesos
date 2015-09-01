'''hello world framework

adapted from http://jamesporter.me/2014/11/15/hello-mesos.html
'''

from mesos.interface import Scheduler
from pesos.scheduler import PesosSchedulerDriver as SchedulerDriver
from pesos.vendor.mesos import mesos_pb2
import logging
import uuid
import time

logging.basicConfig(level=logging.DEBUG)

def new_task(offer):
    task = mesos_pb2.TaskInfo()
    id = uuid.uuid4()
    task.task_id.value = str(id)
    task.slave_id.value = offer.slave_id.value
    task.name = "task {}".format(str(id))

    cpus = task.resources.add()
    cpus.name = "cpus"
    cpus.type = mesos_pb2.Value.SCALAR
    cpus.scalar.value = 1

    mem = task.resources.add()
    mem.name = "mem"
    mem.type = mesos_pb2.Value.SCALAR
    mem.scalar.value = 1

    return task


class HelloWorldScheduler(Scheduler):
    def registered(self, driver, framework_id, master_info):
        logging.info("Registered with framework id: %s", framework_id)

    def resourceOffers(self, driver, offers):
        logging.info("Received resource offers: %s", [o.id.value for o in offers])

        for offer in offers:
            task = new_task(offer)
            task.command.value = "echo hello world"
            time.sleep(2)
            logging.info("Launching task {task} "
                         "using offer {offer}.".format(task=task.task_id.value,
                                                       offer=offer.id.value))
            tasks = [task]
            driver.launchTasks([offer.id.value], tasks)


if __name__ == '__main__':
    # give system a while to get online
    time.sleep(20)

    framework = mesos_pb2.FrameworkInfo()
    framework.user = 'root'
    framework.name = 'zoidberg'

    driver = SchedulerDriver(HelloWorldScheduler(),
                             framework,
                             'zk://zookeeper:2181/mesos')
    driver.run()
