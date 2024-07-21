import pyshark
import csv
# Open the pcap file
pcap_file = pyshark.FileCapture('testing.pcap')

# Get the timestamp of the first packet
first_packet_time = None
for packet in pcap_file:
    first_packet_time = float(packet.sniff_timestamp)
    break  # Only need the first packet's timestamp
else:
    # If no packets were found, exit
    print("No packets found in the capture file.")
    exit()

# Reset the file capture to read from the beginning again
with open('new1.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(
        ['Packet Number','Time(seconds)' ,'socket_count'])
    seconds =0
    socket = 0
    for packet in pcap_file:
        # Check if the packet has TCP layer and source IP address
        if 'tcp' in packet and 'ip' in packet:
            src_ip = packet.ip.src
            stream = int(packet.tcp.stream)

            current_packet_time = float(packet.sniff_timestamp)
            seconds_since_start = current_packet_time - first_packet_time
            seconds = int(seconds_since_start)
            seq_number = packet.tcp.seq
            ack_number = packet.tcp.ack
            flag1 = str(packet.tcp.flags_ack)
            flag2 = str(packet.tcp.flags_push)
            if src_ip != '192.168.77.131':

                if flag1 == 'True' and flag2 == 'False':
                    if int(seq_number) == 1 and int(ack_number) == 1:
                        print(f"Packet #{packet.number}: {stream}")
                        print(flag1)
                        print(flag2)
                        print('socket detected')
                        socket = socket +1
                        print("socket count ==" + str(socket))
                        print(f"time === {seconds}")
                        csvwriter.writerow(
                            [packet.number, seconds, socket])


        else:
            csvwriter.writerow(
                [packet.number, seconds, socket])

    print(socket)
# Close the pcap file
pcap_file.close()

'''

import pyshark

# Open the pcap file
pcap_file = pyshark.FileCapture('test2.pcap')

# Get the timestamp of the first packet
first_packet_time = None
for packet in pcap_file:
    first_packet_time = float(packet.sniff_timestamp)
    break  # Only need the first packet's timestamp
else:
    # If no packets were found, exit
    print("No packets found in the capture file.")
    exit()

# Reset the file capture to read from the beginning again
pcap_file.close()
pcap_file = pyshark.FileCapture('test1.pcap')

# Loop through each packet in the pcap file
for packet in pcap_file:
    # Calculate the time difference in seconds from the first packet
    current_packet_time = float(packet.sniff_timestamp)
    seconds_since_start = current_packet_time - first_packet_time

    # Print packet summary
    print(f"Packet #{packet.number}: {seconds_since_start:.2f} seconds {packet.transport_layer} {packet.length} bytes")

    # Print packet details
    print("Layers:")
    for layer in packet.layers:
        print(f"Layer: {layer.layer_name}")
        for field in layer.field_names:
            print(f"\t{field}: {getattr(layer, field)}")

# Close the pcap file
pcap_file.close()'''

