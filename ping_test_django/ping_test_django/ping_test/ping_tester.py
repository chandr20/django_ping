import subprocess
import re
import os


class Record_Ping:
    path = r'D:\temp1'


    def __init__(self, iplist):
        self.iplist = iplist
        self.filepath = os.path.join(Record_Ping.path,"ping_test")
        self.ip = None
        self.sent = None
        self.recieve = None
        self.lost = None

    def get_file_append(self):
        ipfile = open(self.filepath, "r+")
        return ipfile

    def ping_test(self):

        process = subprocess.Popen("ping {} -n 5".format(self.iplist), stdout=self.get_file_append(), shell=True)
        process.wait()

    def retreive_param(self):
        sent_pattern = re.compile(r'(Sent\s?)(=)(\s?\d*)')
        receive_pattern = re.compile(r'(Received\s?)(=)(\s?\d*)')
        Lost_pattern = re.compile(r'(Lost\s?)(=)(\s?\d*)')
        ip_pattern = re.compile(r'[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}')
        with open(self.filepath) as f:

            for line in f:
                if "Ping statistics" in line:
                    ip = ip_pattern.search(line)
                    self.ip = ip.group(0)
                elif "Packets" in line:
                    sent = sent_pattern.search(line)
                    self.sent = sent.group(3)
                    Recieve = receive_pattern.search(line)
                    self.recieve = Recieve.group(3)
                    Lost = Lost_pattern.search(line)
                    self.lost = Lost.group(3)

                if self.ip and self.sent and self.recieve and self.lost is not None:
                    return [self.sent,self.recieve,self.lost]

    def perform_test(self):
        self.ping_test()
        samp = self.retreive_param()
        return samp