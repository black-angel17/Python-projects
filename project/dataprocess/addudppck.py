
import pyshark
import csv
seconds = ''
pcap_file = pyshark.FileCapture('testing.pcap')
with open('training.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(
    #     ['Packet Number','Time(seconds)' ,'Time_interval', 'Layer','src_ip','scr_port','dst_port','ack_no','tcp_length','socket_count','sql','stream'])
    for packet in pcap_file:
        data = packet.length
        print(packet.number)
        if 'udp' in packet:
            print("Protocol: UDP")
            time = int(float(packet.udp.time_delta))
            data = packet.udp.length

            try:
                # Check if the packet has an IP layer
                if packet.ip.src:
                    src_ip = packet.ip.src
                    print("Source IP:", src_ip)
            except AttributeError:
                print("Packet does not contain an IP layer")
                src_ip = ''

            print(packet.number)
            layer = "UDP"
            csvwriter.writerow(
                [packet.number, time, layer,src_ip, '', '',
                 '', data, 0, '',seconds ,''])
        if 'icmp' in packet:
            print("Protocol: ICMP")
            layer = "ICMP"
            src_ip = packet.ip.src
            time = ''
            csvwriter.writerow(
                [packet.number,seconds, layer, src_ip, '', '',
                 '', data,0,'', time,''])
        elif 'arp' in packet:
            print('arp')
            layer = "ARP"
            print(packet.number)
            src_ip = ''
            time= ''
            csvwriter.writerow(
                [packet.number, seconds, layer, src_ip, '', '',
                 '', data,0,'',time,''])
        elif 'dns' in packet:
            print('Dns')
            layer = "DNS"
            print(packet.number)
            src_ip = packet.ip.src
            time = ''
            csvwriter.writerow(
                [packet.number, seconds, layer, src_ip, '', '',
                 '', data, 0, '', time, ''])
        elif 'dhcp' in packet:
            print('DHCP')
            src_ip = packet.ip.src
            layer = "DHCP"
            print(packet.number)
            time= ''
            csvwriter.writerow(
                [packet.number, seconds, layer, src_ip, '', '',
                 '', data,0,'',time,''])

        else:
            continue