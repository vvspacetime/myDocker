from docker import Client


class Docker(object):

    def __init__(self,base_url = ''):
        self.cli = Client(base_url=base_url)
        self.containers = []
        self.images = 'docker/whalsay'

    def build(self):
        self.cli.build(path='../../dockfiles/'+self.images,rm=True,tag=self.images)

    def create(self):
        container = self.cli.create_container(image=self.images + ':latest',command='cowsay boo',detach=True)
        self.containers.append(container)
        return len(self.containers) - 1

    def remove(self,num):
        self.stop(num)
        container = self.containers[num]
        self.cli.remove_container(container=container)
        self.containers.remove(num)

    def start(self,num):
        self.cli.start(container=self.containers[num])

    def stop(self,num):
        self.cli.stop(container=self.containers[num])