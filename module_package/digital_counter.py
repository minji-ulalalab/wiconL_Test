from queue import Queue
import time
from enum import Enum

class STATE(Enum):
    INIT_PROTOCOL = 1
    MAKE_PROTOCOL = 2


class DigitalCounter:
    wicon_id = "WF-001412"
    device_ver = 'v1.001'
    temp = '23.5'
    humi = '60'
    vibr = '0'

    state = None
    msg = None
  
    start_time = None
    end_time = None

    _count = 0
    _flag = False


    def run(self, queue):
        print("run digital_counter thread")
        try:
            self.state = STATE.INIT_PROTOCOL
            while True:
                
                if(self.state == STATE.INIT_PROTOCOL):#시작메세지
                    print("STATE.INIT_PROTOCOL")
                    self.msg = self.wicon_id + ",000000000000,"+ self.device_ver +",000,0.0000,0.0000,0.0000,0.0000\n"
                    queue.put(self.msg)
                    self.state = STATE.MAKE_PROTOCOL
                    
                elif(self.state == STATE.MAKE_PROTOCOL):
                    print("STATE.MAKE_PROTOCOL")
                    self.set_counter()
                    send_time = time.strftime('%y%m%d%H%M%S', time.gmtime())
                    self.msg = "%s,%s,%s,001,-99,%s,%s,%s,%s\n"%(self.wicon_id, send_time, self.device_ver, self.temp, self.humi, self._count, self.vibr)
                    queue.put(self.msg)
                    print("큐에 저장완료")

        except Exception as ex:
            print(ex)

    def set_counter(self):
        if(self._count > 65535):  #65535가되면 0으로 돌아간다
            self._count = 0
        self._count += 1 # 1씩 증가
        time.sleep(1) #1초 마다

        