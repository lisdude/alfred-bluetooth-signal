import sys
import json
from workflow import Workflow3
from subprocess import check_output

def main(wf):
    parsed_json = json.loads(check_output(['system_profiler', '-json', 'SPBluetoothDataType']))

    for data in parsed_json['SPBluetoothDataType']:
        for devices in data['device_title']:
            for device_name in devices:
                if not 'device_RSSI' in devices[device_name]:
                    continue
          
                rssi = devices[device_name]['device_RSSI']
                substr = "RSSI: " + str(rssi)
                if rssi >= -60:
                    icon_path = "green.png"
                    substr = substr + " (Strong)"
                elif rssi >= -70:
                    icon_path = "yellow.png"
                    substr = substr + " (Good)"
                elif rssi >= -100:
                    icon_path = "red.png"
                    substr = substr + " (Poor)"
                else:
                    icon_path = "x.png"
                    substr = substr + " (Unusable)"

                if 'device_batteryPercent' in devices[device_name]:
                    substr = substr + "      Battery: " + devices[device_name]['device_batteryPercent']

                wf.add_item(title = device_name, subtitle = substr, icon = icon_path)
    
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))