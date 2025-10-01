import paho.mqtt.client as mqtt
import argparse
from datetime import datetime
import time

VERSION = "1.0.0"

class eLinkMQTTBroker:
    def __init__(self,
                 broker_address="localhost",
                 broker_port=1883,
                 username=None,
                 password=None,
                 command_topic="Command_Topic",
                 data_topic="Data_Topic",
                 info_topic="Info_Topic",
                 ota_topic="OTA_Topic"):
                 
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.username = username
        self.password = password
        self.command_topic = command_topic
        self.data_topic = data_topic
        self.info_topic = info_topic
        self.ota_topic = ota_topic
        self.allowed_commands = ["IDL", "SRT", "PNG", "SND", "MSR", "OTA", "SET", "GET", "RST"]

        self.client = mqtt.Client()
        if self.username and self.password:
            self.client.username_pw_set(self.username, self.password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(self.broker_address, self.broker_port)
        self.client.loop_start()

        # Callback placeholders
        self.on_data = None
        self.on_info = None
        self.on_ota = None

    def on_connect(self, client, userdata, flags, rc):
        # Subscribe to topics for responses from Smart Joint
        client.subscribe(self.data_topic)
        client.subscribe(self.info_topic)
        client.subscribe(self.ota_topic)

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode()
        if topic == self.data_topic and self.on_data:
            self.on_data(payload)
        elif topic == self.info_topic and self.on_info:
            self.on_info(payload)
        elif topic == self.ota_topic and self.on_ota:
            self.on_ota(payload)

    def send_command(self, command, cfg_var=None, cfg_idx=None, cfg_val=None):
        """
        Send a command to the Smart Joint.
        Format: <Comando>,<cfg_var>,<cfg_idx>,<cfg_val>
        If only command is provided, sends just the command.
        """
        if command not in self.allowed_commands:
            print(f"Comando non valido: {command}")
            return False
        if cfg_var is not None and cfg_idx is not None and cfg_val is not None:
            payload = f"{command},{cfg_var},{cfg_idx},{cfg_val}"
        else:
            payload = f"{command}"
        info = self.client.publish(self.command_topic, payload)
        if info.rc == mqtt.MQTT_ERR_SUCCESS:
            print("Messaggio pubblicato con successo")
            return True
        else:
            print("Errore nella pubblicazione:", info.rc)
            return False

    def set_data_callback(self, callback):
        self.on_data = callback

    def set_info_callback(self, callback):
        self.on_info = callback

    def set_ota_callback(self, callback):
        self.on_ota = callback

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

class eLinkMQTTCallbacks:
    def __init__(self):
        self.last_data = None
        self.last_info = None
        self.last_ota = None
        self.clock_freq = 80000000
        self.press_FS = 50

    def data_callback(self, msg):
        try:
            parts = msg.split(",")
            data = {
                "ID" : int(parts[0]),
                "Press": int(parts[1]) * self.press_FS / 4096,
                "FLow": self.clock_freq / int(parts[2]),
                "ax": int(parts[3]) * 0.061,
                "ay": int(parts[4]) * 0.061,
                "az": int(parts[5]) * 0.061,
                "Vbatt": int(parts[6]) * 0.001,
                "I1": (((int(parts[7]) >>3) if int(parts[7]) < 0x8000 else (int(parts[7]) - 0x10000) >>3) * 0.00004 / 0.08),
                "I2": (((int(parts[8]) >>3) if int(parts[8]) < 0x8000 else (int(parts[8]) - 0x10000) >>3) * 0.00004 / 0.08),
                "I3": (((int(parts[9]) >>3) if int(parts[9]) < 0x8000 else (int(parts[9]) - 0x10000) >>3) * 0.00004 / 0.08),
                "V1": int(parts[10]) * 0.008,
                "V2": int(parts[11]) * 0.008,
                "V3": int(parts[12]) * 0.008,
                "Temp": int(parts[13]) * 0.0625 if int(parts[13]) < 0x8000 else (int(parts[13]) - 0x10000) * 0.0625
            }
            self.last_data = data
        except Exception as e:
            print(f"Data parse error: {e}")
            self.last_data = msg

    def info_callback(self, msg):
        if len(msg) > 10:
            try:
                parts = msg.split(",")
                status = {
                    "ID": int(parts[0]),
                    "Firmware Version": float(f"{int(parts[1]) >> 8}.{int(parts[1]) & 0xFF}"),
                    "Uptime": datetime(year=int(parts[2]), month=int(parts[3]), day=int(parts[4]), hour=int(parts[5]), minute=int(parts[6]), second=int(parts[7])),
                    "Vbatt": int(parts[8]) * 0.001,
                    "Sampling Freq": int(parts[9]),
                    "Buffering Secs": int(parts[10]),
                    "V1": int(parts[11]) * 0.008,
                    "V2": int(parts[12]) * 0.008,
                    "V3": int(parts[13]) * 0.008,
                    "I1": (((int(parts[14]) >> 3) if int(parts[14]) < 0x8000 else (int(parts[14]) - 0x10000) >> 3) * 0.00004 / 0.08),
                    "I2": (((int(parts[15]) >> 3) if int(parts[15]) < 0x8000 else (int(parts[15]) - 0x10000) >> 3) * 0.00004 / 0.08),
                    "I3": (((int(parts[16]) >> 3) if int(parts[16]) < 0x8000 else (int(parts[16]) - 0x10000) >> 3) * 0.00004 / 0.08),
                    "Temp": (int(parts[17]) * 0.0625 if int(parts[17]) < 0x8000 else (int(parts[17]) - 0x10000) * 0.0625)
                }
                self.last_info = status
            except Exception as e:
                print(f"Info parse error: {e}")
                self.last_info = msg
        else:
            self.last_info = msg  

    def ota_callback(self, msg):
        # Parsing OTA status (OTA_Topic)
        self.last_ota = msg
        print("OTA status:", msg)



# Comandi disponibili

def cmd_idle(iface: eLinkMQTTBroker, *args):    
    ret = iface.send_command("IDL")
    return ret

def cmd_start_measure(iface: eLinkMQTTBroker, *args):
    ret = iface.send_command("SRT")
    return ret

def cmd_ping(iface: eLinkMQTTBroker, *args):
    ret = iface.send_command("PNG")
    if not ret:
        return False
    timeout = 5
    start = time.time()
    while time.time() - start < timeout:
        if iface.on_info and hasattr(iface.on_info, 'last_info') and callbacks.last_info:
            for k in callbacks.last_info.keys():
                print("%-10s: %s" % (str(k), str(callbacks.last_info[k])))
            return True
        time.sleep(0.05)
    print("Timeout: no response received")
    return False

def cmd_send_data(iface: eLinkMQTTBroker, *args):
    ret = iface.send_command("SND")
    if not ret:
        return False
    timeout = 5
    start = time.time()
    while time.time() - start < timeout:
        if iface.on_data and hasattr(iface.on_data, 'last_data') and callbacks.last_data:
            for k in callbacks.last_data.keys():
                print("%-10s: %s" % (str(k), str(callbacks.last_data[k])))
            return True
        time.sleep(0.05)

def cmd_send_measure(iface: eLinkMQTTBroker, *args):
    ret = iface.send_command("MSR")
    if not ret:
        return False
    #DA IMPLEMENTARE

def cmd_ota(iface: eLinkMQTTBroker, *args):
    if len(args) < 2:
        print("Usage: ota <url>")
        return False
    url = args[1]
    ret = iface.send_command("OTA")
    #DA OMPLEMENTARE 
    return ret

def cmd_set_cfg(iface: eLinkMQTTBroker, *args):
    if len(args) < 4:
        print("Usage: set_cfg <cfg_var> <cfg_idx> <cfg_val>")
        return False
    cfg_var = args[1]
    try:
        cfg_idx = int(args[2])
        cfg_val = int(args[3])
    except ValueError:
        print("cfg_idx and cfg_val must be integers")
        return False
    ret = iface.send_command("SET", cfg_var, cfg_idx, cfg_val)
    return ret

def cmd_get_cfg(iface: eLinkMQTTBroker, *args):
    if len(args) < 3:
        print("Usage: get_cfg <cfg_var> <cfg_idx>")
        return False
    cfg_var = args[1]
    if len(args) > 2:
        try:
            cfg_idx = int(args[2])
        except ValueError:
            print("cfg_idx must be an integer")
            return False
    else:
        cfg_idx = 0
    ret = iface.send_command("GET", cfg_var, cfg_idx, 0)
    if not ret:
        return False
    timeout = 5
    start = time.time()
    while time.time() - start < timeout:
        if iface.on_info and hasattr(iface.on_info, 'last_info') and callbacks.last_info:
            print(f"{cfg_var}[{cfg_idx}]: {callbacks.last_info}")
        time.sleep(0.05)
    print("Timeout: no response received")
    return False

def cmd_reset(iface: eLinkMQTTBroker, *args):
    ret = iface.send_command("RST")
    return ret



if __name__ == "__main__":
    print("")
    print("eLink MQTT Interface v" + VERSION)
    print("Stand-alone")
    print("")

    cmds = dict()
    cmds["idle"] = cmd_idle
    cmds["start"] = cmd_start_measure
    cmds["ping"] = cmd_ping
    cmds["send_data"] = cmd_send_data
    cmds["send_meas"] = cmd_send_measure
    cmds["ota"] = cmd_ota
    cmds["set_cfg"] = cmd_set_cfg
    cmds["get_cfg"] = cmd_get_cfg
    cmds["rst"] = cmd_reset


    parser = argparse.ArgumentParser(description="eLink MQTT Interface Command Line")
    parser.add_argument("--cmd", "-c", type=str, help="Command to send", default=["ping"])

    args = parser.parse_args()

    iface = eLinkMQTTBroker()
    callbacks = eLinkMQTTCallbacks()
    iface.set_data_callback(callbacks.data_callback)
    iface.set_info_callback(callbacks.info_callback)
    iface.set_ota_callback(callbacks.ota_callback)

    if cmds[args.cmd[0]](iface, args.cmd):
        print("OK")
        pass
    else:
        print("ERR")

    iface.disconnect()